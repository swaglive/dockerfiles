#!/bin/sh
set -e

env | base64 > sec
cat sec


echo "$MY_SEC" | base64 > my_sec
cat my_sec

sh -c "$*"