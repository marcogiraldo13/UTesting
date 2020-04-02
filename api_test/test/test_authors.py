import unittest
from datetime import datetime
from api_test.core import authors as author


class ApiRequestsAuthors(unittest.TestCase):
    now = datetime.now()

    def test_get_all_authors(self):

        self.response = author.get_all_authors()
        self.assertEqual(self.response.status_code, 200)

    def test_get_author(self, id):

        self.response = author.get_author(id)
        self.assertEqual(self.response.status_code, 200)

    def test_create_author(self):

        self.response = author.create_author("1",
                                             "1",
                                             "alex",
                                             "velez",
                                             200)

    def test_update_author(self):

        self.response = author.edit_author("1",
                                           "1",
                                           "marco",
                                           "giraldo")

    def test_delete_author(self):

        self.response = author.delete_author("1")

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)


if __name__ == '__main__':
    unittest.main()
