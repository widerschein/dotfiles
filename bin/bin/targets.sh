#!/usr/bin/env bash

grep -E '^(alias|lib|test-suite)' Jamfile \
    | awk '{ print $1":", $2 }' \
    | fzf \
    | awk '{ print $2 }' \
    | xargs printf "$(pwd)//%s" \
    | xargs bj_dbg.sh
