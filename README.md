# Yogi  

Yogi is a web app that helps you find the most suitable yoga class for your needs—quickly, simply, and based on your preferences.  

![Tests](https://github.com/vs3kulic/yogi/actions/workflows/django_test.yml/badge.svg)

---

## How It Works  

- We ask you a few questions to get to know your preferences.  
- Based on your answers, we match you with one of our classes.  
- Before joining, you can preview some content and information about your matched class.  

All of this runs on a subdomain of [bekindstudio.at](https://bekindstudio.at).  

---

## Microservice Architecture  

Yogi is designed as a **microservice** that integrates seamlessly into the broader be kind studio ecosystem. It operates independently while communicating with other services to provide a cohesive user experience.  

### Key Characteristics of the Yogi Microservice:  
- **Independent Deployment**: Yogi can be deployed and scaled independently of other services.  
- **API-Driven**: Yogi communicates with other services via REST APIs for data exchange.  
- **Focused Functionality**: Yogi specializes in personalized yoga class recommendations.  
- **Error Isolation**: Issues in Yogi do not affect other services in the ecosystem.  

---

## Features  

- **Personalized class recommendations** based on your input.  
- **Preview class content** before joining.  
- **Comprehensive testing** with unit tests and end-to-end tests.
- **Continuous Integration** with GitHub Actions to ensure code quality.
- **Error monitoring** with Honeybadger to track and resolve issues in production.  
- **User analytics** with Piwik to understand user behavior and improve the app experience. 
- **Images** delivered through a dedicated CDN to enhance performance and reduce storage requirements.
- **Environment-specific configurations** for development, testing, and production.

---

## Development Setup

### Prerequisites
- Python 3.11+
- MySQL (for production/development)
- Node.js (optional, for frontend enhancements)

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

---

## Error Monitoring with Honeybadger  

We use **Honeybadger** to monitor errors and exceptions in the Yogi app. Honeybadger helps us identify and resolve issues in real-time, ensuring a smooth user experience.  

### Setting Up Honeybadger  

1. Install the Honeybadger Python library:  
   ```bash  
   pip install honeybadger  
   ```

2. Add your Honeybadger API key to the environment variables:  
   ```bash  
   export HONEYBADGER_API_KEY=<your-api-key>  
   ```

3. Honeybadger is already integrated into the app. Errors will automatically be logged and reported to the Honeybadger dashboard.  

---

## User Analytics with Piwik  

We use **Piwik** (Matomo) for tracking user behavior and analytics, without capturing personal data. Piwik helps us understand how users interact with the app, enabling us to make data-driven improvements.  

### How Piwik is Integrated  

1. The Piwik tracking code is included in the `base.html` template.  
2. It tracks page views, user interactions, and other key metrics.  
3. Analytics data is available in the Piwik dashboard for analysis.  

### Notes on Piwik  
- To modify the Piwik integration, update the tracking code in `base.html`.  

---

## Pre-Commit Hook  

To maintain code quality and ensure tests are run before committing, we use a pre-commit hook. This hook automatically runs the Playwright test suite before each commit.  

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

Stay tuned for setup instructions and contribution guidelines as the project evolves.
