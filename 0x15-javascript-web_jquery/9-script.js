// Wait for the document to be ready
$(document).ready(function() {
    // Make an AJAX request to fetch the translation
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        success: function(response) {
            // Update the content of the div with id hello
            $('#hello').text(response.hello);
        },
        error: function() {
            // Handle errors if any
            $('#hello').text('Error fetching translation');
        }
    });
});
