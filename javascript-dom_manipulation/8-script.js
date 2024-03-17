document.addEventListener("DOMContentLoaded", function() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(response => {
            if (!response.ok) {
                throw new Error('There was no response');
            }
            return response.json();
        })
        .then(data => {
            say_hello(data);
        })
        .catch(error => {
            console.error('There was a problem fetching the data:', error);
        });
});

function say_hello(response) {
        const hello_selector = document.querySelector('#hello');
        hello_selector.textContent = response.hello;
    }