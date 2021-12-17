from gettext import NullTranslations
from ..helper import translate_any


def translate_recipe_category(translation: NullTranslations, json_object):
    cid = json_object["id"]
    if cid == 'CC_NONCRAFT':
        return
    cat_name = cid.split("_")[1]
    json_object["name"] = translate_any(translation, cat_name)

    for index, subcat in enumerate(json_object.get("recipe_subcategories", [])):
        name = subcat
        if subcat == 'CSC_ALL':
            name = translate_any(translation, "ALL")
        else:
            subcat_name = subcat.split('_')[2]
            name = translate_any(translation, subcat_name)
        json_object["recipe_subcategories"][index] = {
            "id": subcat,
            "name": name
        }
