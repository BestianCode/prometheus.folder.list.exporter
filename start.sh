#!/bin/bash

set -e

while true; do
    python3 exporter.py || true
    sleep 1
done
