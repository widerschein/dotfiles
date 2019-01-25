#!/bin/bash

rsync -av --progress --delete --exclude-from=${HOME}/bin/backup_exclude.txt ${HOME} /mnt/backup
