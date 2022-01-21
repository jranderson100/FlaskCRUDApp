import unittest
import os.path


from images_test import check_images_exist

class ImagesTestClass(unittest.TestCase):
    def test_images(self):
        self.assertTrue(check_images_exist)

   

if __name__ == '__main__':
    unittest.main()