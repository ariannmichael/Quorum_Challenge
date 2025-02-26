from django.db import connection
from votes.domain.models import Vote


class VotesRepository:
    def get_all(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, bill_id FROM votes_vote")
            rows = cursor.fetchall()

        return [Vote(id=row[0], bill_id=row[1]) for row in rows]

    def save_bulk(self, votes_data):
        if not votes_data:
            return

        BATCH_SIZE = 1000

        query = """
          INSERT INTO votes_vote (id, bill_id)
          VALUES (%s, %s)
          ON CONFLICT (id) DO NOTHING;
      """

        try:
            with connection.cursor() as cursor:
                cursor.execute("BEGIN;")

                batch = []
                for row in votes_data:
                    batch.append((row['id'], row['bill_id']))

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
