from django.test import TestCase
from django.db import connection

class TestLegislators(TestCase):
    """
    Unit tests for legislators-related queries.
    """

    def setUp(self):
        """
        Set up test data before running the tests.
        """
        with connection.cursor() as cursor:
            # Insert test legislators
            cursor.execute("""
                INSERT INTO legislators_legislator (id, name) 
                VALUES 
                (1, 'John Doe'), 
                (2, 'Jane Smith'), 
                (3, 'Alice Johnson');
            """)

    def test_legislator_exists(self):
        """
        Test if a legislator exists in the database.
        """
        legislator_id = 1
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM legislators_legislator WHERE id = %s;", [legislator_id])
            result = cursor.fetchone()[0]

        self.assertEqual(result, 1, f"Expected 1 legislator with ID {legislator_id}, but got {result}")

    def test_get_all_legislators(self):
        """
        Test fetching all legislators.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM legislators_legislator ORDER BY id;")
            results = cursor.fetchall()

        expected_results = [
            (1, 'John Doe'),
            (2, 'Jane Smith'),
            (3, 'Alice Johnson')
        ]

        self.assertEqual(results, expected_results, f"Expected {expected_results} but got {results}")

    def test_legislator_not_exists(self):
        """
        Test that a legislator who is not in the database returns 0.
        """
        legislator_id = 99  # Non-existing ID
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM legislators_legislator WHERE id = %s;", [legislator_id])
            result = cursor.fetchone()[0]

        self.assertEqual(result, 0, f"Expected 0 legislators with ID {legislator_id}, but got {result}")
