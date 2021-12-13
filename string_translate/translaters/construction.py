from gettext import NullTranslations
from ..helper import translate_any


def translate_construction(translation: NullTranslations, json_object):
    if "pre_note" in json_object:
        json_object["pre_note"] = translate_any(
            translation, json_object["pre_note"])
