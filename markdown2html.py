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

            return f"{open_tag}{actual_sentence}{closing_tag}\n"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    md_file, html_file = sys.argv[1:]

    if not os.path.exists(md_file) and not os.path.isfile(md_file):
        print("Missing <filename>", file=sys.stderr)
        sys.exit(1)

    with open(md_file, "r") as md_str:
        md_str_list = md_str.readlines()
        html_result_list = []

        md_str_list = [line.replace("\n", "") for line in md_str_list]
        for line in md_str_list:
            line = parse_heading(line)
            html_result_list.append(line)

        with open(html_file, "w") as html:
            html.writelines(html_result_list)
