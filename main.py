#!/usr/bin/env python3

import os
import shutil
import gettext
from argparse import ArgumentParser
from string_translate.translate import translate_json_dir

parser = ArgumentParser("CDDA json translater", "Translate CDDA data/ json file",
                        description="specify game data path, output path and mo path")
parser.add_argument("-i", "--info", dest="info",
                    action="store_true", help="is show debug info")
parser.add_argument("-d", "--data_dir", dest="data_dir",
                    help="game data/ path", type=str, nargs="*")
parser.add_argument("-o", "--out_dir", dest="out_dir",
                    help="translated json file output path", type=str)
parser.add_argument("-l", "--lang", dest="langs",
                    help="translate language list", type=str, nargs="*")
parser.add_argument("-m", "--mo_dir", dest="mo_dir",
                    help="mo file dir path", type=str)
args = parser.parse_args()

if not args.data_dir:
    print("Have to specify game data/ path")
    exit(1)
for data_dir in args.data_dir:
    if not os.path.exists(data_dir):
        print("{} is not exist".format(data_dir))
        exit(1)
    elif not os.path.isdir(data_dir):
        print("{} is not dir".format(data_dir))
        exit(1)

if not args.out_dir:
    print("Have to specify translated json file output path")
    exit(1)

if not args.mo_dir:
    print("Have to specify mo file dir path")
    exit(1)
elif not os.path.exists(args.mo_dir):
    print("{} is not exist".format(args.mo_dir))
    exit(1)
elif not os.path.isdir(args.mo_dir):
    print("{} is not dir".format(args.mo_dir))
    exit(1)


if os.path.exists(args.out_dir):
    shutil.rmtree(args.out_dir, True)
os.mkdir(args.out_dir)

if args.langs == None:
    args.langs = os.listdir(args.mo_dir)

print("Start translate.\ndata_dir is {}.\nmo_dir is {}.\nout_dir is {}.\nneed process lang have {}"
      .format(args.data_dir, args.mo_dir, args.out_dir, args.langs))
for lang in args.langs:
    print("\n\t----- process {} -----".format(lang))
    translater = gettext.translation(
        "cataclysm-dda", localedir=args.mo_dir, languages=[lang])
    for data_dir in args.data_dir:
        translate_json_dir(
            translater, data_dir, os.path.join(args.out_dir, lang)
        )
    print("\t----- process {} end -----".format(lang))
