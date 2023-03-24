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
wget --no-check-certificate https://download.ncg.ingrid.pt/webdav/udocker/udocker-englib-${1}.tar.gz

echo "unzip/untar udocker-englib-${1}.tar.gz"
tar zxvf udocker-englib-${1}.tar.gz

BIN="${TMPDIR}/udocker_dir/bin"
LIB="${TMPDIR}/udocker_dir/lib"

rm ${FILE_LIST}
cd ${BIN}
for fname in `find * -type f`
do
    TAR="${TAR_DIR}/${fname}.tgz"
    tar zcvf ${TAR} ${fname}
    line=`sha256sum ${TAR}`
    SHA256=$(echo $line | awk -F' ' '{printf "%s", $1}' | tr -d '"')
    echo "${fname}.tgz,${SHA256}" >> ${FILE_LIST}
done

cd ${LIB}
for fname in `find * -name 'libfakechroot-*' -type f`
do
    TAR="${TAR_DIR}/${fname}.tgz"
    tar zcvf ${TAR} ${fname}
    line=`sha256sum ${TAR}`
    SHA256=$(echo $line | awk -F' ' '{printf "%s", $1}' | tr -d '"')
    echo "${fname}.tgz,${SHA256}" >> ${FILE_LIST}
done
