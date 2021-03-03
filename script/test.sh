#!/usr/bin/env bash
data01=`cat /usr/123.txt`
data02=`cat /usr/234.txt`
if test ${data01} -eq ${data02}
then
echo "Don't need to fetch the package!"
else
echo "Need to fetch the package!"
fi
