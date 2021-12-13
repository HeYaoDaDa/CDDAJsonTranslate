from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_gun(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    if "variants" in json_object:
        for variant in json_object["variants"]:
            translate_generic(translation, variant)

    if "modes" in json_object:
        for mode in json_object["modes"]:
            mode[1] = translate_any(translation, mode[1])

    if "skill" in json_object:
        if json_object["skill"] != "archery":
            json_object["skill"] = translate_any(
                translation, json_object["skill"])

    if "reload_noise" in json_object:
        json_object["reload_noise"] = translate_any(
            translation, json_object["reload_noise"])

    if "valid_mod_locations" in json_object:
        for loc in json_object["valid_mod_locations"]:
            loc[0] = translate_any(translation, loc[0])
