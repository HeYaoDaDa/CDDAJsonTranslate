from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_movement_mode(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)

    json_object["character"] = translate_any(
        translation, json_object["character"])

    json_object["panel_char"] = translate_any(
        translation, json_object["panel_char"])

    json_object["change_good_none"] = translate_any(
        translation, json_object["change_good_none"])

    json_object["change_good_animal"] = translate_any(
        translation, json_object["change_good_animal"])

    json_object["change_good_mech"] = translate_any(
        translation, json_object["change_good_mech"])

    if "change_bad_none" in json_object:
        json_object["change_bad_none"] = translate_any(
            translation, json_object["change_bad_none"])

    if "change_bad_animal" in json_object:
        json_object["change_bad_animal"] = translate_any(
            translation, json_object["change_bad_animal"])

    if "change_bad_mech" in json_object:
        json_object["change_bad_mech"] = translate_any(
            translation, json_object["change_bad_mech"])
