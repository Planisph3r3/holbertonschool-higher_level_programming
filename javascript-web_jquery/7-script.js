$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .done(function (data) {
    $('div#character').text(data.name);
  })
  .fail(function () {
    $('div#character').text('Character not found');
    console.log('Error: Cannot acomplish request');
  });