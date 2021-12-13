from gettext import NullTranslations
from ..helper import translate_any

use_action_msg_keys = [
    "activate_msg",
    "activation_message",
    "auto_extinguish_message",
    "bury_question",
    "charges_extinguish_message",
    "deactive_msg",
    "descriptions",
    "done_message",
    "failure_message",
    "friendly_msg",
    "gerund",
    "holster_msg",
    "holster_prompt",
    "hostile_msg",
    "lacks_fuel_message",
    "menu_text",
    "message",
    "msg",
    "need_charges_msg",
    "need_fire_msg",
    "no_deactivate_msg",
    "noise_message",
    "non_interactive_msg",
    "not_ready_msg",
    "out_of_power_msg",
    "sound_msg",
    "success_message",
    "unfold_msg",
    "use_message",
    "verb",
    "voluntary_extinguish_message",
    "water_extinguish_message",
]


def translate_use_action(translation: NullTranslations, json_object):
    if type(json_object) is dict:
        for msg_key in use_action_msg_keys:
            if msg_key in json_object:
                json_object[msg_key] = translate_any(
                    translation, json_object[msg_key])
        for json_key in json_object:
            translate_use_action(json_object[json_key], translation)
    elif type(json_object) is list:
        for use_action in json_object:
            translate_use_action(use_action, translation)
