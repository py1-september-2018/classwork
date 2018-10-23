$(document).ready(function() {
  $('#user-search-form').submit(function(e) {
    e.preventDefault();
    $.ajax({
      url: $('#user-search-form').attr('action'),
      method: 'post',
      data: {
        csrfmiddlewaretoken: $('#user-search-form input[name="csrfmiddlewaretoken"]').val(),
        searchString: $('#user-search-input').val()
      },
      success: function(data) {
        console.log(data);
        htmlStr = "";
        for(var i = 0; i < data.length; i++) {
          htmlStr += `<div class='user'>${data[i].fields.first_name} ${data[i].fields.last_name}</div>`
          console.log(data[i].fields.first_name, data[i].fields.last_name);
          $('.found-users').html(htmlStr);
        }
      },
      error: function(error) {
        console.log('THERE WAS AN ERROR');
      }
    });
  });
});