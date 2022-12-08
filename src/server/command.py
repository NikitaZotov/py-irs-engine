import json

from abc import ABC, abstractmethod

import engine


class Command(ABC):
    @abstractmethod
    def complete(self, payload: json) -> json:
        raise NotImplementedError


class GetDocumentsLangsCommand(Command):
    def complete(self, payload: any) -> any:
        langs = engine.get_documents_langs(*payload)
        return langs


class GetDocumentsSummarizationsCommand(Command):
    def complete(self, payload: any) -> any:
        summarizations = engine.get_documents_summarizations(*payload)
        return summarizations


class GetDocumentsTranslationsCommand(Command):
    def complete(self, payload: any) -> any:
        translations = engine.get_documents_translations(payload["documents"], payload["lang"])
        return translations


class GetDocumentsFrequentWords(Command):
    def complete(self, payload: any) -> any:
        translations = engine.get_documents_frequent_words(payload["documents"], payload["lang"])
        return translations
