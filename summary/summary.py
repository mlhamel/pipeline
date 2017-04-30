#!/usr/bin/env python

import time
import json
import os

SRC_DATA_PATH = "/pfs/fixed_time_sorting"


def write_summary(timestamp, summary, dstpath="/pfs/out"):
    filename = "summary-{timestamp}.json".format(timestamp=timestamp)
    filepath = os.path.join(dstpath, filename)

    with open(filepath, "w") as fd:
        fd.write(json.dumps(summary))


def build_summary(entries):
    altitude = 0
    speed = 0
    quantity = 0
    max_speed = 0
    min_altitude = float("inf")
    flights = []

    for entry in entries:
        if entry["speed"] > max_speed:
            max_speed = entry["speed"]
        if entry["altitude"] < min_altitude:
            min_altitude = entry["altitude"]
        quantity += 1
        altitude += entry["altitude"]
        speed += entry["speed"]
        flights.append(entry)

    divider = max([1, quantity])

    summary = {}
    summary["altitude"] = int(altitude/divider)
    summary["speed"] = int(speed/divider)
    summary["quantity"] = quantity
    summary["max_speed"] = max_speed
    summary["min_altitude"] = min_altitude
    summary["flights"] = flights

    return summary


def load_entries(timestamp, src_dir=SRC_DATA_PATH):
    path = os.path.join(src_dir, timestamp)
    entries = []

    for dirpath, dirs, files in os.walk(path):
        for item in files:
            filepath = os.path.join(dirpath, item)
            with open(filepath) as data_file:
                entries += json.load(data_file)
    return entries


def main():
    date = time.strftime("%Y%m%d")
    timestamp = time.strftime("%Y%m%d-%M%H%S")

    entries = load_entries(date)
    summary = build_summary(entries)
    write_summary(timestamp, summary)


if __name__ == '__main__':
    main()
