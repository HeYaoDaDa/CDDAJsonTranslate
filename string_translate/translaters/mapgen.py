from gettext import NullTranslations
from ..helper import translate_any


def translate_mapgen(translation: NullTranslations, json_object):
    if "object" not in json_object:
        return

    for key in ["place_specials", "place_signs"]:
        if key in json_object["object"]:
            for sign in json_object["object"][key]:
                if "signage" in sign:
                    sign["signage"] = translate_any(
                        translation, sign["signage"])

    if "signs" in json_object["object"]:
        for sign in json_object["object"]["signs"]:
            if "signage" in json_object["object"]["signs"][sign]:
                json_object["object"]["signs"][sign]["signage"] = translate_any(
                    translation, json_object["object"]["signs"][sign]["signage"])

    if "computers" in json_object["object"]:
        for key in json_object["object"]["computers"]:
            com = json_object["object"]["computers"][key]
            if "name" in com:
                com["name"] = translate_any(translation, com["name"])
            for opt in com.get("options", []):
                if "name" in opt:
                    opt["name"] = translate_any(translation, opt["name"])
            if "access_denied" in com:
                com["access_denied"] = translate_any(
                    translation, com["access_denied"])
