document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("home-button").addEventListener("click", function(event) {
        event.preventDefault(); // Prevent the default action for a moment
        this.classList.add("clicked"); // Add the "clicked" class to trigger the animation

        // Wait for the animation to finish before redirecting
        setTimeout(function() {
            window.location.href = "{% url 'home' %}"; // Redirect to the home page
        }, 3000); // Time should match the animation duration (3s)
    });
});