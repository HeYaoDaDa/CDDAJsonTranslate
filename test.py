from gettext import translation
from string_translate.translate import translate_json_object
if __name__ == "__main__":
    translater = translation(
        "cataclysm-dda", localedir="lang/mo/", languages=["zh_CN"])
    json_object = {"type": "tool", "name": "3D printer"}
    translate_json_object(translater, json_object)
    print(json_object)
