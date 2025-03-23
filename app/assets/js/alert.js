document.addEventListener('click', function(event) {
    var alertElements = document.querySelectorAll('.alert-dismissible');
    alertElements.forEach(function(alert) {
        if (alert.contains(event.target)) {
            return; 
        }
        alert.classList.remove('show');  
        alert.classList.add('fade');     
    });
});