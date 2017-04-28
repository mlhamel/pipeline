#!/usr/bin/env python

import time
import json
import os

SRC_DATA_PATH = "/pfs/fixed_time_sorting"


def write_summary(summary, timestamp, dstpath="/pfs/out"):
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

    summary = {}
    summary["altitude"] = int(altitude/quantity)
    summary["speed"] = int(speed/quantity)
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
    timestamp = time.strftime("%Y%m%d")

    entries = load_entries(timestamp)
    summary = build_summary(entries)
    write_summary(summary, timestamp)


if __name__ == '__main__':
    main()
