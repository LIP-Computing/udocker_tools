#!/usr/bin/env python3

# -*- encoding: utf-8 -*-
#
# Copyright 2021-2023 LIP
#
# Author: Mario David <mariojmdavid@gmail.com>
#

"""Produces a json file metadata.json with information of all modules"""

import json
import csv
import pprint

def create_jsonmodule():
    mod_json = {"uid": None,
                "module": None,
                "fname": None,
                "version": None,
                "arch": None,
                "os": None,
                "os_ver": None,
                "kernel_ver": None,
                "sha256sum": None,
                "urls": list(),
                "docs_url": list()}
    return mod_json

if __name__ == '__main__':
    fjson = "../metadata.json"
    fcsv = "../flist-keep.csv"
    all_mod = list()
    url_dirs = ["https://download.ncg.ingrid.pt/webdav/udocker/engines/tarballs/",
               "https://github.com/LIP-Computing/udocker_tools/raw/main/tarballs/"]

    with open(fcsv, 'r') as csvin:
        csv_reader = csv.DictReader(csvin, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1

            mod_json = create_jsonmodule()
            for key in row:
                mod_json[key] = row[key]

            for urldir in url_dirs:
                mod_json["urls"].append(urldir + row["fname"])

            line_count += 1
            all_mod.append(mod_json)

    with open(fjson, 'w') as jdump:
        json.dump(all_mod, jdump, indent=4)

    pprint.pprint(all_mod)
