import { createApp } from 'vue';
import App from './App.vue';

// Only initialize Vue if we're on a page that should have Vue functionality
const currentPath = window.location.pathname;
const isYogaPage = currentPath === '/result/' || currentPath === '/recommended_classes/';

if (isYogaPage) {
  const app = createApp(App);
  app.mount('#app');
  console.log('Vue app mounted for yoga page');
} else {
  console.log('Not a yoga page, Vue not initialized');
}