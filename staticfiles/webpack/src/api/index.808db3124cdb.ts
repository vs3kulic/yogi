export const fetchYogaClasses = async () => {
  try {
    // Get the current path
    const currentPath = window.location.pathname;
    
    // Only make API calls on relevant pages
    if (currentPath !== '/result/' && currentPath !== '/recommended_classes/') {
      console.log('Not on a yoga page, skipping API call');
      return [];
    }
    
    const response = await fetch('/api/yoga-classes/');
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching yoga classes:', error);
    return []; // Return empty array on error
  }
};