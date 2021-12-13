from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_speed_description(translation: NullTranslations, json_object):
    for speed in json_object.get("values", []):
        if "descriptions" in speed:
            descriptions = []
            if type(speed["descriptions"]) is list:
                descriptions = speed["descriptions"]
            else:
                descriptions.append(speed["descriptions"])
            for index, desc in enumerate(descriptions):
                descriptions[index] = translate_any(translation, desc)
