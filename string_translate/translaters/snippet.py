from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_snippet(translation: NullTranslations, json_object):
    text = json_object["text"]
    if type(text) is not list:
        text = [text]
    for index, snip in enumerate(text):
        if type(snip) is str:
            text[index] = translate_any(translation, snip)
        elif type(snip) is dict:
            snip["text"] = translate_any(translation, snip["text"])
