<template>
  <div class="yoga-type-filter mb-4">
    <h4 class="mb-3">Filter by Yoga Type</h4>
    <div class="btn-group" role="group">
      <button 
        type="button" 
        class="btn" 
        :class="activeType === '' ? 'btn-primary' : 'btn-outline-primary'"
        @click="setFilter('')"
      >
        All Types
      </button>
      <button 
        v-for="type in yogaTypes" 
        :key="type" 
        type="button" 
        class="btn" 
        :class="activeType === type ? 'btn-primary' : 'btn-outline-primary'"
        @click="setFilter(type)"
      >
        [[ type ]]
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, ref } from 'vue';
import { YogaType } from '../types';

export default defineComponent({
  name: 'YogaTypeFilter',
  props: {
    initialType: {
      type: String as PropType<YogaType | ''>,
      default: ''
    }
  },
  setup(props, { emit }) {
    const yogaTypes: YogaType[] = [
      'Burnout-Yogini',
      'Ashtanga-Warrior',
      'Homeoffice-Yogini',
      'Casual-Stretcher'
    ];
    
    const activeType = ref<YogaType | ''>(props.initialType);
    
    const setFilter = (type: YogaType | ''): void => {
      activeType.value = type;
      emit('filter-change', type);
    };
    
    return {
      yogaTypes,
      activeType,
      setFilter
    };
  }
});
</script>

<style scoped>
.yoga-type-filter .btn-group {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.yoga-type-filter .btn {
  border-radius: 20px;
  padding: 0.375rem 1rem;
}
</style>