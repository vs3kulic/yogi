<template>
  <!-- Super clean template with no filter -->
  <div class="class-results">
    <!-- Only classes, no filter -->
    <div v-if="classes.length > 0" class="row">
      <div v-for="yogaClass in classes" :key="yogaClass.id" class="col-md-6 mb-4">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">{{ yogaClass.name }}</h5>
            <p class="card-text">{{ yogaClass.description }}</p>
          </div>
          <div class="card-footer bg-transparent">
            <span class="badge bg-primary me-2">{{ yogaClass.yoga_type }}</span>
            <span class="badge bg-secondary">{{ yogaClass.duration }} min</span>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="alert alert-info">
      Loading classes...
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, PropType } from 'vue';
import { YogaClass } from '../types';

export default defineComponent({
  props: {
    initialClasses: {
      type: Array as PropType<YogaClass[]>,
      default: () => []
    },
    initialResultType: String,
    showFilters: Boolean
  },
  setup(props) {
    const classes = ref<YogaClass[]>([]);
    
    onMounted(() => {
      // Just use the classes we're given
      classes.value = props.initialClasses;
    });
    
    return {
      classes
    };
  }
});
</script>

<style scoped>
/* No extra styles */
</style>