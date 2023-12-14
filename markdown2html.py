#!/usr/bin/python3
"""
This script converts markdown syntax html syntax.
"""
import os
import sys


def parse_heading(string):
    heading = {
        "# ": "h1",
        "## ": "h2",
        "### ": "h3",
        "#### ": "h4",
        "##### ": "h5",
        "###### ": "h6",
    }
    for i in heading.keys():
        if line.startswith(i):
            open_tag = f"<{heading[i]}>"
            closing_tag = f"</{heading[i]}>"
            actual_sentence = string.replace(i, "")

    return f"{open_tag}{actual_sentence}{closing_tag}"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./markdown2html.py README.md README.html")

    md_file, html_file = sys.argv[1:]

    if not os.path.exists(md_file):
        sys.exit("Missing <filename>")

    with open(md_file, "r") as md_str:
        md_str_list = md_str.readlines()

        md_str_list = [line.replace("\n", "") for line in md_str_list]
        with open(html_file, "w") as html:
            for line in md_str_list:
                line = parse_heading(line)
                html.write(line + "\n")
