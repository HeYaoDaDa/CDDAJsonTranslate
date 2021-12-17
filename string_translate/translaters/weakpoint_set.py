from gettext import NullTranslations
from ..helper import translate_any


def translate_weakpoint_set(translation: NullTranslations, json_object):
    if "weakpoints" in json_object:
        for wp in json_object["weakpoints"]:
            id = ""
            if "id" in wp:
                id = wp["id"]
            if "name" in wp:
                wp["name"] = translate_any(translation, wp["name"])
            if "effects" in wp:
                for fx in wp["effects"]:
                    if "message" in fx:
                        fx["message"] = translate_any(
                            translation, fx["message"])
