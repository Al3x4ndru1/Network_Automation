#!/bin/bash

sudo find /var/ -size +10M -ls | sort -n -r -k 7

sudo truncate -s 0 /var/log/syslog

sudo journalctl --disk-usage

sudo journalctl --rotate

sudo journalctl --vacuum-time=1s

sudo journalctl --rotate --vacuum-size=500M

sudo snap list --all | while read snapname ver rev trk pub notes; do if [[ $notes = *disabled* ]]; then snap remove "$snapname" --revision="$rev"; fi; done
