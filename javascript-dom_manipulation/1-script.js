const sel_header = document.querySelector('header');
const red_header = document.querySelector('#red_header');
red_header.addEventListener("click", function() {
	function change_color() {
		sel_header.style.color = "#FF0000";
	}
	change_color();
});
