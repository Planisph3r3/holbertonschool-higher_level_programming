$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .done(function (data) {
    $('div#hello').text(data.hello);
  })
  .fail(function () {
    console.log('There was an error');
  });