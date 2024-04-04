$(document).ready(function() {
    // Attach a click event handler to the button with id btn_translate
    $('#btn_translate').click(function() {
        // Get the language code entered by the user
        var languageCode = $('#language_code').val();
        
        // Make an AJAX request to fetch the translation
        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            data: { lang: languageCode },
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
});
