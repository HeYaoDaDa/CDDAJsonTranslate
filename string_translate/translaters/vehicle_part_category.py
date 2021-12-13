from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_vehicle_part_category(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    json_object["short_name"] = translate_any(
        translation, json_object["short_name"])
