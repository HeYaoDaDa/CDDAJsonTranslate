from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_trap(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    if "vehicle_data" in json_object and "sound" in json_object["vehicle_data"]:
        json_object["vehicle_data"]["sound"] = translate_any(
            translation, json_object["vehicle_data"]["sound"])
