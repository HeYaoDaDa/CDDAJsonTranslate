from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_mutation_category(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    for key in ["mutagen_message",
                "iv_message",
                "iv_sleep_message",
                "iv_sound_message",
                "junkie_message"
                ]:
        if key in json_object:
            json_object[key] = translate_any(translation, json_object[key])

    if "memorial_message" in json_object:
        json_object["memorial_message"] = translate_any(
            translation, json_object["memorial_message"], context="memorial_male")
