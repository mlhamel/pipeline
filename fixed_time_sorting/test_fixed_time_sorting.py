import unittest
import tempfile
import shutil
import os
import fixed_time_sorting

class TestFixedTimeSorting(unittest.TestCase):
    def setUp(self):
        self.dst_dir = tempfile.mkdtemp()
        self.src_dir = tempfile.mkdtemp()

    def teardown(self):
        shutil.rmtree(self.dst_dir)
        shutil.rmtree(self.src_dir)

    def test_move_per_day(self):
        self._touch_file(self.src_dir, "20171201-201020.json")

        destination = os.path.join(self.dst_dir, "20171201")

        self.assertFalse(os.path.exists(destination))

        fixed_time_sorting.move_per_day(self.src_dir, "20171201-201020.json", dstpath=self.dst_dir)

        self.assertEqual(os.listdir(destination), ["20171201-201020.json"])

    def _touch_file(self, path, filename):
        filepath = os.path.join(path, filename)
        with open(filepath, 'a'):
            os.utime(filepath, None)

if __name__ == '__main__':
    unittest.main()
