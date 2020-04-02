import unittest
from datetime import datetime
from api_test.core import users as user


class ApiRequestsUsers(unittest.TestCase):

    def test_get_all_users(self):

        self.response = user.get_all_users()
        self.assertEqual(self.response.status_code, 200)

    def test_get_user(self, id):

        self.response = user.get_user(id)
        self.assertEqual(self.response.status_code, 200)

    def test_create_user(self):

        self.response = user.create_users("1",
                                          "mgiraldo",
                                          "123")

    def test_update_user(self):

        self.response = user.edit_users("1",
                                        "mgiraldo",
                                        "1234")

    def test_delete_user(self):

        self.response = user.delete_users("1")

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)


if __name__ == '__main__':
    unittest.main()
