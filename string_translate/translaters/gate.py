from gettext import NullTranslations
from ..helper import translate_any


def translate_gate(translation: NullTranslations, json_object):
    messages = json_object.get("messages", {})

    for i in messages:
        messages[i] = translate_any(translation, messages[i])
