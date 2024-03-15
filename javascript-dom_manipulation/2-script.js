const sel_header = document.querySelector('header');
const red_header = document.querySelector('#red_header');
red_header.addEventListener("click", function() {
	function change_color() {
		sel_header.setAttribute("class", "red");
	}
	change_color();
});
