console.log(window.location.host);
console.log('ws://' + window.location.host + '/chat/');
var socket = new WebSocket('ws://' + window.location.host + '/chat/');

socket.onopen = function open() {
  console.log('WebSockets connection created.');
};

socket.onmessage = function(e) {
  console.log(e);
};

if (socket.readyState == WebSocket.OPEN) {
  socket.onopen();
};
