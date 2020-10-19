function form_submit (event, success_url) {
  console.log('form submit');
  event.preventDefault();
  var url = event.target.action;
  var query_string = $('#' + event.target.id).serialize();
  console.log(url);
  console.log(query_string);
  $.post({
    url: url,
    data: query_string,
    success: function(resp) {
      document.open();
      document.write(resp);
      document.close();
    }
  });
}
