#!/bin/bash
#
# Copyright 2020 LIP
#
# Author: Mario David <mariojmdavid@gmail.com>
#
# This script produces all tarballs, the sha256sum and makes a CSV with the filename and sha256sum

cd ..
DIR=`pwd`
BIN="${DIR}/engines/bin"
LIB="${DIR}/engines/lib"
TAR_DIR="${DIR}/tarballs"
FILE_LIST=${DIR}/flist.csv

for direxe in ${BIN} ${LIB}
do
    cd ${direxe}
    for fname in `find * -type f`
    do
        TAR="${TAR_DIR}/${fname}.tgz"
        tar zcvf ${TAR} ${fname}
        line=`sha256sum ${TAR}`
        SHA256=$(echo $line | awk -F' ' '{printf "%s", $1}' | tr -d '"')
        echo "${fname}.tgz,${SHA256}" >> ${FILE_LIST}
    done
done
