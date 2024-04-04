// Wait for the document to be ready
$(document).ready(function() {
    // Make an AJAX request to fetch the movies data
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function(response) {
            // Iterate over each movie in the response
            $.each(response.results, function(index, movie) {
                // Create a new list item with the movie title
                var listItem = $('<li>').text(movie.title);
                // Append the new list item to the ul with id list_movies
                $('#list_movies').append(listItem);
            });
        },
        error: function() {
            // Handle errors if any
            $('#list_movies').append($('<li>').text('Error fetching movies data'));
        }
    });
});
