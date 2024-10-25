var selectAllCheckbox = document.getElementById('select-all');

var checkboxes = document.querySelectorAll('input[type="checkbox"]');

selectAllCheckbox.addEventListener('click', function() {
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = selectAllCheckbox.checked;
    }
});

window.onload = function() {
    // Select all checkboxes on the page
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');

    // If there are exactly two checkboxes, check the second one by default
    if (checkboxes.length === 2) {
        checkboxes[1].checked = true;
    }
};