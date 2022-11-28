from websocket_server import WebsocketServer
from src.server.message_handler import MessageHandler


class IrsServer(WebsocketServer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._handler = MessageHandler()
        self._initialize()

    def _initialize(self):
        self.set_fn_message_received(self._build_on_message())

    def _build_on_message(self):
        def _on_message(client, server, message):
            answer = self._handler.handle(message)
            server.send_message(client, answer)

        return _on_message
