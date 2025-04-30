# Yogi  

Yogi is a web app that helps you find the most suitable yoga class for your needs-quickly, simply, and based on your preferences.  

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
- **Data-driven evaluation:** At the end, we (be kind) can analyze how good the recommendation was using internal data.  
- **Potential for machine learning** to improve recommendations over time.  
- **Automated testing** with Playwright to ensure the app works as expected.  

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

## Notes  

- We use the term "classes" instead of "courses".  
- Class content and requirements will be provided by the be kind team.  

---

## Get Involved  

Stay tuned for setup instructions and contribution guidelines as the project evolves.
