from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_skill_display_type(translation: NullTranslations, json_object):
    json_object["display_string"] = translate_any(
        translation, json_object["display_string"])
