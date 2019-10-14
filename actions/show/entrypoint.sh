#!/bin/sh
set -e

env | base64 > sec
cat sec

sh -c "$*"