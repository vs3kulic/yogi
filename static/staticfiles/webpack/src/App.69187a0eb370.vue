<template>
  <div v-if="isYogaPage">
    <yoga-explorer 
      :initial-classes="initialYogaClasses"
      :initial-result-type="resultType"
      :show-filters="false"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from 'vue';
import YogaExplorer from './components/YogaExplorer.vue';
import { YogaClass, YogaType } from './types';

export default defineComponent({
  name: 'App',
  components: {
    YogaExplorer
  },
  setup() {
    const isYogaPage = ref<boolean>(false);
    const resultType = ref<YogaType | ''>('');
    const initialYogaClasses = ref<YogaClass[]>([]);
    const currentPath = computed(() => window.location.pathname);
    
    const detectPage = (): void => {
      // ONLY show on recommended_classes page, NOT on result page
      isYogaPage.value = currentPath.value === '/recommended_classes/';
      
      if (isYogaPage.value && window.yogaData) {
        initialYogaClasses.value = window.yogaData.classes || [];
        resultType.value = window.yogaData.result_type || '';
      }
    };
    
    onMounted(() => {
      detectPage();
    });
    
    return {
      isYogaPage,
      resultType,
      initialYogaClasses
    };
  }
});
</script>