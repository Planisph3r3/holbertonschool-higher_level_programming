const sel_header = document.querySelector('header');
const toggle_header = document.querySelector('#toggle_header');


toggle_header.addEventListener("click", function() {
    function change_color() {

        const header_class = sel_header.getAttribute('class')
        if (header_class != "green") {
            sel_header.setAttribute("class", "green");
        } else if (header_class == "green") {
            sel_header.setAttribute("class", "red");
        };

    }
    change_color();
});
