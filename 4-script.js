// Wait for the document to be ready
$(document).ready(function() {
    // Attach a click event handler to the div with id toggle_header
    $('#toggle_header').click(function() {
        // Toggle the class 'red' on the header element
        $('header').toggleClass('red');
        // Toggle the class 'green' on the header element
        $('header').toggleClass('green');
    });
});
