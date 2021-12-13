from gettext import NullTranslations
from ..helper import translate_any


def translate_effect_type(translation: NullTranslations, json_object):
    if json_object.get("name"):
        json_object["name"] = translate_any(translation, json_object["name"])
    if json_object.get("desc"):
        json_object["desc"] = translate_any(translation, json_object["desc"])

    keys = ["apply_message", "remove_message", "miss_messages", "decay_messages",
            "speed_name", "apply_memorial_log", "remove_memorial_log"]
    for key in keys:
        if json_object.get(key):
            json_object[key] = translate_any(translation, json_object[key])
