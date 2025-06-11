<template>
  <div class="result-type-display">
    <div class="card">
      <div class="card-header bg-light">
        <h3 class="m-0">Your Yoga Type: [[ resultType ]]</h3>
      </div>
      
      <div class="card-body">
        <div class="type-description" v-if="typeDescription">
          <p class="lead">[[ typeDescription ]]</p>
        </div>
        
        <div class="recommended-classes mt-4">
          <h4>Recommended Classes</h4>
          <p v-if="!hasClasses">No recommended classes found.</p>
          
          <slot name="classes"></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, computed } from 'vue';
import { YogaType } from '../types';

export default defineComponent({
  name: 'ResultTypeDisplay',
  props: {
    resultType: {
      type: String as PropType<YogaType>,
      required: true
    },
    hasClasses: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    // Computed property to get description based on type
    const typeDescription = computed((): string => {
      switch (props.resultType) {
        case 'Burnout-Yogini':
          return 'You need yoga that helps you relax and reduce stress. Focus on gentle flows and restorative poses.';
        case 'Ashtanga-Warrior':
          return 'You thrive in dynamic, strength-building practices. Energetic sequences and challenges are perfect for you.';
        case 'Homeoffice-Yogini':
          return 'Your practice should address sitting for long periods. Focus on posture improvement and mobility.';
        case 'Casual-Stretcher':
          return 'You benefit from accessible, gentle yoga that improves flexibility and overall wellbeing.';
        default:
          return '';
      }
    });
    
    return {
      typeDescription
    };
  }
});
</script>

<style scoped>
.result-type-display {
  margin-bottom: 2rem;
}

.type-description {
  border-left: 4px solid #8c61b0;
  padding-left: 1rem;
  margin-bottom: 1.5rem;
}
</style>