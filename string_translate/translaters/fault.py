from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_fault(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    for method in json_object["mending_methods"]:
        translate_generic(translation, method)
        if "success_msg" in method:
            method["success_msg"] = translate_any(
                translation, method["success_msg"])
