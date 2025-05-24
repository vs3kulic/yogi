document.addEventListener('DOMContentLoaded', function() {
    // Function to initialize the questionnaire validation
    function initQuestionnaireValidation() {
        // Select all buttons we care about
        const buttons = document.querySelectorAll('.weiter-btn, button[type="submit"]:not(.btn-primary), button');
        
        // Filter for buttons with text "Weiter" 
        const weiterButtons = Array.from(buttons).filter(btn => 
            btn.textContent.trim().toLowerCase() === "weiter" || 
            btn.value?.toLowerCase() === "weiter"
        );
        
        if (weiterButtons.length > 0) {
            console.log("Found Weiter buttons:", weiterButtons);
            
            weiterButtons.forEach(nextButton => {
                nextButton.addEventListener('click', function(event) {
                    // Check if any option is selected
                    const selectedOption = document.querySelector('.quiz-option.selected, .option.selected, input[type="radio"]:checked');
                    
                    console.log("Selected option:", selectedOption);
                    
                    if (!selectedOption) {
                        console.log("No option selected, showing error");
                        event.preventDefault();
                        
                        // Create error message if it doesn't exist
                        let errorMsg = document.querySelector('.option-error-message');
                        if (!errorMsg) {
                            errorMsg = document.createElement('div');
                            errorMsg.className = 'option-error-message alert alert-danger text-center';
                            errorMsg.innerHTML = '<i class="bi bi-exclamation-triangle-fill me-2"></i>Bitte wähle eine Antwort aus!';
                            errorMsg.style.width = '100%';
                            errorMsg.style.maxWidth = '600px';
                            errorMsg.style.margin = '1rem auto';
                            errorMsg.style.borderRadius = '8px';
                            errorMsg.style.boxShadow = '0 4px 8px rgba(220, 53, 69, 0.15)';
                            
                            // Find the form or container
                            const form = nextButton.closest('form');
                            const container = nextButton.closest('.container, .row, .col');
                            
                            if (form) {
                                form.insertBefore(errorMsg, form.firstChild);
                            } else if (container) {
                                container.insertBefore(errorMsg, container.firstChild);
                            } else {
                                // Fallback - insert before the button itself
                                nextButton.parentNode.insertBefore(errorMsg, nextButton);
                            }
                        } else {
                            // Make sure the error is visible
                            errorMsg.style.display = 'block';
                        }
                        
                        // Scroll to error message
                        errorMsg.scrollIntoView({ behavior: 'smooth', block: 'center' });
                        
                        // Highlight options
                        const options = document.querySelectorAll('.quiz-option, .option, input[type="radio"] + label');
                        options.forEach(option => {
                            option.style.borderColor = '#dc3545';
                            option.style.boxShadow = '0 0 0 2px rgba(220, 53, 69, 0.25)';
                        });
                    }
                });
            });
        } else {
            console.log("No Weiter buttons found on this page");
        }
        
        // Add selection behavior to options
        setupOptionSelection();
    }
    
    // Function to handle option selection
    function setupOptionSelection() {
        const options = document.querySelectorAll('.quiz-option, .option');
        options.forEach(option => {
            option.addEventListener('click', function() {
                // Remove selected class from all options
                options.forEach(opt => opt.classList.remove('selected'));
                
                // Add selected class to clicked option
                this.classList.add('selected');
                
                // Hide error message if present
                const errorMsg = document.querySelector('.option-error-message');
                if (errorMsg) {
                    errorMsg.style.display = 'none';
                }
            });
        });
        
        // Also handle radio buttons
        const radioInputs = document.querySelectorAll('input[type="radio"]');
        radioInputs.forEach(radio => {
            radio.addEventListener('change', function() {
                // Hide error message if present
                const errorMsg = document.querySelector('.option-error-message');
                if (errorMsg) {
                    errorMsg.style.display = 'none';
                }
                
                // Remove highlighting from labels
                const labels = document.querySelectorAll('input[type="radio"] + label');
                labels.forEach(label => {
                    label.style.borderColor = '';
                    label.style.boxShadow = '';
                });
            });
        });
    }
    
    // Initialize if we're on the questionnaire page
    if (window.location.pathname.includes('questionnaire') || 
        document.querySelector('.quiz-option, .option, input[type="radio"]')) {
        initQuestionnaireValidation();
        console.log("Questionnaire validation initialized");
    }
    
    // For single-page applications, monitor DOM changes
    let lastUrl = location.href; 
    new MutationObserver(() => {
        const url = location.href;
        if (url !== lastUrl) {
            lastUrl = url;
            // Check if new page is a questionnaire
            setTimeout(() => {
                if (window.location.pathname.includes('questionnaire') || 
                    document.querySelector('.quiz-option, .option, input[type="radio"]')) {
                    initQuestionnaireValidation();
                    console.log("Questionnaire validation initialized after navigation");
                }
            }, 500);
        }
    }).observe(document, {subtree: true, childList: true});
});