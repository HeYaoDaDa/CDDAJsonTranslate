from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_martial_art(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    if "initiate" in json_object:
        json_object["initiate"] = translate_any(
            translation, json_object["initiate"])
    onhit_buffs = json_object.get("onhit_buffs", list())
    static_buffs = json_object.get("static_buffs", list())
    onmove_buffs = json_object.get("onmove_buffs", list())
    ondodge_buffs = json_object.get("ondodge_buffs", list())
    onattack_buffs = json_object.get("onattack_buffs", list())
    onpause_buffs = json_object.get("onpause_buffs", list())
    onblock_buffs = json_object.get("onblock_buffs", list())
    ongethit_buffs = json_object.get("ongethit_buffs", list())
    onmiss_buffs = json_object.get("onmiss_buffs", list())
    oncrit_buffs = json_object.get("oncrit_buffs", list())
    onkill_buffs = json_object.get("onkill_buffs", list())

    buffs = (onhit_buffs + static_buffs + onmove_buffs + ondodge_buffs +
             onattack_buffs + onpause_buffs + onblock_buffs + ongethit_buffs +
             onmiss_buffs + oncrit_buffs + onkill_buffs)
    for buff in buffs:
        translate_generic(translation, buff)
