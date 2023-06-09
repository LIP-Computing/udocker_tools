#!/bin/bash
#
# Copyright 2021-2023 LIP
#
# Author: Mario David <mariojmdavid@gmail.com>
#
# This script produces all tarballs, the sha256sum and makes a CSV with the filename and sha256sum

cd ..
DIR=`pwd`
TAR_DIR="${DIR}/tarballs"
FILE_LIST=${DIR}/flist.csv
TMPDIR=${HOME}/tmpdir
mkdir -p ${TMPDIR}

if [ $# -ne 1 ]
then
    echo "Usage: $0 <udocker tools tarball version>"
    echo "Example: $0 1.2.9"
    exit 1
fi

echo "wget udocker tools tarball to ${TMPDIR}"
cd ${TMPDIR}
rm -rf *
wget --no-check-certificate https://download.ncg.ingrid.pt/webdav/udocker/udocker-englib-${1}.tar.gz

echo "unzip/untar udocker-englib-${1}.tar.gz"
tar zxvf udocker-englib-${1}.tar.gz
