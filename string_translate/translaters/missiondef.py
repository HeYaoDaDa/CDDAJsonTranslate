from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic
from .effect import translate_effect


def translate_missiondef(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    if "dialogue" in json_object:
        for key in ["describe", "offer", "accepted", "rejected", "advice",
                    "inquire", "success", "success_lie", "failure"]:
            if key in json_object["dialogue"]:
                json_object["dialogue"][key] = translate_any(
                    translation, json_object["dialogue"][key])

    for key in ["start", "end", "fail"]:
        if key in json_object and "effect" in json_object[key]:
            translate_effect(translation, json_object[key]["effect"])
