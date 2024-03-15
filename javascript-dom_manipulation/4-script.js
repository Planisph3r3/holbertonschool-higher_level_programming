const sel_id = document.querySelector('#add_item');


sel_id.addEventListener("click", function() {
    function add_item() {

        const sel_list = document.querySelector('ul.my_list');
        const list_mem = document.createElement('li');
        sel_list.appendChild(list_mem);
    }
    add_item();
});
