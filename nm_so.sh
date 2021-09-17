#!/bin/bash


#OUTPUT_PATH=`pwd`/dex/out.dex
#INPUT_PATH=`pwd`/dex/classes
NDK_VERSION=21.4.7075529
TOOLCHAIN=/Users/huzhou/Library/Android/sdk/ndk/$NDK_VERSION/toolchains/llvm/prebuilt/darwin-x86_64
NM=$TOOLCHAIN/bin/aarch64-linux-android-nm
SO=app/libs/arm64-v8a/libjingle_peerconnection_so.so

$NM $SO
