# Yogi  

Yogi is a web app that helps you find the most suitable yoga class for your needs—quickly, simply, and based on your preferences.  

---

## How It Works  

- We ask you a few questions to get to know your preferences.  
- Based on your answers, we match you with one of our classes.  
- Before joining, you can preview some content and information about your matched class.  

All of this runs on a subdomain of [bekindstudio.at](https://bekindstudio.at).  

---

## Features  

- **Personalized class recommendations** based on your input.  
- **Preview class content** before joining.  
- **Potential for machine learning** to improve recommendations over time.  
- **Automated testing** with Playwright to ensure the app works as expected.  
- **Error monitoring** with Honeybadger to track and resolve issues in production.  
- **User analytics** with Piwik to understand user behavior and improve the app experience.  

---

## Testing  

We use **Playwright** for end-to-end testing of the Yogi web app. The test suite ensures that critical workflows, such as navigating the homepage and completing the questionnaire, function correctly.  

### Running the Tests  

1. Install Playwright and its dependencies:  
   ```bash  
   pip install playwright  
   playwright install  
   ```

2. Run the Playwright test suite:  
   ```bash  
   playwright test  
   ```

3. To debug tests, run Playwright in non-headless mode:  
   ```bash  
   playwright test --headed  
   ```

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

- The Piwik consent popup is styled to be non-intrusive and user-friendly.  
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
