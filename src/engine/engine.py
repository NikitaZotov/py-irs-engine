from typing import List

import cld3 as nlp

from transformers import pipeline

from googletrans import Translator

summarizer = pipeline("summarization")
translator = Translator()

_lang_keys = {
    "en": "English",
    "fr": "French",
    "it": "Italian",
}

_key_langs = {
    "English": "en",
    "French": "fr",
    "Italian": "it",
    "Germany": "de",
}


def get_documents_langs(*documents: str) -> List[str]:
    langs = []
    for document in documents:
        lang = _lang_keys.get(nlp.get_language(document).language)
        langs.append(lang)

    return langs


def get_documents_summarizations(*documents: str) -> List[str]:
    summarizations = []

    for document in documents:
        summar = summarizer(document, min_length=75, max_length=300)
        summarizations.append(summar[0]["summary_text"])

    return summarizations


def get_documents_translations(documents: str, language: str) -> List[str]:
    translations = []

    for document in documents:
        trans = translator.translate(text=document, dest=_key_langs[language])
        translations.append(trans.text)

    return translations
