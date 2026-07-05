#!/bin/bash
set -e
cd "$(dirname "$0")"
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Starting Bot..."
python main.py
