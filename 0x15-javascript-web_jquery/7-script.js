// Wait for the document to be ready
$(document).ready(function() {
    // Make an AJAX request to fetch the character data
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        success: function(response) {
            // Extract the character name from the response
            var characterName = response.name;
            // Update the content of the div with id character
            $('#character').text(characterName);
        },
        error: function() {
            // Handle errors if any
            $('#character').text('Error fetching character data');
        }
    });
});
