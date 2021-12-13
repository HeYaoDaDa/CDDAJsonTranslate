from gettext import NullTranslations
from ..helper import translate_any


def translate_recipe_group(translation: NullTranslations, json_object):
    if "recipes" in json_object:
        for recipe in json_object["recipes"]:
            recipe["description"] = translate_any(
                translation, recipe["description"])
