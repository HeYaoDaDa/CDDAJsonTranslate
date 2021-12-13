from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_material(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)

    if "bash_dmg_verb" in json_object:
        json_object["bash_dmg_verb"] = translate_any(
            translation, json_object["bash_dmg_verb"])

    if "cut_dmg_verb" in json_object:
        json_object["cut_dmg_verb"] = translate_any(
            translation, json_object["cut_dmg_verb"])

    if "dmg_adj" in json_object:
        for i in range(4):
            json_object["dmg_adj"][i] = translate_any(
                translation, json_object["dmg_adj"][i])
