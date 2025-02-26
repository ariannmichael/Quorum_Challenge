from django.test import TestCase
from django.db import connection

class BillVoteCountTest(TestCase):
    """
    Unit tests for counting supporters and opposers for each bill.
    """

    def setUp(self):
        """
        Set up test data before running the tests.
        """
        with connection.cursor() as cursor:
            # Insert test data into legislators table
            cursor.execute("INSERT INTO legislators_legislator (id, name) VALUES (1, 'John Doe'), (2, 'Jane Smith');")

            # Insert test data into bills table
            cursor.execute("INSERT INTO bills_bill (id, title, primary_sponsor) VALUES (1, 'Infrastructure Bill', 1), (2, 'Healthcare Reform', 2);")

            # Insert test data into votes table
            cursor.execute("INSERT INTO votes_vote (id, bill_id) VALUES (100, 1), (101, 2);")

            # Insert test data into vote_results table
            cursor.execute("""
                INSERT INTO vote_results_vote_result (id, legislator_id, vote_id, vote_type) VALUES 
                (200, 1, 100, 1),  -- John Doe supports Bill 1
                (201, 2, 100, 2),  -- Jane Smith opposes Bill 1
                (202, 1, 101, 1),  -- John Doe supports Bill 2
                (203, 2, 101, 1);  -- Jane Smith supports Bill 2
            """)

    def test_bill_vote_counts(self):
        """
        Test if the query correctly counts supporters and opposers for each bill.
        """
        query = """
            SELECT bill.id, bill.title, 
                   COUNT(CASE WHEN vr.vote_type = 1 THEN 1 END) AS supporters, 
                   COUNT(CASE WHEN vr.vote_type = 2 THEN 1 END) AS opposers, 
                   bill.primary_sponsor
            FROM bills_bill AS bill
            LEFT JOIN votes_vote AS v ON v.bill_id = bill.id
            LEFT JOIN vote_results_vote_result AS vr ON vr.vote_id = v.id
            GROUP BY bill.id, bill.title, bill.primary_sponsor;
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()

        expected_results = [
            (1, 'Infrastructure Bill', 1, 1, 1),  # Bill 1: 1 supporter, 1 opposer
            (2, 'Healthcare Reform', 2, 0, 2)  # Bill 2: 2 supporters, 0 opposers
        ]

        results.sort()
        expected_results.sort()

        self.assertEqual(results, expected_results, f"Expected {expected_results} but got {results}")

