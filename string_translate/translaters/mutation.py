from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_mutation(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    if "attacks" in json_object:
        attacks = json_object["attacks"]
        if type(attacks) is dict:
            attacks = [attacks]
        for attack in attacks:
            if "attack_text_u" in attack:
                attack["attack_text_u"] = translate_any(
                    translation, attack["attack_text_u"])
            if "attack_text_npc" in attack:
                attack["attack_text_npc"] = translate_any(
                    translation, attack["attack_text_npc"])

    if "ranged_mutation" in json_object:
        if "message" in json_object["ranged_mutation"]:
            json_object["ranged_mutation"]["message"] = translate_any(
                translation, json_object["ranged_mutation"]["message"])

    if "spawn_item" in json_object:
        if "message" in json_object["spawn_item"]:
            json_object["spawn_item"]["message"] = translate_any(
                translation, json_object["spawn_item"]["message"])

    if "triggers" in json_object:
        for arr in json_object["triggers"]:
            for trigger in arr:
                if "msg_on" in trigger and "text" in trigger["msg_on"]:
                    trigger["msg_on"]["text"] = translate_any(
                        translation, trigger["msg_on"]["text"])
                if "msg_off" in trigger and "text" in trigger["msg_off"]:
                    trigger["msg_off"]["text"] = translate_any(
                        translation, trigger["msg_off"]["text"])

    if "transform" in json_object:
        json_object["transform"]["msg_transform"] = translate_any(
            translation, json_object["transform"]["msg_transform"])
