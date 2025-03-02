# Fellowships Game

Fellowships Game is a Django-based project that simulates epic battles inspired by classic fantasy literature. Players select a character, choose powerful artifacts, and face off against a randomized opponent. In addition to traditional game mechanics, the project includes:

- **Dynamic Quotes:**  
  Fetches lore and quotes from The One API to provide thematic insights and character flavor.

- **Machine Learning Artifact Recommendation:**  
  The app recommends artifacts to players based on historical battle outcomes. A model predicts the probability of winning a battle given the character's and opponent's stats, the selected artifact's properties, and the result of a coin toss.

- **AI-Generated Battle Summaries:**  
  After each battle, a summary is generated using the OpenAI ChatCompletion API (gpt-3.5-turbo), summarizing the battle in under 100 words.

## Tech Stack

- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Bootstrap:** A popular front-end framework for developing responsive and mobile-first websites.
- **MySQL:** A widely used open-source relational database management system.
- **scikit-learn:** A machine learning library in Python used for training the artifact recommendation model.

## Features

- **Character & Artifact Selection:**  
  Players choose their main character and select an artifact that boosts their battle stats. The opponent's artifact is selected automatically and can be viewed before the battle starts.

- **Coin Toss Mechanic:**  
  The order of attack is determined by a simulated coin toss.

- **Battle Simulation:**  
  In each round, characters attack one another until one is defeated. Damage is calculated based on their attack and defense statistics.

- **Quotes from The One API:**  
  Fetches real-time quotes to display lore-related background information, adding depth and immersion.

- **Machine Learning Artifact Recommendation:**  
  The ML app recommends artifacts to players based on historical battle outcomes. The model predicts the probability of winning a battle given the character's and opponent's stats, the selected artifact's properties, and the result of a coin toss.

- **AI-Powered Battle Summaries:**  
  Using OpenAI’s API, the game generates a concise, thematic summary of each battle, offering a unique narrative twist to every fight.

## Project Structure

- **models.py:**  
  Contains the `Character`, `Artifact`, and `BattleOutcome` models. Artifacts are associated with characters via a ForeignKey, and equipped artifacts add bonuses to the character's attack and defense values during battles.

- **views.py:**  
  Includes views for character selection, artifact selection, coin toss, battle simulation, and battle results. Session data is used to maintain state across steps (e.g., selected character, opponent, coin toss result).

- **templates:**  
  Contains HTML templates for each step — including `select_character.html`, `artifact_selection.html`, `coin_toss_result.html`, `battle.html`, and `battle_results.html` — ensuring a smooth game flow.

- **static/css/styles.css:**  
  Houses custom styles, including dark mode settings and responsive design elements.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/fellowships.git
   cd fellowships
   ```

2. **Create a Virtual Environment and Install Dependencies:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. **Environment Variables:**

   Create a `.env` file in the project root (or update it as needed) with the your keys.

4. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

## Usage

1. **Character & Artifact Selection:**  
   Start by selecting a character from the main characters list. Then, on the artifact selection page, choose an artifact to empower your character.

2. **Coin Toss:**  
   After selecting an artifact, you'll be redirected to the coin toss page where the outcome determines who attacks first.

3. **Battle Simulation:**  
   The battle sequence plays out round by round. After the battle, a detailed round-by-round summary is shown along with a concise AI-generated summary.

4. **Quotes & Lore:**  
   Throughout the game, quotes fetched from The One API are displayed to provide lore and enhance the atmospheric storytelling.

## Integrations

- **The One API:**  
  Utilized for fetching LOTR-themed quotes and background lore. Ensure you have a valid API token.

- **OpenAI API:**  
  Used to generate a brief textual battle summary after each battle. The summary is generated dynamically based on the battle events and character data.

## Conclusion

This project provides a foundational understanding of how to build a simple game using Python and Django. By following the steps outlined in this README, you should be able to set up the project, understand its structure, and run the application locally. 

## Outlook

Future enhancements could include:

- **Additional Artifacts and Characters:** Expand the game by adding more characters and artifacts with unique abilities.
- **Improved UI/UX:** Enhance the user interface and experience with more interactive elements and animations.

Feel free to contribute to the project by submitting pull requests or opening issues on GitHub.

## License

[MIT License](LICENSE)