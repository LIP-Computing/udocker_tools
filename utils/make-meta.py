#!/usr/bin/env python3

# -*- encoding: utf-8 -*-
#
# Copyright 2021 LIP
#
# Author: Mario David <mariojmdavid@gmail.com>
#

"""Produces a json file metadata.json with information of all modules"""

import os
import json
import csv

if __name__ == '__main__':
    fjson = "../metadata.json"
    fcsv = "../flist.csv"
