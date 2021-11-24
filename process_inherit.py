#!/usr/bin/env python3
" Procees CDDA Json inherit "

import json
import os

class CddaJson:
    jsonData = {}
    mod = "dda"
    dependents = []
    id = ""
    jsonType = ""
    def __init__(self, data, mod, dependents):
        self.jsonData = data
        self.mod = mod
        self.dependents = dependents
        self.id = self.findId()
        self.jsonType = data["type"]

    def findId(self):
        if "id" in self.jsonData:
            return self.jsonData["id"]
        elif "abstract" in self.jsonData:
            return self.jsonData["abstract"]
        elif "type" in self.jsonData:
            if "dream" == self.jsonData["type"]:
                return self.jsonData["category"]+str(self.jsonData["strength"])
            elif "monstergroup" == self.jsonData["type"] or "MONSTER_FACTION" == self.jsonData["type"]:
                return self.jsonData["name"]
            elif "profession_item_substitutions" == self.jsonData["type"]:
                print(self.jsonData)
                return self.jsonData["item"]
            elif "recipe" == self.jsonData["type"]:
                item_id = ""
                if "result" not in self.jsonData:
                    if "copy-from" in self.jsonData:
                        item_id = self.jsonData["copy-from"]
                    else:
                        print(self.jsonData)
                else:
                    item_id = self.jsonData["result"]
                if "id_suffix" in self.jsonData:
                    return item_id + self.jsonData["id_suffix"]
                else:
                    return item_id
            elif self.jsonData["type"] in solo_type:
                return self.jsonData["type"]
        print("no find")
        print(self.jsonData)
        raise Exception(self.jsonData)

def process_dir(json_dir, mod, dependents):
    allfiles = os.listdir(json_dir)
    allfiles.sort()
    dirs = []
    for f in allfiles:
        full_name = os.path.join(json_dir, f)
        if os.path.isdir(full_name):
            dirs.append(f)
        elif f in skiplist or full_name in ignore_files:
            continue
        elif any(full_name.startswith(dir) for dir in ignore_directories):
            continue
        elif f.endswith(".json"):
            procees_file(full_name, mod, dependents)
        else:
            print("Skipping file: '{}'".format(f))
        pass
    for f in dirs:
        process_dir(os.path.join(json_dir, f), mod, dependents)

def procees_file(json_file, mod, dependents):
    with open(json_file, encoding="utf-8") as fp:
        jsondata = json.load(fp)
    if hasattr(jsondata, "keys"):
        process_json(jsondata, mod, dependents)
    else:
        for jsonobject in jsondata:
            process_json(jsonobject, mod, dependents)

def process_json(json_data, mod, dependents):
    result = CddaJson(json_data, mod, dependents)
    no_process_json.append(result)

skiplist = ["default_blacklist.json"]
ignore_files = []
ignore_directories = []
solo_type = ["hit_range","obsolete_terrain"]
no_process_json = []
dup_size = 0
dup_type = set()
print("start")
process_dir("data/json","dda",[])
print(len(no_process_json))
for i in range(0,len(no_process_json)):
    for j in range(i+1,len(no_process_json)):
        if no_process_json[i].id == no_process_json[j].id and no_process_json[i].jsonType == no_process_json[j].jsonType:
            dup_size += 1
            dup_type.add(no_process_json[i].jsonType)
            break
print("dup size {}".format(dup_size))
print(dup_type)