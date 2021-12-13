from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_achievement(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    for requirement in json_object.get("requirements", ()):
        if "description" in requirement:
            requirement["description"] = translate_any(
                translation, requirement["description"])
