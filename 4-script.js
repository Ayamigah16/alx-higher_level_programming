// Wait for the document to be ready
$(document).ready(function() {
    // Attach a click event handler to the div with id red_header
    $('#red_header').click(function() {
        // Add the class 'red' to the header element
        $('header').addClass('red');
    });
});
