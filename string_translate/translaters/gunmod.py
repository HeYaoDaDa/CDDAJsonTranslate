from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_gunmod(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    if "mode_modifier" in json_object:
        modes = json_object.get("mode_modifier", [])
        for fire_mode in modes:
            fire_mode[1] = translate_any(translation, fire_mode[1])
    if "location" in json_object:
        json_object["location"] = translate_any(
            translation, json_object["location"])
    if "mod_targets" in json_object:
        json_object["mod_targets"] = translate_any(
            translation, json_object["mod_targets"], context="gun_type_type")
