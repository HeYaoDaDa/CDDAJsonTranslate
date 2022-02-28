import os
import shutil
import gettext
from .translate import translate_json_dir

def translate_data(data_dirs:list[str],out_dir:str,mo_dir:str,langs:list[str]):
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir, True)
    os.mkdir(out_dir)

    if langs == None:
        langs = os.listdir(mo_dir)

    print("Start translate.\ndata_dirs is {}.\nmo_dir is {}.\nout_dir is {}.\nneed process lang have {}"
        .format(data_dirs, mo_dir, out_dir, langs))
    for lang in langs:
        print("\n\t----- process {} -----".format(lang))
        translater = gettext.translation(
            "cataclysm-dda", localedir=mo_dir, languages=[lang])
        for data_dir in data_dirs:
            translate_json_dir(
                translater, data_dir, os.path.join(out_dir, lang)
            )
        print("\t----- process {} end -----".format(lang))