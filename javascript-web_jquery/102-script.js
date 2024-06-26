$(document).ready(function () {
    $('#btn_translate').click(function () {
      const lenguageCode = $('#language_code').val();
  
      if (lenguageCode.length !== 2) {
        alert('Code must be 2 characters long');
      } else {
        $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${lenguageCode}`)
          .done(function (data) {
            $('#hello').text(data.hello);
          })
          .fail(function () {
            alert('There was an error');
          });
      }
    });
  });