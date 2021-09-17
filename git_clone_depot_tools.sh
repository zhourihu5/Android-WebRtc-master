#!/bin/bash

cd ..
echo `pwd`
while ( ! git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git)
do
  echo "再来一次试试"
done
