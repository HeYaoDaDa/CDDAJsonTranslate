from gettext import NullTranslations
from ..helper import translate_any


def translate_palette(translation: NullTranslations, json_object):
    if "signs" in json_object:
        for x in sorted(json_object["signs"]):
            json_object["signs"][x]["signage"] = translate_any(
                translation, json_object["signs"][x]["signage"])
