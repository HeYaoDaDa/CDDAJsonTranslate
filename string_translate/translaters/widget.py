from gettext import NullTranslations
from ..helper import translate_any


def translate_widget(translation: NullTranslations, json_object):
    if "label" in json_object:
        json_object["label"] = translate_any(translation, json_object["label"])
    if "strings" in json_object:
        json_object["strings"] = translate_any(translation, json_object["strings"])
