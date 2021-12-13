from gettext import NullTranslations
from ..helper import translate_any


def translate_ter_furn_transform(translation: NullTranslations, json_object):
    if "fail_message" in json_object:
        json_object["fail_message"] = translate_any(
            translation, json_object["fail_message"])
    if "terrain" in json_object:
        for terrain in json_object["terrain"]:
            if "message" in terrain:
                terrain["message"] = translate_any(
                    translation, terrain["message"])
    if "furniture" in json_object:
        for furniture in json_object["furniture"]:
            if "message" in furniture:
                furniture["message"] = translate_any(
                    translation, furniture["message"])
