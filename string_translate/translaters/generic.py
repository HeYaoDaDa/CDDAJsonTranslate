from gettext import NullTranslations
from ..helper import translate_any
from .use_action import translate_use_action


def translate_generic(translation: NullTranslations, json_object):
    if "name" in json_object:
        json_object["name"] = translate_any(translation, json_object["name"])

    if "description" in json_object:
        json_object["description"] = translate_any(
            translation, json_object["description"])

    if "name_suffix" in json_object:
        json_object["name_suffix"] = translate_any(
            translation, json_object["name_suffix"])

    if "name_unique" in json_object:
        json_object["name_unique"] = translate_any(
            translation, json_object["name_unique"])

    if "job_description" in json_object:
        json_object["job_description"] = translate_any(
            translation, json_object["job_description"])

    if "use_action" in json_object:
        translate_use_action(translation, json_object["use_action"])

    if "conditional_names" in json_object:
        for cname in json_object.get("conditional_names", []):
            cname["name"] = translate_any(translation, cname["name"])

    if "death_function" in json_object:  # monster
        if "message" in json_object["death_function"]:
            json_object["death_function"]["message"] = translate_any(
                translation, json_object["death_function"]["message"])

    if "detailed_definition" in json_object:
        json_object["detailed_definition"] = translate_any(
            translation, json_object["detailed_definition"])

    if "sound" in json_object:
        json_object["sound"] = translate_any(
            translation, json_object["sound"])

    if "sound_description" in json_object:
        json_object["sound_description"] = translate_any(
            translation, json_object["sound_description"])

    if "snippet_category" in json_object and type(json_object["snippet_category"]) is list:
        # snippet_category is either a simple string (the category ident)
        # which is not translated, or an array of snippet texts.
        for index, entry in enumerate(json_object["snippet_category"]):
            # Each entry is a json-object with an id and text
            if type(entry) is dict:
                entry["text"] = translate_any(translation, entry["text"])
            else:
                # or a simple string
                json_object["snippet_category"][index] = translate_any(
                    translation, entry)

    if "bash" in json_object and type(json_object["bash"]) is dict:
        # entries of type technique have a bash member, too.
        # but it's a int, not an object.
        bash = json_object["bash"]
        if "sound" in bash:
            bash["sound"] = translate_any(translation, bash["sound"])
        if "sound_fail" in bash:
            bash["sound_fail"] = translate_any(translation, bash["sound_fail"])

    if "boltcut" in json_object:
        boltcut = json_object["boltcut"]
        if "sound" in boltcut:
            boltcut["sound"] = translate_any(translation, boltcut["sound"])

        if "message" in boltcut:
            boltcut["message"] = translate_any(translation, boltcut["message"])

    if "seed_data" in json_object:
        seed_data = json_object["seed_data"]
        seed_data["plant_name"] = translate_any(
            translation, seed_data["plant_name"])

    if "relic_data" in json_object and "name" in json_object["relic_data"]:
        json_object["relic_data"]["name"] = translate_any(
            translation, json_object["relic_data"]["name"])

    if "text" in json_object:
        json_object["text"] = translate_any(
            translation, json_object["text"])

    if "message" in json_object:
        json_object["message"] = translate_any(
            translation, json_object["message"])

    if "messages" in json_object:
        json_object["messages"] = translate_any(
            translation, json_object["messages"])

    if "valid_mod_locations" in json_object:
        for mod_loc in json_object["valid_mod_locations"]:
            mod_loc[0] = translate_any(translation, mod_loc[0])

    if "info" in json_object:
        json_object["info"] = translate_any(translation, json_object["info"])

    if "restriction" in json_object:
        json_object["restriction"] = translate_any(
            translation, json_object["restriction"])

    if "verb" in json_object:
        json_object["verb"] = translate_any(
            translation, json_object["verb"])

    if "special_attacks" in json_object:
        special_attacks = json_object["special_attacks"]
        for special_attack in special_attacks:
            if "description" in special_attack:
                special_attack["description"] = translate_any(
                    translation, special_attack["description"])

            if "monster_message" in special_attack:
                special_attack["monster_message"] = translate_any(
                    translation, special_attack["monster_message"])

            if "targeting_sound" in special_attack:
                special_attack["targeting_sound"] = translate_any(
                    translation, special_attack["targeting_sound"])

            if "no_ammo_sound" in special_attack:
                special_attack["no_ammo_sound"] = translate_any(
                    translation, special_attack["no_ammo_sound"])

    if "footsteps" in json_object:
        json_object["footsteps"] = translate_any(
            translation, json_object["footsteps"])

    if "revert_msg" in json_object:
        json_object["revert_msg"] = translate_any(
            translation, json_object["revert_msg"])
