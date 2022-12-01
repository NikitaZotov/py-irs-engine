from typing import List

import cld3 as nlp

from transformers import pipeline

summarizer = pipeline("summarization")

_lang_keys = {
    "en": "English",
    "fr": "French",
    "it": "Italian",
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

