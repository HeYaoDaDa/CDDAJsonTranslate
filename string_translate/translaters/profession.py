from gettext import NullTranslations
from ..helper import translate_any


def translate_profession(translation: NullTranslations, json_object):
    if type(json_object["name"]) is str:
        profession_name = json_object["name"]
        json_object["name"] = {
            "male": profession_name, "female": profession_name
        }
    json_object["name"]["male"] = translate_any(
        translation, json_object["name"]["male"], context="profession_male")

    json_object["name"]["female"] = translate_any(
        translation, json_object["name"]["female"], context="profession_male")

    if type(json_object["description"]) is dict and "str" in json_object["description"]:
        json_object["description"] = json_object["description"]["str"]
    if type(json_object["description"]) is str:
        profession_description = json_object["description"]
        json_object["description"] = {
            "male": profession_description, "female": profession_description
        }
    json_object["description"]["male"] = translate_any(
        translation, json_object["description"]["male"], context="prof_desc_male"
    )

    json_object["description"]["female"] = translate_any(
        translation, json_object["description"]["female"], context="prof_desc_female"
    )
