from gettext import NullTranslations
from ..helper import translate_any
from .generic import translate_generic


def translate_recipe(translation: NullTranslations, json_object):
    translate_generic(translation, json_object)
    if "book_learn" in json_object and type(json_object["book_learn"]) is dict:
        for book in json_object["book_learn"]:
            if "recipe_name" in json_object["book_learn"][book]:
                json_object["book_learn"][book]["recipe_name"] = translate_any(
                    translation, json_object["book_learn"][book]["recipe_name"])

    if "blueprint_name" in json_object:
        json_object["blueprint_name"] = translate_any(
            translation, json_object["blueprint_name"])
