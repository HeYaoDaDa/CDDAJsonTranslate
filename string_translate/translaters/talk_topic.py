import itertools
from gettext import NullTranslations
from ..helper import translate_any
from .effect import translate_effect


all_genders = ["f", "m", "n"]


def gender_options(subject):
    return [subject + ":" + g for g in all_genders]


dynamic_line_string_keys = [
    # from `simple_string_conds` in `condition.h`
    "u_male", "u_female", "npc_male", "npc_female",
    "has_no_assigned_mission", "has_assigned_mission",
    "has_many_assigned_missions", "has_no_available_mission",
    "has_available_mission", "has_many_available_missions",
    "mission_complete", "mission_incomplete", "mission_has_generic_rewards",
    "npc_available", "npc_following", "npc_friend", "npc_hostile",
    "npc_train_skills", "npc_train_styles",
    "at_safe_space", "is_day", "npc_has_activity", "is_outside", "u_has_camp",
    "u_can_stow_weapon", "npc_can_stow_weapon", "u_has_weapon",
    "npc_has_weapon", "u_driving", "npc_driving",
    "has_pickup_list", "is_by_radio", "has_reason",
    # yes/no strings for complex conditions, 'and' list
    "yes", "no", "and"
]


def parse_dynamic_line(translation: NullTranslations, json_object):
    if type(json_object) is list:
        for index, line in enumerate(json_object):
            if type(line) is str:
                json_object[index] = translate_any(translation, line)
            else:
                parse_dynamic_line(translation, line)

    elif type(json_object) is dict:
        if "gendered_line" in json_object:
            text = json_object["gendered_line"]
            subjects = json_object["relevant_genders"]
            options = [gender_options(subject) for subject in subjects]
            for context_list in itertools.product(*options):
                context = " ".join(context_list)
                json_object["gendered_line"] = translate_any(
                    translation, text, context=context)

        for key in dynamic_line_string_keys:
            if key in json_object:
                parse_dynamic_line(translation, json_object[key])


def parse_response(translation: NullTranslations, json_object):
    if "text" in json_object:
        json_object["text"] = translate_any(translation, json_object["text"])

    if "truefalsetext" in json_object:
        json_object["truefalsetext"]["true"] = translate_any(translation,
                                                             json_object["truefalsetext"]["true"])
        json_object["truefalsetext"]["false"] = translate_any(translation,
                                                              json_object["truefalsetext"]["false"])

    if "success" in json_object:
        parse_response(translation, json_object["success"])

    if "failure" in json_object:
        parse_response(translation, json_object["failure"])

    if "speaker_effect" in json_object:
        speaker_effects = json_object["speaker_effect"]
        if not type(speaker_effects) is list:
            speaker_effects = [speaker_effects]
        for eff in speaker_effects:
            if "effect" in eff:
                translate_effect(translation, eff["effect"])

    if "effect" in json_object:
        translate_effect(translation, json_object["effect"])


def translate_talk_topic(translation: NullTranslations, json_object):
    if "dynamic_line" in json_object:
        if type(json_object["dynamic_line"]) is str:
            json_object["dynamic_line"] = translate_any(
                translation, json_object["dynamic_line"])
        else:
            parse_dynamic_line(translation, json_object["dynamic_line"])

    if "responses" in json_object:
        for response in json_object["responses"]:
            parse_response(translation, response)

    if "repeat_responses" in json_object:
        if type(json_object["repeat_responses"]) is dict:
            if "response" in json_object["repeat_responses"]:
                parse_response(
                    translation, json_object["repeat_responses"]["response"])
        elif type(json_object["repeat_responses"]) is list:
            for response in json_object["repeat_responses"]:
                if "response" in response:
                    parse_response(translation, response["response"])

    if "effect" in json_object:
        translate_effect(translation, json_object["effect"])
