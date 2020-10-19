function ref_btn_clicked (event) {
  console.log('chat settings button clicked');
  event.preventDefault();
  var url = event.target.href;
  console.log(url);
  $.ajax({
    url: url,
    success: function(resp) {
      document.open();
      document.write(resp);
      document.close();
    }
  });
}
