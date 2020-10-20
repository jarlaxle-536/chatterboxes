console.log(window.location.host);
console.log('ws://' + window.location.host + '/chat/');
var socket = new WebSocket('ws://' + window.location.host + '/chat/');

socket.onopen = function open() {
  console.log('WebSockets connection created.');
};

socket.onmessage = function(event) {
  var msg_data = JSON.parse(event.data);
  var msg_html = create_msg_html(msg_data);;
  console.log(msg_html);
  var chat_div = document.getElementById('chat_div');
  chat_div.innerHTML += msg_html;
  chat_div.scrollTop = chat_div.scrollHeight;
};

if (socket.readyState == WebSocket.OPEN) {
  socket.onopen();
};

function create_msg_html (data) {
  console.log(data);
  var template = $('#message_template_card').clone()
  var template_text = template.find('#message_template_card_body');
  template.removeAttr('hidden');
  template.removeAttr('id');
  template_text.text(data['text']);
  template_text.removeAttr('id');
  return template[0].outerHTML;
};
