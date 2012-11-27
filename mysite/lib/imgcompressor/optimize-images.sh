#!/bin/sh

##################################################
# This script optimizes image maps by appliying  #
# jpegtran for lossless compression to improve   #
# page loading                                   #
##################################################

EXTENSIONS="jpe?g"

if [ -z "$1" ]; then
    DIR="`pwd`"
else
    DIR="$1"
fi

echo $DIR

# Optimize JPEG images
find $DIR -regextype posix-egrep -regex ".*\.($EXTENSIONS)\$" -type f | xargs -I{} jpegtran -optimize -progressive -outfile "{}.optimized" "{}"

# Rename xxx.jpg.optimize to xxx.jpg

for file in $(find $DIR -name '*.optimized'); do
    chown $(stat -c "%U:%G" "${file%.optimized}") "$file"
    chmod $(stat -c "%a" "${file%.optimized}") "$file"
    mv -f "$file" "${file%.optimized}";
done


