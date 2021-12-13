from gettext import NullTranslations
from ..helper import translate_any


def translate_profession(translation: NullTranslations, json_object):
    if type(json_object["name"]) is str:
        profession_name = json_object["name"]
        json_object["name"] = {
            "male": profession_name, "female": profession_name}
    json_object["name"]["male"] = translate_any(
        translation, json_object["name"]["male"], context="profession_male")

    json_object["name"]["female"] = translate_any(
        translation, json_object["name"]["female"], context="profession_male")

    # TODO this should have female's description?
    json_object["description"] = translate_any(
        translation, json_object["description"], context="prof_desc_male")
