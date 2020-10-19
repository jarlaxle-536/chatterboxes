function chat_settings_btn_clicked (event) {
  console.log('chat settings button clicked');
  event.preventDefault();
  var url = $(this).href;
  console.log(url);
  $.ajax({
    url: url,
    success: function(resp) {
      console.log(resp);
    }
  });
}
