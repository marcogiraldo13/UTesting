import unittest
from datetime import datetime
from api_test.core import books as book


class ApiRequestsBooks(unittest.TestCase):
    now = datetime.now()

    def test_get_all_books(self):

        self.response = book.get_all_books()
        self.assertEqual(self.response.status_code, 200)

    def test_get_book(self, id):

        self.response = book.get_book(id)
        self.assertEqual(self.response.status_code, 200)

    def test_create_book(self):

        self.response = book.create_book("1",
                                         "Cien años de soledad",
                                         "Novela",
                                         500,
                                         "excerpt",
                                         self.now,
                                         200)

    def test_update_book(self):

        self.response = book.edit_book("1",
                                         "Cien años de soledad",
                                         "Novela",
                                         500,
                                         "excerpt",
                                         self.now,
                                         200)

    def test_delete_book(self):

        self.response = book.delete_books("1")

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)


if __name__ == '__main__':
    unittest.main()
