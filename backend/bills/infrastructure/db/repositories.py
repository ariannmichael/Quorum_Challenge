from django.db import connection
from bills.domain.models import Bill

class BillRepository:
    def get_all(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, title, primary_sponsor FROM bills")
            rows = cursor.fetchall()

        return [Bill(id=rows[0], title=rows[1], primary_sponsor=rows[2]) for rows in rows]


    def get_bill_with_supporter_and_opposer_count(self):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT bill.id, bill.title,
                (SELECT COUNT(*) FROM vote_results as vr LEFT JOIN vote v on v.id = vr.vote_id WHERE v.bill_id = bill.id AND vr.vote_type = 1) as supporters,
                (SELECT COUNT(*) FROM vote_results as vr LEFT JOIN vote v on v.id = vr.vote_id WHERE v.bill_id = bill.id AND vr.vote_type = 2) as opposers,
                bill.primary_sponsor FROM bills_bill as bill
            """)
            rows = cursor.fetchall()

            return [
                {
                    "bill": Bill(id=row[0], title=row[1]),
                    "supporters": row[2],
                    "opposers": row[3],
                    "primary_sponsor": row[4]
                }
                for row in rows
            ]


    def save_bulk(self, bills_data):
        BATCH_SIZE = 1000

        with connection.cursor() as cursor:
            cursor.execute("BEGIN;")
            query = """
                INSERT INTO bills_bill (id, title, primary_sponsor) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING;
            """

            batch = []
            skipped_bills = []
            for row in bills_data:
                batch.append((row['id'], row['title'], row['primary_sponsor']))

                if len(batch) >= BATCH_SIZE:
                    cursor.executemany(query, batch)
                    batch.clear()

            if batch:
                cursor.executemany(query, batch)

            cursor.execute("COMMIT;")

        return skipped_bills