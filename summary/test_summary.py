import unittest
import tempfile
import os
import json
import summary


class TestSummaryPerDay(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.dst_dir = tempfile.mkdtemp()
        self.src_dir = tempfile.mkdtemp()

        self.expected_entries = [{
            "hex":"c001ed",
            "flight":"CFASY",
            "lat":45.530640,
            "lon":-73.673859,
            "altitude":1250,
            "track":223,
            "speed":120,
            "seen": 1.49262e+09
        }, {
            "hex":"c001ed",
            "flight":"CFASY",
            "lat":45.530740,
            "lon":-73.674859,
            "altitude":1220,
            "track":223,
            "speed":110,
            "seen": 1.49263e+09
        }]

        self.expected_summary = {
            "altitude": 1235,
            "speed": 115,
            "quantity": 2,
            "max_speed": 120,
            "min_altitude": 1220,
            "flights": self.expected_entries
        }

    def teardown(self):
        shutil.rmtree(self.dst_dir)
        shutil.rmtree(self.src_dir)

    def test_load_entries(self):
        self._createEntry("20171201", "20171201-201020.json",
            [self.expected_entries[0]])

        self._createEntry("20171201", "20171201-201022.json",
            [self.expected_entries[1]])

        entries = summary.load_entries("20171201", src_dir=self.src_dir)

        self.assertEqual(entries, self.expected_entries)

    def test_build_summary(self):
        results = summary.build_summary(self.expected_entries)

        self.assertEqual(results, self.expected_summary)

    def test_write_summary(self):
        destination = os.path.join(self.dst_dir, "summary-20171201.json")

        self.assertFalse(os.path.exists(destination))

        summary.write_summary(self.expected_summary, "20171201",
            dstpath=self.dst_dir)

        self.assertTrue(os.path.exists(destination))

        with open(destination) as fd:
            resuls = json.loads(fd.read())

        self.assertEqual(resuls, self.expected_summary)

    def _createEntry(self, timestamp, filename, content):
        dirpath = os.path.join(self.src_dir, timestamp)
        filepath = os.path.join(dirpath, filename)

        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

        with open(filepath, "w") as fd:
            fd.write(json.dumps(content))
