# Yogi  

Yogi is a web app that helps you find the most suitable yoga class for your needs—quickly, simply, and based on your preferences.  

![Tests](https://github.com/vs3kulic/yogi/actions/workflows/django_test.yml/badge.svg)

---

## How It Works  

- We ask you a few questions to get to know your preferences.  
- Based on your answers, we match you with a Yoga type.  
- You get a recommendation and can view classes or subscribe to our newsletter.  

All of this runs on a subdomain of [bekindstudio.at](https://bekindstudio.at).

---

## Architecture  

Yogi is designed with a hybrid architecture that combines Django templates with Vue.js components where needed:

- **Django Backend**: Handles routing, authentication, data processing, and template rendering.
- **Vue.js Frontend**: Provides interactive elements for features like the class explorer and questionnaire.

This hybrid approach leverages Django's robust backend capabilities while enhancing the user experience with Vue.js for interactive components.

### Key Characteristics:  
- **Independent Deployment**: Yogi can be deployed and scaled independently of other services.  
- **Focused Functionality**: Personalised yoga class recommendations with dynamic content.

---

## Features  

- **Class recommendations** based on user input.  
- **Dark mode support** for comfortable viewing in any lighting condition.  
- **Responsive design** optimized for mobile, tablet, and desktop devices.  
- **Comprehensive testing** with unit tests and end-to-end tests.  
- **Continuous Integration** with GitHub Actions to ensure code quality.  
- **Error monitoring** with Honeybadger to track and resolve issues in production.  
- **User analytics** with Piwik (Matomo) to understand user behavior and improve the app experience.  
- **Images** delivered through a dedicated CDN to enhance performance and reduce storage requirements.  
- **Environment-specific configurations** for development, testing, and production.  
- **Pro-Tips with OLLAMA and DEEPL**: Yogi uses **Ollama** (gemma3:1b) to generate pro-tips based on user questionnaire answers and **DeepL** to translate these pro-tips into German

---

## Development Setup

### Prerequisites
- Python 3.11+
- MySQL (for production/development)
- Node.js 18+ (for Vue.js development)
- npm or yarn

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vs3kulic/yogi.git
   cd yogi
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - For development, use the provided SQLite database.
   - For production, configure MySQL and import the schema from `db/schema.sql`.

5. Configure environment variables:
   - Copy the example environment file:  
     ```bash
     cp .env.example .env
     ```
   - Update the `.env` file with your configuration, including database settings and API keys.

6. (Optional) Install Node.js dependencies for frontend development:
   ```bash
   npm install
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the app at `http://localhost:8000`.

### Testing

To run the test suite, including unit tests and Playwright end-to-end tests:

1. Ensure the development server is running.
2. In a new terminal, activate the virtual environment and run:
   ```bash
   playwright install
   playwright test
   ```

### Continuous Integration

This project uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/django_test.yml`. It includes steps for:

- Setting up the Python environment.
- Installing dependencies.
- Running tests.
- Linting code with flake8.
- Building and pushing Docker images (for production).

## Pre-Commit Hook  

To maintain code quality and ensure tests are run before committing, we use a pre-commit hook. This hook automatically runs the Playwright test suite before each commit 

### Setting Up the Pre-Commit Hook  

1. Install the pre-commit hook:  
   ```bash  
   playwright install  
   ```

Now, every time you commit, the Playwright tests will run automatically. If the tests fail, the commit will be aborted. 

To skip the pre-commit hook for a specific commit, use:  
```bash  
git commit --no-verify  
```

---

## Get Involved  

Stay tuned for setup instructions and contribution guidelines as the project evolves!
