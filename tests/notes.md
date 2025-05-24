# Implementing Vue.js with TypeScript in Django: Step-by-Step Guide

## Getting Started with Vue.js and TypeScript in Django

### Done 

1. **Add Vue.js to your base template**
   * Include Vue.js CDN in your HTML head
   * Add custom delimiters to avoid conflicts with Django templates
   * Create a container element with id="app" for Vue to mount to

2. **Create directory structure for Vue.js and TypeScript files**
   * Create `static/ts/components/` directory
   * Create `static/ts/app.ts` main file
   * Create `tsconfig.json` configuration file

3. **Create the main Vue application file**
   * Set up the Vue app with custom delimiters
   * Define typed reactive state, methods, and computed properties
   * Mount the app to your container element
   * Use interfaces and types for better code organization

4. **Create custom CSS for fancy styling**
   * Define CSS variables for theming
   * Set up light/dark theme support
   * Add animations and transitions
   * Style cards, buttons, and UI elements

5. **Create Vue components with TypeScript**
   * Define component templates, props with type definitions, and methods
   * Use class-based components with decorators or composition API with type safety
   * Emit typed events for parent components to handle

### Done

6. **Update Django templates to use Vue**
   * Add Vue-specific attributes and directives
   * Use v-for, v-if, v-model for dynamic content
   * Implement event handlers

7. **Update Django views to provide data**
   * Convert model data to JSON format
   * Pass data to templates as context
   * Create helper functions for data transformation

8. **Add FontAwesome for icons**
   * Include FontAwesome CDN in your base template

9. **Create Django models for your data**
   * Define models with appropriate fields and relationships
   * Set up choices for dropdowns and filters

10. **Create API endpoints for Vue to interact with**
    * Implement GET endpoints for retrieving data
    * Implement POST endpoints for form submissions
    * Add proper CSRF protection
    * Handle filtering and searching

11. **Update Django URLs**
    * Create routes for your API endpoints
    * Map page views to templates

12. **Update Vue app to fetch data from API with TypeScript**
    * Use fetch or axios with type definitions for AJAX requests
    * Create interfaces for API responses
    * Handle loading states and errors with proper typing
    * Implement data transformation and filtering with type safety

13. **Run migrations and create sample data**
    * Set up initial database structure
    * Populate with sample content for testing

14. **Implement CSRF token handling for API calls**
    * Extract CSRF token from cookies
    * Include in API request headers
    * Create typed helper functions for API communication

15. **Enhance your app with fancy features**
    * Dark/light theme switching with TypeScript enums
    * Add animations and transitions
    * Create interactive components with proper type definitions
    * Implement loading indicators
    * Add smooth scrolling
    * Use micro-interactions for better UX

## TypeScript Configuration

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "strict": true,
    "jsx": "preserve",
    "importHelpers": true,
    "moduleResolution": "node",
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "sourceMap": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["static/ts/*"]
    },
    "experimentalDecorators": true,
    "lib": ["ESNext", "DOM", "DOM.Iterable"]
  },
  "include": ["static/ts/**/*.ts", "static/ts/**/*.vue"],
  "exclude": ["node_modules"]
}
```

## Best Practices

* Always use custom delimiters in Vue to avoid conflicts with Django templates
* Define interfaces for all API responses and component props
* Use TypeScript's type system to catch errors during development
* Keep Vue data and Django context separate and well-defined
* Handle loading states and errors gracefully
* Store user preferences in localStorage with typed getters and setters
* Use transitions and animations sparingly
* Include proper CSRF protection for all POST requests
* Organize component files in a modular structure
* Create barrel files for easier imports
* Use strict mode in TypeScript for better type safety
* Create typed wrappers for third-party libraries
* Define enums for constants and options
* Use utility types for common transformations

## Vue Component Example with TypeScript

```typescript
// Example component using TypeScript
import { defineComponent, PropType } from 'vue';

interface YogaSession {
  id: number;
  name: string;
  duration: number;
  level: string;
}

export default defineComponent({
  name: 'SessionList',
  props: {
    initialSessions: {
      type: Array as PropType<YogaSession[]>,
      required: true
    }
  },
  data() {
    return {
      sessions: [] as YogaSession[],
      loading: false
    };
  },
  methods: {
    async fetchSessions(): Promise<void> {
      this.loading = true;
      try {
        const response = await fetch('/api/yoga-sessions/');
        if (!response.ok) {
          throw new Error('Failed to fetch sessions');
        }
        this.sessions = await response.json() as YogaSession[];
      } catch (error) {
        console.error('Error fetching sessions:', error);
      } finally {
        this.loading = false;
      }
    }
  },
  mounted() {
    this.sessions = this.initialSessions;
  }
});
```

## API Service with TypeScript

```typescript
// api.ts
import axios, { AxiosInstance, AxiosResponse } from 'axios';

// Define response types
interface YogaSession {
  id: number;
  name: string;
  duration: number;
  level: string;
}

interface User {
  id: number;
  username: string;
  email: string;
}

class ApiService {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: '/api/',
      timeout: 5000,
      headers: {
        'Content-Type': 'application/json'
      }
    });
    
    // Configure CSRF token for Django
    this.client.defaults.xsrfCookieName = 'csrftoken';
    this.client.defaults.xsrfHeaderName = 'X-CSRFToken';
  }

  async getSessions(): Promise<YogaSession[]> {
    const response: AxiosResponse<YogaSession[]> = await this.client.get('/yoga-sessions/');
    return response.data;
  }

  async getSessionById(id: number): Promise<YogaSession> {
    const response: AxiosResponse<YogaSession> = await this.client.get(`/yoga-sessions/${id}/`);
    return response.data;
  }

  async createSession(session: Omit<YogaSession, 'id'>): Promise<YogaSession> {
    const response: AxiosResponse<YogaSession> = await this.client.post('/yoga-sessions/', session);
    return response.data;
  }

  async getCurrentUser(): Promise<User> {
    const response: AxiosResponse<User> = await this.client.get('/current-user/');
    return response.data;
  }
}

export default new ApiService();
```