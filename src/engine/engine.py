import re
import string
from typing import List, Dict

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


def get_documents_frequent_words(documents: str, language: str) -> List[Dict[str, str]]:
    def _define_frequent_words_and_translations(document: str) -> Dict[str, str]:
        frequent_words_dict = {}
        words = re.sub('[' + string.punctuation + ']', '', document).split()

        for word in words:
            frequent_words_dict[word] = frequent_words_dict.get(word, 0) + 1
        sorted_words = sorted(frequent_words_dict, key=lambda k: frequent_words_dict[k], reverse=True)

        result_dict = {}
        max_length = 50
        for fr_word in sorted_words[:max_length]:
            trans = translator.translate(text=fr_word, dest=_key_langs[language])
            result_dict[fr_word] = trans.text

        return result_dict

    result = []

    for doc in documents:
        result_dict = _define_frequent_words_and_translations(doc)
        result.append(result_dict)

    return result
