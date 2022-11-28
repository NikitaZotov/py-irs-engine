from typing import List

import cld3 as nlp


def get_documents_langs(*documents: str) -> List[str]:
    langs = []
    for document in documents:
        langs.append(nlp.get_language(document))

    return langs
