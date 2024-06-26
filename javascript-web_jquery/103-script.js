$(document).ready(function () {
    function translateGreet() {
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
    }
    // On click
    $('#btn_translate').click(translateGreet);
  
    //   Keypress ENTER
    $('#language_code').keypress(function (event) {
      if (event.keyCode === 13) {
        translateGreet();
      }
    });
  });