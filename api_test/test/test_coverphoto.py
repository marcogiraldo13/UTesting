import unittest
from datetime import datetime
from api_test.core import coverphoto as act


class ApiRequestsCoverPhoto(unittest.TestCase):
    now = datetime.now()

    def test_get_all_coverphoto(self):
        self.response = act.get_all_coverphoto()
        self.assertEqual(self.response.status_code, 200)

    def test_get_coverphoto(self, id):
        self.response = act.get_coverphoto(id)
        self.assertEqual(self.response.status_code, 200)

    def test_get_coverbookphoto(self, id):
        self.response = act.get_coverbookphoto(id)
        self.assertEqual(self.response.status_code, 200)

    def test_create_coverphoto(self):
        self.response = act.create_coverphoto("20",
                                              "1",
                                              "url de prueba")

    def test_update_coverphoto(self):
        self.response = act.edit_coverphoto("20",
                                            "1",
                                            "url de prueba")

    def test_delete_coverphoto(self):
        self.response = act.delete_coverphoto("20")

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)


if __name__ == '__main__':
    unittest.main()
