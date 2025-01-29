# Fellowships

## Description
This repository contains the code for a Django-based web application where users can select characters from the Fellowship of the Ring and engage in battles. The application includes character selection, battle mechanics, and various game features.

## Contents
- `Fellowships/`: Main Django application directory.
  - `__init__.py`
  - `settings.py`
  - `urls.py`
  - `views.py`
  - `game.py`
  - `game_data.py`
  - `characters.py`
  - `templates/`: Directory containing HTML templates.
    - `index.html`
    - `hello_world.html`
  - `static/`: Directory containing static files (CSS, JavaScript, images).
    - `css/`
      - `styles.css`
- `manage.py`: Django management script.

## Usage
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/Fellowships.git
    cd Fellowships
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run migrations**:
    ```sh
    python manage.py migrate
    ```

4. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

5. **Access the application**:
    Open your web browser and navigate to `http://localhost:8000/`.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License
This repository is licensed under the MIT License. See the `LICENSE` file for more details.