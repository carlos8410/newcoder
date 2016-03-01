"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.

Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.

Copyright (c) 2016 Weixin Zhao
Distributed under the Creative Commons license. See LICENSE for details.
"""


import csv

MY_FILE = 'sample_sfpd_incident_all.csv'

def parse(raw_file, delimiter):
    """ Parse a raw csv file to a JSON-line object."""
    parsed_data = []
    try:
        f = open(raw_file, 'r')
        reader = csv.reader(f, delimiter=delimiter)
    except:
        print("Error in reading the raw data file.")
        raise 
    fields = reader.next()
    for row in reader:
        parsed_data.append(dict(zip(fields, row)))
    f.close()
    return parsed_data

if __name__ == "__main__":
    parsed_data = parse(MY_FILE, ',')


