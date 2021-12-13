from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_sub_bodypart(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    if "name_multiple" in json_object:
        json_object["name_multiple"] = translate_any(
            translation, json_object["name_multiple"])