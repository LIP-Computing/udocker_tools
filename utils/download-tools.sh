#!/bin/bash
#
# Copyright 2021-2023 LIP
#
# Author: Mario David <mariojmdavid@gmail.com>
#
# This script produces downloads the udocker tools tarball and unzips it

cd ..
DIR=`pwd`
TAR_DIR="${DIR}/tarballs"
TMPDIR=${HOME}/tmpdir
mkdir -p ${TMPDIR}

if [ $# -ne 1 ]
then
    echo "Usage: $0 <udocker tools tarball version>"
    echo "Example: $0 1.2.10"
    exit 1
fi

echo "wget udocker tools tarball to ${TMPDIR}"
cd ${TAR_DIR}
rm -rf *

wget https://download.ncg.ingrid.pt/webdav/udocker/udocker-englib-${1}.tar.gz
echo "unzip/untar udocker-englib-${1}.tar.gz"
tar zxvf udocker-englib-${1}.tar.gz -C ${TMPDIR}
