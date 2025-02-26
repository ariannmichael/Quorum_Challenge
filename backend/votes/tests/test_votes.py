from django.test import TestCase
from django.db import connection

class TestVotes(TestCase):
    """
    Unit tests for votes-related queries.
    """

    def setUp(self):
        """
        Set up test data before running the tests.
        """
        with connection.cursor() as cursor:
            # Insert test data into bills table
            cursor.execute("""
                INSERT INTO bills_bill (id, title, primary_sponsor) 
                VALUES 
                (1, 'Infrastructure Bill', 101), 
                (2, 'Healthcare Reform', 102);
            """)

            # Insert test data into votes table
            cursor.execute("""
                INSERT INTO votes_vote (id, bill_id) 
                VALUES 
                (100, 1), 
                (101, 2);
            """)

    def test_vote_exists(self):
        """
        Test if a vote exists in the database.
        """
        vote_id = 100
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM votes_vote WHERE id = %s;", [vote_id])
            result = cursor.fetchone()[0]

        self.assertEqual(result, 1, f"Expected 1 vote with ID {vote_id}, but got {result}")

    def test_get_all_votes(self):
        """
        Test fetching all votes.
        """
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, bill_id FROM votes_vote ORDER BY id;")
            results = cursor.fetchall()

        expected_results = [
            (100, 1),
            (101, 2)
        ]

        self.assertEqual(results, expected_results, f"Expected {expected_results} but got {results}")

    def test_vote_not_exists(self):
        """
        Test that a vote that is not in the database returns 0.
        """
        vote_id = 999  # Non-existing ID
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM votes_vote WHERE id = %s;", [vote_id])
            result = cursor.fetchone()[0]

        self.assertEqual(result, 0, f"Expected 0 votes with ID {vote_id}, but got {result}")
