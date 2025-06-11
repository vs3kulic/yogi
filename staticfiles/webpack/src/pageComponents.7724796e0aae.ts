import { createApp } from 'vue';
import QuestionnaireEnhancer from './components/QuestionnaireEnhancer.vue';

// Function to detect current page and mount appropriate components
export function mountPageComponents(): void {
  // Try to detect current page from URL
  const currentPath = window.location.pathname;
  
  // Check if we're on the questionnaire page
  if (currentPath.includes('/questionnaire')) {
    console.log('Questionnaire page detected, mounting enhancer...');
    
    // Create a container for the component if it doesn't exist
    let container = document.getElementById('vue-questionnaire-enhancer');
    if (!container) {
      container = document.createElement('div');
      container.id = 'vue-questionnaire-enhancer';
      
      // Find where to insert it (before the form)
      const questionHeader = document.querySelector('h1.mb-4');
      if (questionHeader) {
        questionHeader.parentNode?.insertBefore(container, questionHeader.nextSibling);
      }
    }
    
    // Mount the component with its own app instance
    const app = createApp(QuestionnaireEnhancer, {
      // Props could go here
    });
    
    // Use the same delimiters as the main app
    app.config.compilerOptions.delimiters = ['[[', ']]'];
    
    // Mount the component
    app.mount('#vue-questionnaire-enhancer');
    console.log('Questionnaire enhancer mounted successfully');
  }
}