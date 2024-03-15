const sel_id = document.querySelector('#update_header');


sel_id.addEventListener("click", function() {
    function change_text() {

        const sel_header = document.querySelector('header');
        sel_header.textContent = "New Header!!!";
    }
    change_text();
});
