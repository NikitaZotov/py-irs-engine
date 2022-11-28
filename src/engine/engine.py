from typing import List

import cld3 as nlp


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
