from gettext import NullTranslations
from ..helper import translate_any
from .sub_bodypart import translate_sub_bodypart


def translate_bodypart(translation: NullTranslations, json_object):
    translate_sub_bodypart(translation, json_object)

    json_object["accusative"] = translate_any(
        translation, json_object["accusative"])

    if "accusative_multiple" in json_object:
        json_object["accusative_multiple"] = translate_any(
            translation, json_object["accusative_multiple"])

    json_object["encumbrance_text"] = translate_any(
        translation, json_object["encumbrance_text"])

    json_object["heading"] = translate_any(translation, json_object["heading"])

    json_object["heading_multiple"] = translate_any(
        translation, json_object["heading_multiple"])

    if "smash_message" in json_object:
        json_object["smash_message"] = translate_any(
            translation, json_object["smash_message"])

    if "hp_bar_ui_text" in json_object:
        json_object["hp_bar_ui_text"] = translate_any(
            translation, json_object["hp_bar_ui_text"])
