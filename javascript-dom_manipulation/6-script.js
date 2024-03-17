fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('There was no response');
        }
        return response.json();
    })
    .then(data => {
        change_names(data);
    })
    .catch(error => {
        console.error('There was a problem fetching the data:', error)
    });

function change_names(response) {
    const tar_div = document.querySelector('#character');
    tar_div.textContent = response.name;
}