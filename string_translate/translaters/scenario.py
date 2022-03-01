from gettext import NullTranslations
from ..helper import translate_any


def translate_scenario(translation: NullTranslations, json_object):
    if "name" in json_object:
        if type(json_object["name"]) is str:
            scenario_name = json_object["name"]
            json_object["name"] = {
                "male": scenario_name, "female": scenario_name
            }
        json_object["name"]["male"] = translate_any(
            translation, json_object["name"]["male"], context="scenario_male")

        json_object["name"]["female"] = translate_any(
            translation, json_object["name"]["female"], context="scenario_female")

    if "description" in json_object:
        if type(json_object["description"]) is str:
            scenario_description = json_object["description"]
            json_object["description"] = {
                "male": scenario_description, "female": scenario_description
            }
        json_object["description"]["male"] = translate_any(
            translation, json_object["description"]["male"], context="scen_desc_male"
        )

        json_object["description"]["female"] = translate_any(
            translation, json_object["description"]["female"], context="scen_desc_female"
        )

    if "start_name" in json_object:
        json_object["start_name"] = translate_any(
            translation, json_object["start_name"])
