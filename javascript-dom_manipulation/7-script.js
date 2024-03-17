fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('There was no response');
        }
        return response.json();
    })
    .then(data => {
        listing_movies(data);
    })
    .catch(error => {
        console.error('There was a problem fetching the data:', error)
    });


function listing_movies(response) {
    const list_selector = document.querySelector('#list_movies');

    response.results.forEach(film_info => {
        const add_item = document.createElement('li');
        add_item.textContent = film_info.title;
        list_selector.appendChild(add_item);
    });
}