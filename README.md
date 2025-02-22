# Fellowships

A repository for learning Python with Django. This project simulates a simple game where users can select a character, equip artifacts, flip a coin, and then engage in a battle simulation.

## Tech Stack

- **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Bootstrap:** A popular front-end framework for developing responsive and mobile-first websites.
- **MySQL:** A widely used open-source relational database management system.

## Features

- **Character Selection:**  
  Choose your character from a list. Each character has attributes such as attacks, defense, life points, and quotes.
  
- **Artifact Selection:**  
  After selecting a character, equip your main character with an artifact that provides offensive and defensive bonuses. If no artifact is selected, an error message is displayed prompting the user to select an artifact.
  
- **Coin Toss:**  
  Perform a coin toss to decide the attack order during battle. The result is stored in the session and used to determine who attacks first.
  
- **Battle Simulation:**  
  A turn-based battle simulation where characters attack each other until one is defeated. The simulation steps (damage calculations and events) are recorded and displayed to the user.
  
- **Battle Outcomes:**  
  Battle results are saved to the database, including details about the outcome and timestamps.

## Project Structure

- **models.py:**  
  Contains the `Character`, `Artifact`, and `BattleOutcome` models. Artifacts are associated with characters via a ForeignKey, and equipped artifacts add bonuses to the character's attack and defense values during battles.

- **views.py:**  
  Includes views for character selection, artifact selection, coin toss, battle simulation, and battle results. Session data is used to maintain state across steps (e.g., selected character, opponent, coin toss result).

- **templates:**  
  Contains HTML templates for each step — including `select_character.html`, `artifact_selection.html`, `coin_toss_result.html`, `battle.html`, and `battle_results.html` — ensuring a smooth game flow.

- **static/css/styles.css:**  
  Houses custom styles, including dark mode settings and responsive design elements.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<your-username>/fellowships.git
   cd fellowships
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open your web browser and go to `http://127.0.0.1:8000/`

## Conclusion

This project provides a foundational understanding of how to build a simple game using Python and Django. By following the steps outlined in this README, you should be able to set up the project, understand its structure, and run the application locally. 

## Outlook

Future enhancements could include:

- **Additional Artifacts and Characters:** Expand the game by adding more characters and artifacts with unique abilities.
- **Improved UI/UX:** Enhance the user interface and experience with more interactive elements and animations.

Feel free to contribute to the project by submitting pull requests or opening issues on GitHub.