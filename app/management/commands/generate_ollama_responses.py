from django.core.management.base import BaseCommand
from app.models import OllamaResponse
from app.services.ollama_service import call_ollama
from app.views import load_questions, clean_text
import itertools

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
            # Construct the prompt
            question_answer_pairs = []
            for idx, answer in enumerate(combination):
                question_text = questions[idx]['text']
                answer_text = answer['text']  # Extract the answer text from the dictionary
                question_answer_pairs.append(f"Q: {question_text}\nA: {answer_text}")

            questions_and_answers = "\n\n".join(question_answer_pairs)
            prompt = (
                f"Based on the following questionnaire responses:\n\n"
                f"{questions_and_answers}\n\n"
                f"Provide a personalized yoga tip in Markdown format. Limit to 20 words. Don't mention the word focus."
                f"Change it up, don't repeat the same answer, and don't use the word gentle."
            )

            # Call the Ollama API
            ollama_response = call_ollama(prompt)

            # Save the response to the database if successful
            if "error" not in ollama_response:
                raw_text = ollama_response.get("response", "No response received.")
                cleaned_text = clean_text(raw_text)

                # Save the prompt, response, and combinations to the database
                OllamaResponse.objects.create(
                    prompt=prompt,
                    response=cleaned_text,
                    combinations=[answer['value'] for answer in combination]  # Save the answer keys (e.g., ["A", "C", "B"])
                )
                self.stdout.write(self.style.SUCCESS(f"Saved response for combination: {[answer['value'] for answer in combination]}"))
            else:
                self.stdout.write(self.style.ERROR(f"Error generating response for combination: {[answer['value'] for answer in combination]}"))

        self.stdout.write(self.style.SUCCESS("Successfully generated Ollama responses for all combinations."))
