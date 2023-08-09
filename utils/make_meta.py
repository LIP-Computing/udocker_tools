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
import os
import glob
import hashlib


ALL_MODULES = []
URL_DIRS = ['https://download.ncg.ingrid.pt/webdav/udocker/engines/tarballs/',
            'https://github.com/LIP-Computing/udocker_tools/raw/main/tarballs/']
URL_DOCS = ['https://download.ncg.ingrid.pt/webdav/udocker/engines/doc/',
            'https://github.com/LIP-Computing/udocker_tools/raw/main/docs/']


def create_jsonmodule():
    '''Create json structure for a module'''
    mod_json = {'uid': None,
                'module': None,
                'tarball': None,
                'version': None,
                'arch': None,
                'os': None,
                'os_ver': None,
                'kernel_ver': None,
                'sha256sum': None,
                'installdir': None,
                'fname': None,
                'docs': None,
                'urls': [],
                'dependencies': [],
                'docs_url': []}
    return mod_json


def init_all_mods(fcsv):
    '''Initialize the list of all modules'''
    with open(fcsv, 'r', encoding='utf-8') as csvin:
        csv_reader = csv.DictReader(csvin, delimiter=',')
        for row in csv_reader:
            mod_json = create_jsonmodule()
            for key in row:
                mod_json[key] = row[key]

            for urldir in URL_DIRS:
                mod_json['urls'].append(urldir + row['tarball'])

            for urldoc in URL_DOCS:
                mod_json['docs_url'].append(urldoc + row['docs'])

            if mod_json['module'] == 'libfakechroot':
                depend = 'patchelf-' + mod_json['arch'] + '.tgz'
                mod_json['dependencies'].append(depend)

            ALL_MODULES.append(mod_json)


# def get_ref_fkchroot():
#     '''Get libfakechroot reference module'''
#     ref_mod = {}
#     for mod in ALL_MODULES:
#         if mod['module'] == 'libfakechroot':
#             ref_mod = mod

#     return ref_mod


# def get_libfchroot(tar_dir, ref_module_fkchroot):
#     '''Get the list of all libfakechroot for all OSs and Versions'''
#     list_libs = [os.path.basename(x) for x in glob.glob(tar_dir + 'libfakechroot-*.so.tgz')]
#     list_lib_modules = []
#     for lib_fkchr in list_libs:
#         mod_json = create_jsonmodule()
#         mod_json['tarball'] = lib_fkchr
#         mod_json['arch'] = ref_module_fkchroot['arch']
#         mod_json['module'] = ref_module_fkchroot['module']
#         mod_json['version'] = ref_module_fkchroot['version']
#         mod_json['docs'] = ref_module_fkchroot['docs']
#         mod_json['dependencies'].append('patchelf-x86_64.tgz')

#         opsys_ver = lib_fkchr.removesuffix('-x86_64.so.tgz').removeprefix('libfakechroot-')
#         if '-' in opsys_ver:
#             (opsys, os_ver) = opsys_ver.split('-')
#             mod_json['os'] = opsys
#             mod_json['os_ver'] = os_ver
#         else:
#             mod_json['os'] = opsys_ver

#         for urldir in URL_DIRS:
#             mod_json['urls'].append(urldir + lib_fkchr)

#         for urldoc in URL_DOCS:
#             mod_json['docs_url'].append(urldoc + ref_module_fkchroot['docs'])

#         list_lib_modules.append(mod_json)

#     return list_lib_modules


def get_sha256(tar_dir):
    '''Calculate the sha256sum of all tarballs of the tools and libraries'''
    nuid = 1
    for mod in ALL_MODULES:
        tarball = tar_dir + mod['tarball']
        with open(tarball, 'rb') as f:
            fread_bytes = f.read()      # read entire file as bytes
            readable_hash = hashlib.sha256(fread_bytes).hexdigest()
            mod['sha256sum'] = readable_hash
            mod['uid'] = nuid
            nuid += 1


if __name__ == '__main__':
    rel_tar_dir = '../tarballs/'
    fjson = '../data/metadata.json'
    file_csv = '../data/module-keep.csv'
    init_all_mods(file_csv)
    # ref_mod_fkchroot = get_ref_fkchroot()
    # libs_fkchroot = get_libfchroot(rel_tar_dir, ref_mod_fkchroot)
    # ALL_MODULES += libs_fkchroot
    get_sha256(rel_tar_dir)
    pprint.pprint(ALL_MODULES)
    with open(fjson, 'w', encoding='utf-8') as jdump:
        json.dump(ALL_MODULES, jdump, indent=4)
