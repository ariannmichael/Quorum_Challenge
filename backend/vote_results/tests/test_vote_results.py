from django.test import TestCase
from django.db import connection

class TestVoteResults(TestCase):
    """
    Unit tests for vote results-related queries.
    """

    def setUp(self):
        """
        Set up test data before running the tests.
        """
        with connection.cursor() as cursor:
            # Insert test data into legislators table
            cursor.execute("""
                INSERT INTO legislators_legislator (id, name) 
                VALUES 
                (1, 'John Doe'), 
                (2, 'Jane Smith');
            """)

            # Insert test data into bills table
            cursor.execute("""
                INSERT INTO bills_bill (id, title, primary_sponsor) 
                VALUES 
                (1, 'Infrastructure Bill', 1), 
                (2, 'Healthcare Reform', 2);
            """)

            # Insert test data into votes table
            cursor.execute("""
                INSERT INTO votes_vote (id, bill_id) 
                VALUES 
                (100, 1), 
                (101, 2);
            """)

            # Insert test data into vote_results table
            cursor.execute("""
                INSERT INTO vote_results_vote_result (id, legislator_id, vote_id, vote_type) 
                VALUES 
                (200, 1, 100, 1),  -- John Doe supports Bill 1
                (201, 2, 100, 2),  -- Jane Smith opposes Bill 1
                (202, 1, 101, 1),  -- John Doe supports Bill 2
                (203, 2, 101, 1);  -- Jane Smith supports Bill 2
            """)

    def test_vote_result_exists(self):
        """
        Test if a vote result exists in the database.
        """
        vote_result_id = 200
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM vote_results_vote_result WHERE id = %s;", [vote_result_id])
            result = cursor.fetchone()[0]

        self.assertEqual(result, 1, f"Expected 1 vote result with ID {vote_result_id}, but got {result}")

    def test_get_all_vote_results(self):
        """
        Test fetching all vote results.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, legislator_id, vote_id, vote_type FROM vote_results_vote_result ORDER BY id;")
            results = cursor.fetchall()

        expected_results = [
            (200, 1, 100, 1),
            (201, 2, 100, 2),
            (202, 1, 101, 1),
            (203, 2, 101, 1)
        ]

        self.assertEqual(results, expected_results, f"Expected {expected_results} but got {results}")

    def test_vote_result_not_exists(self):
        """
        Test that a vote result that is not in the database returns 0.
        """
        vote_result_id = 999  # Non-existing ID
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM vote_results_vote_result WHERE id = %s;", [vote_result_id])
            result = cursor.fetchone()[0]

        self.assertEqual(result, 0, f"Expected 0 vote results with ID {vote_result_id}, but got {result}")
