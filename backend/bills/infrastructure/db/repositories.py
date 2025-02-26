from django.db import connection
from bills.domain.models import Bill

class BillRepository:
    def get_all(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, title, primary_sponsor FROM bills_bill")
            rows = cursor.fetchall()

        return [Bill(id=rows[0], title=rows[1], primary_sponsor=rows[2]) for rows in rows]


    def get_bill_with_supporter_and_opposer_count(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT bill.id, bill.title,
                    COUNT(CASE WHEN vr.vote_type = 1 THEN 1 END) AS supporters,
                    COUNT(CASE WHEN vr.vote_type = 2 THEN 1 END) AS opposers,
                    bill.primary_sponsor
                FROM bills_bill as bill
                LEFT JOIN votes_vote AS v ON v.bill_id = bill.id
                LEFT JOIN vote_results_vote_result AS vr ON vr.vote_id = v.id
                GROUP BY bill.id, bill.title, bill.primary_sponsor;
            """)
            rows = cursor.fetchall()

            return [
                {
                    "bill": Bill(id=row[0], title=row[1], primary_sponsor=row[4]),
                    "supporters": row[2],
                    "opposers": row[3],
                }
                for row in rows
            ]


    def save_bulk(self, bills_data):
        BATCH_SIZE = 1000

        try:
            with connection.cursor() as cursor:
                cursor.execute("BEGIN;")
                query = """
                    INSERT INTO bills_bill (id, title, primary_sponsor) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING;
                """

                batch = []
                for row in bills_data:
                    batch.append((row['id'], row['title'], row['primary_sponsor']))

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