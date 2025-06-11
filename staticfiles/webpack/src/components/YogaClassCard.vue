<template>
  <div class="card yoga-class-card mb-3">
    <div class="card-body">
      <h5 class="card-title">[[ yogaClass.name ]]</h5>
      <h6 class="card-subtitle mb-2 text-muted">[[ yogaClass.yoga_type ]]</h6>
      
      <div v-if="yogaClass.key_features" class="key-features">
        <h6 class="features-title">Key Features:</h6>
        <p class="card-text">[[ yogaClass.key_features ]]</p>
      </div>
      
      <div class="ideal-for mt-3">
        <h6>Ideal For:</h6>
        <p class="card-text">[[ yogaClass.ideal_for ]]</p>
      </div>
      
      <div class="d-grid gap-2 mt-3">
        <button class="btn btn-primary" @click="selectClass">
          Learn More
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { YogaClass } from '../types';

export default defineComponent({
  name: 'YogaClassCard',
  props: {
    yogaClass: {
      type: Object as PropType<YogaClass>,
      required: true
    }
  },
  setup(props, { emit }) {
    const selectClass = (): void => {
      emit('select', props.yogaClass);
    };
    
    return {
      selectClass
    };
  }
});
</script>

<style scoped>
.yoga-class-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.yoga-class-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.key-features, .ideal-for {
  border-top: 1px solid #eee;
  padding-top: 10px;
}

.features-title {
  font-size: 0.9rem;
  color: #6c757d;
  text-transform: uppercase;
  letter-spacing: 1px;
}
</style>