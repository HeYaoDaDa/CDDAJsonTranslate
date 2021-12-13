from gettext import NullTranslations
from .generic import translate_generic


def translate_magazine(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    if "variants" in json_object:
        for variant in json_object["variants"]:
            translate_generic(translation, variant)
