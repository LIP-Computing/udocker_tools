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
TMPDIR=${HOME}/tmpdir
BIN="${TMPDIR}/udocker_dir/bin"
LIB="${TMPDIR}/udocker_dir/lib"

cd ${BIN}
echo "In dir: ${BIN}"
for fname in `find . -type f`
do
    TAR="${TAR_DIR}/${fname}.tgz"
    tar zcvf ${TAR} ${fname}
done

# cd ${LIB}
# echo "In dir: ${LIB}"
# for fname in `find . -name 'libfakechroot-*' -type f`
# do
#     TAR="${TAR_DIR}/${fname}.tgz"
#     tar zcvf ${TAR} ${fname}
# done

# cd ${LIB}
# echo "In dir: ${LIB}"
# for fname in `find . -name 'libfakechroot-*' -type l`
# do
#     link_to=`readlink ${fname} `
#     echo "TARZipping: ${fname} and ${link_to}"
#     TAR="${TAR_DIR}/${fname}.tgz"
#     tar zcvfp ${TAR} ${fname} ${link_to}
# done

cd ${LIB}
tar zcvfp ${TAR_DIR}/libfakechroot-x86_64.tgz libfakechroot-*-x86_64.so
tar zcvfp ${TAR_DIR}/libfakechroot-arm64.tgz libfakechroot-*-arm64.so
tar zcvfp ${TAR_DIR}/libfakechroot-ppc64le.tgz libfakechroot-*-ppc64le.so
