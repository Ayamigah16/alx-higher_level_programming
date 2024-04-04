$(document).ready(function() {
    // Add item to the list
    $('#add_item').click(function() {
        // Create a new list item element
        var newItem = $('<li>').text('Item');
        // Append the new item to the UL element with class my_list
        $('ul.my_list').append(newItem);
    });

    // Remove last item from the list
    $('#remove_item').click(function() {
        // Select the last item in the list and remove it
        $('ul.my_list li:last-child').remove();
    });

    // Clear the entire list
    $('#clear_list').click(function() {
        // Remove all items from the UL element with class my_list
        $('ul.my_list').empty();
    });
});
