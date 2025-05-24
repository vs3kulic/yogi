<template>
  <div class="vue-questionnaire-enhancer card mb-4">
    <div class="card-body">
      <h3>Your Yoga Journey</h3>
      
      <!-- Progress bar -->
      <div class="progress mb-3">
        <div class="progress-bar bg-success" 
             :style="{ width: `${progressPercentage}%` }">
          [[ progressPercentage ]]%
        </div>
      </div>
      
      <!-- Animation on answer selection -->
      <div class="answer-animation text-center mt-3">
        <transition name="fade">
          <span v-if="showAnswerFeedback" class="answer-feedback badge"
                :class="{ 'bg-success': lastAnswerPositive, 'bg-info': !lastAnswerPositive }">
            [[ lastAnswerPositive ? '✓ Gute Wahl!' : '✓ Verstanden!' ]]
          </span>
        </transition>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'QuestionnaireEnhancer',
  data() {
    return {
      currentQuestion: 1,
      totalQuestions: 5,
      showAnswerFeedback: false,
      lastAnswerPositive: true
    };
  },
  computed: {
    progressPercentage(): number {
      return Math.round((this.currentQuestion / this.totalQuestions) * 100);
    }
  },
  methods: {
    detectQuestionnaireData(): void {
      console.log('Detecting questionnaire data...');
      
      // Get current question number and total from the page
      const questionCountElement = document.querySelector('.question-count');
      if (questionCountElement) {
        const text = questionCountElement.textContent || '';
        const match = text.match(/Frage\s+(\d+)\s+von\s+(\d+)/);
        
        if (match) {
          this.currentQuestion = parseInt(match[1], 10);
          this.totalQuestions = parseInt(match[2], 10);
          console.log(`Found question ${this.currentQuestion} of ${this.totalQuestions}`);
        }
      }
      
      // Add event listeners to radio buttons
      const radioButtons = document.querySelectorAll('input[type="radio"]');
      radioButtons.forEach(radio => {
        radio.addEventListener('change', () => {
          this.showAnswerAnimation(true);
        });
      });
    },
    
    showAnswerAnimation(isPositive: boolean): void {
      this.lastAnswerPositive = isPositive;
      this.showAnswerFeedback = true;
      
      setTimeout(() => {
        this.showAnswerFeedback = false;
      }, 2000);
    }
  },
  mounted() {
    console.log('QuestionnaireEnhancer component mounted');
    this.detectQuestionnaireData();
    
    // Show animation on component mount for testing
    setTimeout(() => {
      this.showAnswerAnimation(true);
    }, 500);
  }
});
</script>

<style>
.vue-questionnaire-enhancer {
  margin-bottom: 2rem;
}

.answer-feedback {
  display: inline-block;
  padding: 8px 16px;
  font-size: 1rem;
  font-weight: 500;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

/* Make form elements more interactive */
.form-check-input {
  cursor: pointer;
  transition: all 0.2s ease;
}

.form-check-input:checked + label {
  color: #8c61b0;
  font-weight: 600;
}

button[type="submit"] {
  transition: all 0.3s ease;
}

button[type="submit"]:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>