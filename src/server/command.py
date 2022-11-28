import json

from abc import ABC, abstractmethod

import engine


class Command(ABC):
    @abstractmethod
    def complete(self, payload: json) -> json:
        raise NotImplementedError


class GetDocumentsLangsCommand(Command):
    def complete(self, payload: any) -> any:
        documents = json.loads(payload)
        langs = engine.get_documents_langs(*documents)
        return langs