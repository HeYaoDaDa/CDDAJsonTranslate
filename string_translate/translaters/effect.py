from gettext import NullTranslations
from ..helper import translate_any


def translate_effect(translation: NullTranslations, json_object):
    if type(json_object) != list:
        json_object = [json_object]
    for effect in json_object:
        if type(effect) == dict:
            if "u_buy_monster" in effect and "name" in effect:
                effect["name"] = translate_any(translation, effect["name"])
            if "message" in effect:
                effect["message"] = translate_any(
                    translation, effect["message"])
            if "u_message" in effect:
                if "snippet" in effect and effect["snippet"] is True:
                    continue
                effect["u_message"] = translate_any(
                    translation, effect["u_message"])
