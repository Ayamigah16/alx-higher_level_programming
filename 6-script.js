// Wait for the document to be ready
$(document).ready(function() {
    // Attach a click event handler to the div with id update_header
    $('#update_header').click(function() {
        // Update the text of the header element
        $('header').text('New Header!!!');
    });
});
