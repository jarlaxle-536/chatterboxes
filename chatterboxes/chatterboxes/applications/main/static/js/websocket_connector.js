console.log(window.location.host);
console.log('ws://' + window.location.host + '/chat/');
var socket = new WebSocket('ws://' + window.location.host + '/chat/');
var msg_template_obj = $('#message_template_card').clone();

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
  var template = msg_template_obj;
  template.removeAttr('hidden');
  template.removeAttr('id');
  var for_text = template.find('#message_template_card_body');
  for_text.text(data['text']);
  for_text.removeAttr('id');
  return template[0].outerHTML;
};
