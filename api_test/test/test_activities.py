import unittest
from datetime import datetime
from api_test.core import activities as act


class ApiRequestsActivities(unittest.TestCase):
    now = datetime.now()

    def test_get_all_activites(self):

        self.response = act.get_all_activities()
        self.assertEqual(self.response.status_code, 200)

    def test_get_activity(self, id):

        self.response = act.get_activity(id)
        self.assertEqual(self.response.status_code, 200)

    def test_create_activity(self):

        self.response = act.create_activity("20",
                                            "mi actividad de prueba",
                                            self.now,
                                            True)

    def test_update_activity(self):

        self.response = act.create_activity("20",
                                            "cambio en mi actividad",
                                            self.now,
                                            True)

    def test_delete_activity(self):

        self.response = act.delete_activity("20")

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)


if __name__ == '__main__':
    unittest.main()
