from gettext import NullTranslations
from .effect import translate_effect


def translate_effect_on_condition(translation: NullTranslations, json_object):
    translate_effect(translation, json_object["effect"])
    if "false_effect" in json_object:
        translate_effect(translation, json_object["false_effect"])
