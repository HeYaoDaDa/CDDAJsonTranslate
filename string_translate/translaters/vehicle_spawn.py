from gettext import NullTranslations
from ..helper import translate_any


def translate_vehicle_spawn(translation: NullTranslations, json_object):
    for st in json_object.get("spawn_types"):
        if "description" in st:
            st["description"] = translate_any(translation, st["description"])
