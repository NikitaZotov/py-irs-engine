import json

from .command import \
    GetDocumentsLangsCommand, \
    GetDocumentsSummarizationsCommand, \
    GetDocumentsTranslationsCommand, \
    GetDocumentsFrequentWords


class MessageHandler:
    def __init__(self):
        self._commands = {
            "get_langs": GetDocumentsLangsCommand,
            "get_summars": GetDocumentsSummarizationsCommand,
            "get_translations": GetDocumentsTranslationsCommand,
            "get_frequent_words": GetDocumentsFrequentWords,
        }

    def handle(self, message: str) -> str:
        message_obj = json.loads(message)

        id = message_obj["id"]
        type = message_obj["type"]
        payload = message_obj["payload"]

        command = self._commands.get(type)()
        answer = command.complete(payload)
        return json.dumps({"id": id, "payload": answer})
