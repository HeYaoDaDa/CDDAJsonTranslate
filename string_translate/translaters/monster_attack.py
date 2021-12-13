from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_monster_attack(translation: NullTranslations, json_object):
    for key in ["hit_dmg_u", "hit_dmg_npc", "no_dmg_msg_u", "no_dmg_msg_npc"]:
        if key in json_object:
            json_object[key] = translate_any(translation, json_object[key])
