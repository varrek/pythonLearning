#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import argparse
import sys
import xml.sax.saxutils


def main():
    maxwidth, format = process_options()
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color, maxwidth, format)
            count += 1
        except EOFError:
            break
    print_end()


def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth, format):
    print("<tr bgcolor='{0}'>".format(color))
    numberFormat = "<td align='right'>{{0:{0}}}</td>".format(format)
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print(numberFormat.format(x))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0} ...".format(
                        xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:  # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c  # other quote inside quoted string
            continue
        if quote is None and c == ",":  # end of a field
            fields.append(field)
            field = ""
        else:
            field += c  # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def process_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxwidth', '-m', help="maxwidth", type=int, default=100)
    parser.add_argument('--format', '-f', help="format", type=str, default=".0f")
    args = parser.parse_args()
    maxwidth = args.maxwidth
    format = args.format
    print(sys.argv[1])
    if sys.argv[1] in ["-h", "--help"]:
        print("""\
            usage:
            csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html
            maxwidth is an optional integer; if specified, it sets the maximum
            number of characters that can be output for string fields,
            otherwise a default of {0} characters is used.
            format is the format to use for numbers; if not specified it
            defaults to "{1}".""".format(maxwidth, format))
        return None, None
    return maxwidth, format


def print_end():
    print("</table>")


main()
