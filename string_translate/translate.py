from gettext import NullTranslations, translation
import os
import json

from string_translate.translaters import profession
from .translater import ignorable, automatically_convertible, extract_specials
from .translaters.generic import translate_generic


def translate_json_object(translation: NullTranslations, json_object: dict):
    if "type" in json_object and type(json_object["type"]) is str:
        json_type = json_object["type"].lower()
        if json_type in ignorable:
            pass
        elif json_type in automatically_convertible:
            try:
                translate_generic(translation, json_object)
            except Exception as E:
                print("Exception when parsing JSON data type \"{}\"\njson is {}"
                      .format(json_type, json_object))
                raise E
        elif json_type in extract_specials:
            try:
                extract_specials[json_type](translation, json_object)
            except Exception as E:
                print("Exception when parsing JSON data type \"{}\"\njson is {}"
                      .format(json_type, json_object))
                raise E
        else:
            raise Exception("Unrecognized JSON data type \"{}\""
                            .format(json_type))


def translate_json_file(translation: NullTranslations, file_path: str, out_file_path: str):
    with open(file_path, encoding="utf-8") as fp:
        json_data = json.load(fp)
    try:
        json_objects = json_data if type(json_data) is list else [json_data]
        for json_object in json_objects:
            translate_json_object(translation, json_object)
        if not os.path.exists(os.path.dirname(out_file_path)):
            os.makedirs(os.path.dirname(out_file_path))
        json.dump(json_objects, open(out_file_path, mode="w",
                  encoding="utf-8"), ensure_ascii=False, indent=2)
    except Exception as E:
        print("Error in JSON file: '{0}'".format(file_path))
        raise E


def translate_json_dir(translation: NullTranslations, dir_path: str, out_path: str):
    allfiles = sorted(os.listdir(dir_path))
    dirs = []
    for file in allfiles:
        full_file = os.path.join(dir_path, file)
        full_translate_file = os.path.join(out_path, file)
        if os.path.isdir(full_file):
            dirs.append((full_file, full_translate_file))
        elif file.endswith(".json"):
            translate_json_file(
                translation, full_file, full_translate_file
            )
        else:
            print("Skipping file: '{}'".format(file))
    for dir_path, out_path in dirs:
        translate_json_dir(
            translation, dir_path, out_path
        )
