// Wait for the document to be ready
$(document).ready(function() {
    // Attach a click event handler to the div with id add_item
    $('#add_item').click(function() {
        // Create a new list item element
        var newItem = $('<li>Item</li>');
        // Append the new item to the UL element with class my_list
        $('ul.my_list').append(newItem);
    });
});
