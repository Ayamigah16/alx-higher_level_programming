$(document).ready(function() {
    // Function to fetch and display translation
    function fetchTranslation() {
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
    }

    // Attach a click event handler to the button with id btn_translate
    $('#btn_translate').click(fetchTranslation);

    // Attach a keypress event handler to the input with id language_code
    $('#language_code').keypress(function(event) {
        // Check if the pressed key is Enter (key code 13)
        if (event.keyCode === 13) {
            // Fetch and display translation when Enter key is pressed
            fetchTranslation();
        }
    });
});
