/**
 * Extremely Aggressive Dark Mode Handler
 */
document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.getElementById('theme-checkbox');
    if (!toggle) return;
    
    function applyDarkModeToElement(element) {
        if (element && element.style) {
            element.style.backgroundColor = '#121212';
            element.style.color = '#e0e0e0';
            element.classList.add('dark-forced');
        }
    }
    
    function enableDarkMode() {
        document.documentElement.classList.add('dark-theme');
        document.body.classList.add('dark-theme');
        
        // Call the empty function - will just remove any existing overlay
        applyDarkModeToEversports();
        
        // Target all elements that might have white backgrounds
        const elementsToTarget = document.querySelectorAll('div, section, article, header, footer, main, aside, card, form');
        elementsToTarget.forEach(el => {
            applyDarkModeToElement(el);
            el.classList.add('dark-forced');
        });
        
        // Specifically target the quiz container
        const quizContainers = document.querySelectorAll('.quiz-container, .questionnaire-container, .card, [role="dialog"]');
        quizContainers.forEach(container => {
            applyDarkModeToElement(container);
            // Also target all children
            const children = container.querySelectorAll('*');
            children.forEach(child => applyDarkModeToElement(child));
        });
        
        localStorage.setItem('darkMode', 'enabled');
    }
    
    function disableDarkMode() {
        document.documentElement.classList.remove('dark-theme');
        document.body.classList.remove('dark-theme');
        
        document.querySelectorAll('.dark-forced').forEach(el => {
            el.classList.remove('dark-forced');
            if (el.style) {
                el.style.backgroundColor = '';
                el.style.color = '';
            }
        });
        
        localStorage.setItem('darkMode', 'disabled');
    }
    
    // Check if dark mode was enabled
    if (localStorage.getItem('darkMode') === 'enabled') {
        enableDarkMode();
        toggle.checked = true;
    }
    
    // Handle toggle changes
    toggle.addEventListener('change', function() {
        if (this.checked) {
            enableDarkMode();
        } else {
            disableDarkMode();
        }
    });
    
    // Apply dark mode immediately if set
    if (localStorage.getItem('darkMode') === 'enabled') {
        enableDarkMode();
    }
    
    // Watch for new elements added to the DOM
    const observer = new MutationObserver(function(mutations) {
        if (localStorage.getItem('darkMode') === 'enabled') {
            mutations.forEach(function(mutation) {
                if (mutation.addedNodes.length) {
                    mutation.addedNodes.forEach(function(node) {
                        if (node.nodeType === 1) { // Element node
                            applyDarkModeToElement(node);
                            // Also handle children
                            if (node.querySelectorAll) {
                                const children = node.querySelectorAll('*');
                                children.forEach(child => applyDarkModeToElement(child));
                            }
                        }
                    });
                }
            });
        }
    });
    
    // Observe the entire document for changes
    observer.observe(document.body, { childList: true, subtree: true });
    
    // Update the applyDarkModeToEversports function
    function applyDarkModeToEversports() {
        // Find and remove ANY overlay elements that might be present
        const overlays = document.querySelectorAll('.dark-mode-overlay');
        overlays.forEach(overlay => overlay.remove());
        
        // Find the Eversports widget
        const widget = document.querySelector('[data-eversports-widget-id]');
        if (widget) {
            // Remove any inline styles that might be affecting visibility
            widget.style.filter = '';
            widget.style.opacity = '';
            
            // Find all iframes within the widget and ensure they're visible
            const iframes = widget.querySelectorAll('iframe');
            iframes.forEach(iframe => {
                iframe.style.filter = '';
                iframe.style.opacity = '';
            });
        }
        
        console.log('Removed all overlays and filters from Eversports widget');
    }
    
    // Call it immediately if dark mode is enabled
    if (localStorage.getItem('darkMode') === 'enabled') {
        applyDarkModeToEversports();
    }
});