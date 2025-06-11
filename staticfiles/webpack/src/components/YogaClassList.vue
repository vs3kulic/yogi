<template>
  <div class="yoga-class-list">
    <div v-if="loading" class="text-center my-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      <p class="mt-3">Loading yoga classes...</p>
    </div>
    
    <div v-else-if="error" class="alert alert-danger">
      [[ error ]]
    </div>
    
    <div v-else-if="filteredClasses.length === 0" class="alert alert-info">
      No yoga classes found for this type.
    </div>
    
    <div v-else class="row">
      <div v-for="yogaClass in filteredClasses" :key="yogaClass.id" class="col-md-6 col-lg-4 mb-4">
        <yoga-class-card 
          :yoga-class="yogaClass" 
          @select="selectClass"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, ref, computed } from 'vue';
import YogaClassCard from './YogaClassCard.vue';
import { YogaClass, YogaType } from '../types';

export default defineComponent({
  name: 'YogaClassList',
  components: {
    YogaClassCard
  },
  props: {
    classes: {
      type: Array as PropType<YogaClass[]>,
      required: true
    },
    filterType: {
      type: String as PropType<YogaType | ''>,
      default: ''
    },
    loading: {
      type: Boolean,
      default: false
    },
    error: {
      type: String,
      default: ''
    }
  },
  setup(props) {
    const selectedClass = ref<YogaClass | null>(null);
    
    // Computed properties
    const filteredClasses = computed((): YogaClass[] => {
      if (!props.filterType) {
        return props.classes;
      }
      return props.classes.filter(yogaClass => yogaClass.yoga_type === props.filterType);
    });
    
    // Methods
    const selectClass = (yogaClass: YogaClass): void => {
      selectedClass.value = yogaClass;
      console.log('Selected class:', yogaClass);
      // Here you would typically show a modal or navigate to a detail page
    };
    
    return {
      selectedClass,
      filteredClasses,
      selectClass
    };
  }
});
</script>