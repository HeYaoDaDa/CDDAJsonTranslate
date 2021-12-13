from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_scenario(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)

    if "start_name" in json_object:
        json_object["start_name"] = translate_any(
            translation, json_object["start_name"])
