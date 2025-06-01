from django.core.management.base import BaseCommand
from app.models import OllamaResponse
from app.services.ollama_service import call_ollama
from app.views import load_questions
from app.constants import ollama_dictionary_enhanced  # Import the hardcoded fixes
import unicodedata
import re
import itertools
import re
import language_tool_python

# Initialize German language tool for spell checking
tool = language_tool_python.LanguageTool('de-DE')

def construct_prompt(questions, combination):
    """
    Constructs the prompt based on the questionnaire answers.
    """
    question_answer_pairs = []
    for idx, answer in enumerate(combination):
        question_text = questions[idx]['text']
        answer_text = answer['text']
        question_answer_pairs.append(f"Frage: {question_text}\nAntwort: {answer_text}")

    questions_and_answers = "\n\n".join(question_answer_pairs)
    prompt = (
        "Basierend auf den folgenden Antworten aus dem Fragebogen:\n\n"
        f"{questions_and_answers}\n\n"
        "Gib einen personalisierten Yoga-Tipp."
        "Der Tipp soll locker und freundlich sein, die Du-Form verwenden und maximal 20 Wörter umfassen. "
        "Vermeide Wiederholungen. "
        "Schreibe den Tipp als einen einzigen, vollständigen Satz. "
        "WICHTIG: Schreibe jedes Wort vollständig und korrekt, ohne Silbentrennung, Bindestriche oder Leerzeichen innerhalb von Wörtern. "
        "Verwende keine Anführungszeichen, Bindestriche, Sonderzeichen oder ungewöhnliche Formatierung. "
        "Benutze ausschließlich natürliches, korrektes Deutsch. "
        "Gib nur den Tipp als Markdown-Text zurück, ohne weitere Erklärungen oder Formatierungen."
    )
    return prompt


class Command(BaseCommand):
    help = "Generate Ollama responses based on all combinations of questionnaire answers."

    def handle(self, *args, **kwargs):
        # Load questions and their possible answers
        questions = load_questions()
        if not questions:
            self.stdout.write(self.style.ERROR("No questions found."))
            return

        # Calculate the total number of combinations
        total_combinations = 1
        for question in questions:
            total_combinations *= len(question['answers'])
        self.stdout.write(self.style.SUCCESS(f"Total number of combinations: {total_combinations}"))

        # Generate all possible combinations of answers
        answer_combinations = list(itertools.product(*[q['answers'] for q in questions]))
        self.stdout.write(self.style.SUCCESS(f"Generated {len(answer_combinations)} combinations."))

        # Iterate through each combination
        for combination in answer_combinations:
            prompt = construct_prompt(questions, combination)
            cleaned_prompt = clean_text(prompt)

            if not cleaned_prompt.strip():
                self.stdout.write(self.style.ERROR(f"Skipping combination due to empty prompt: {[answer['value'] for answer in combination]}"))
                continue

            # Call the Ollama API
            ollama_response = call_ollama(cleaned_prompt)
            if "error" in ollama_response:
                self.stdout.write(self.style.ERROR(f"Error generating response for combination: {[answer['value'] for answer in combination]}"))
                continue

            # Apply hardcoded fixes FIRST, then validate
            raw_text = ollama_response.get("response", "Keine Antwort erhalten.")
            cleaned_response = clean_text(raw_text)
            fixed_response = apply_hardcoded_fixes(cleaned_response)  # Apply fixes first!

            # Then validate the FIXED response
            if not is_valid_response(fixed_response):
                self.stdout.write(self.style.WARNING(f"Filtered out junk response for combination: {[answer['value'] for answer in combination]}"))
                continue

            # Save the response to the database
            try:
                OllamaResponse.objects.create(
                    prompt=cleaned_prompt,
                    response=fixed_response,  # Use fixed_response instead of cleaned_response
                    combinations=[answer['value'] for answer in combination]
                )
                self.stdout.write(self.style.SUCCESS(f"Saved response for combination: {[answer['value'] for answer in combination]}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Failed to save response for combination: {[answer['value'] for answer in combination]}"))
                self.stdout.write(self.style.ERROR(f"Error details: {str(e)}"))

        self.stdout.write(self.style.SUCCESS("Successfully generated Ollama responses for all combinations."))

def clean_text(text):
    """
    Cleans and corrects the response text:
    - Normalizes unicode
    - Removes unwanted artifacts (Markdown, pipes, table structures)
    - PRESERVES original spacing for hardcoded fixes
    """
    if not text:
        return ""

    # Normalize unicode
    text = unicodedata.normalize("NFKC", text)

    # Remove leading/trailing quotes and Markdown artifacts
    text = re.sub(r'^["""„`\'\s]+|["""„`\'\s]+$', '', text)
    
    # Remove leading/trailing whitespace and dashes and - hyphens
    text = re.sub(r'^[\s-]+|[\s-]+$', '', text)

    # Remove Markdown artifacts
    text = re.sub(r"^[-+*]\s*|```.*?```|``` markdown|```|Hier\s+ist\s+der\s+Tipp\s*:", "", text, flags=re.IGNORECASE)

    # Remove the word "markdown" wherever it appears
    text = re.sub(r"\bmarkdown\b", "", text, flags=re.IGNORECASE)

    # Remove pipes and table-like structures
    text = re.sub(r"\|", "", text)
    text = re.sub(r"-{2,}\|", "", text)

    # DON'T normalize spaces here - let apply_hardcoded_fixes handle it!
    # text = re.sub(r"\s+", " ", text)  # REMOVE THIS LINE

    # Remove unnecessary spaces around punctuation
    text = re.sub(r"\s+([?.!,])", r"\1", text)

    # Fix hyphenation issues
    text = re.sub(r"\s+-\s+", "-", text)

    # Add spaces between camel-cased words
    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)

    # Remove space before punctuation
    text = re.sub(r"\s+([?.,!])", r"\1", text)

    # Strip leading and trailing spaces
    return text.strip()

def is_valid_response(text):
    """
    Filters out junk responses:
    - Too many symbols or dashes
    - Too many split words
    - Empty or too short
    """
    if not text or len(text) < 5:  # Reduced minimum length from 10 to 5
        return False
    if re.search(r'-{10,}|–{10,}', text):  # Allow shorter sequences of dashes
        return False
    # Allow up to 4 split words in a row (e.g., "Kon zent riere dich")
    # This line is rejecting fixable responses
    # if re.search(r'(\w{2,})\s(\w{2,})\s(\w{2,})\s(\w{2,})', text):
    #     return False
    # Allow responses with some symbols if they contain valid words
    if re.fullmatch(r'[\W\d\s]+', text):  # Only symbols or numbers
        return False
    return True

# Apply hardcoded fixes to the response text
def apply_hardcoded_fixes(text):
    """
    Applies hardcoded fixes to the response text.
    """
    # First handle patterns with flexible spacing
    flexible_patterns = {
        r"At\s+me": "Atme",
        r"at\s+me": "atme", 
        r"ents\s+pan\s+ne": "entspanne",
        r"tief\s+ein": "tief ein",
        r"tief\s+durch": "tief durch",
        r"lass\s+los": "lass los",
        r"genie\s+ße": "genieße",
        r"Best\s+es": "Bestes",
        r"inn\s+ere": "innere",
        r"konzent\s+riere": "konzentriere",
        r"Ent\s+spann": "Entspann",
        r"Begin\s+ne": "Beginne",
        r"sp\s+üre": "spüre",
    }
    
    # Apply flexible patterns first
    for pattern, replacement in flexible_patterns.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    # Then apply dictionary fixes
    for key, value in ollama_dictionary_enhanced.items():
        text = re.sub(r'\b' + re.escape(key) + r'\b', value, text, flags=re.IGNORECASE)
    
    # Finally normalize multiple spaces to single spaces
    text = re.sub(r'\s+', ' ', text)
    
    return text