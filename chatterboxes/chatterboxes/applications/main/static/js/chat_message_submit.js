$('#chat_message_form').on('submit', function (event) {
  submit_message(event);
});

function submit_message (event) {
  console.log('chat message cubmit');
  console.log(event);
  event.preventDefault();
  var url = event.target.action;
  var query_string = $('#' + event.target.id).serialize();
  console.log(url);
  console.log(query_string);
  $.post({
    url: url,
    data: query_string,
    success: function(resp) {
      console.log(resp);
    }
  });
};
