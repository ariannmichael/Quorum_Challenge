from django.db import connection
from votes.domain.models import Vote


class VoteResultsRepository:
    def get_all(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, legislator_id, vote_id, vote_type FROM vote_results_vote_result")
            rows = cursor.fetchall()

        return [Vote(id=row[0], bill_id=row[1]) for row in rows]


    def check_legislator_exists(self, legislator_id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM legislators_legislator WHERE id = %s;", [legislator_id])
            return cursor.fetchone()[0] > 0


    def check_vote_exists(self, vote_id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM votes_vote WHERE id = %s;", [vote_id])
            return cursor.fetchone()[0] > 0


    def save_bulk(self, vote_results_data):
        if not vote_results_data:
            return

        BATCH_SIZE = 1000

        query = """
          INSERT INTO vote_results_vote_result (id, legislator_id, vote_id, vote_type)
          VALUES (%s, %s, %s, %s)
          ON CONFLICT (id) DO NOTHING;
      """

        try:
            with connection.cursor() as cursor:
                cursor.execute("BEGIN;")

                batch = []
                for row in vote_results_data:
                    legislator_id = row.get('legislator_id')
                    vote_id = row.get('vote_id')

                    if not self.check_legislator_exists(legislator_id):
                        print(f"Legislator {legislator_id} does not exist.")
                        continue

                    if not self.check_vote_exists(vote_id):
                        print(f"Vote {vote_id} does not exist.")
                        continue

                    batch.append((row['id'], row['legislator_id'], row['vote_id'], row['vote_type']))

                    if len(batch) >= BATCH_SIZE:
                        cursor.executemany(query, batch)
                        batch.clear()

                if batch:
                    cursor.executemany(query, batch)

                cursor.execute("COMMIT;")

        except Exception as e:
            with connection.cursor() as cursor:
                cursor.execute("ROLLBACK;")
            print(f"Database error: {e}")
