#!/usr/bin/python3
"""
This script converts markdown syntax html syntax.
"""
import os
import sys

print(sys.argv[1])
if len(sys.argv) != 3:
    sys.exit("Usage: ./markdown2html.py README.md README.html")

if not os.path.exists(sys.argv[1]):
    sys.exit("Missing <filename>")
