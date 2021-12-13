from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_field_type(translation: NullTranslations, json_object):
    for fd in json_object.get("intensity_levels", []):
        if "name" in fd:
            fd["name"] = translate_any(translation, fd["name"])
