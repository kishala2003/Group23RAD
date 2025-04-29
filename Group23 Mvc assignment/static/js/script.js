document.addEventListener('DOMContentLoaded', function() {
    // Header scroll effect
    const header = document.querySelector('header');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
    
    // Auto-dismiss flash messages
    const flashMessages = document.querySelectorAll('.alert');
    
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => {
                message.style.display = 'none';
            }, 500);
        }, 5000);
    });
    
    // Password confirmation validation
    const registerForm = document.querySelector('form[action="/register"]');
    
    if (registerForm) {
        registerForm.addEventListener('submit', function(e) {
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm_password').value;
            
            if (password !== confirmPassword) {
                e.preventDefault();
                alert('Passwords do not match!');
            }
        });
    }
    
    // Content hover effects
    const contentCards = document.querySelectorAll('.content-card');
    
    contentCards.forEach(card => {
        card.addEventListener('mouseover', function() {
            this.style.zIndex = '10';
        });
        
        card.addEventListener('mouseout', function() {
            this.style.zIndex = '1';
        });
    });
    
    // Simulate play button functionality
    const playButtons = document.querySelectorAll('.btn-play');
    
    playButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            alert('Playing content...\nThis is a demo feature.');
        });
    });

    // Add to your JavaScript
   document.addEventListener('DOMContentLoaded', function() {
      const scrollContainers = document.querySelectorAll('.horizontal-scroll');
    
         scrollContainers.forEach(container => {
           // Check if content is wider than container
             if (container.scrollWidth > container.clientWidth) {
                 // Add visual indicator that more content exists
                container.parentElement.classList.add('has-more-content');
            }
        });
    });
});
