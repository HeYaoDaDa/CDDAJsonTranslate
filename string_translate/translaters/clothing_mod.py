from gettext import NullTranslations
from ..helper import translate_any


def translate_clothing_mod(translation: NullTranslations, json_object):
    json_object["implement_prompt"] = translate_any(
        translation, json_object["implement_prompt"])

    json_object["destroy_prompt"] = translate_any(
        translation, json_object["destroy_prompt"])
