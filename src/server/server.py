from websocket_server import WebsocketServer
from .message_handler import MessageHandler


class IrsServer(WebsocketServer):
    def __call__(self, *args, **kwargs):
        super.__call__(*args, *kwargs)
        self._handler = MessageHandler()
        self._initialize()

    def _initialize(self):
        self.set_fn_message_received(self._on_message)

    def _on_message(self, client, message):
        answer = self._handler.handle(message)
        self.send_message(client, answer)
