from django.db import connection
from legislators.domain.models import Legislator


class LegislatorRepository:
  def get_all(self):
    with connection.cursor() as cursor:
      cursor.execute("SELECT id, name FROM legislators_legislator")
      rows = cursor.fetchall()

    return [Legislator(id=row[0], name=row[1]) for row in rows]


  def get_legislators_with_vote_counts(self):
    with connection.cursor() as cursor:
      cursor.execute("""
        SELECT legislator.id, legislator.name,
        (SELECT COUNT(*) from vote_results_vote_result as vr WHERE vr.legislator_id = legislator.id AND vr.vote_type = 1) as supported_bills,
        (SELECT COUNT(*) from vote_results_vote_result as vr WHERE vr.legislator_id = legislator.id AND vr.vote_type = 2) as opposed_bills
        FROM legislators_legislator AS legislator
      """)
      rows = cursor.fetchall()

      return [
        {
          "legislator": Legislator(id=row[0], name=row[1]),
          "supported_bills": row[2],
          "opposed_bills": row[3]
        }
        for row in rows
      ]

  def save_bulk(self, legislators_data):
    if not legislators_data:
      return

    BATCH_SIZE = 1000

    query = """
        INSERT INTO legislators_legislator (id, name)
        VALUES (%s, %s)
        ON CONFLICT (id) DO NOTHING;
    """

    try:
      with connection.cursor() as cursor:
        cursor.execute("BEGIN;")

        batch = []
        for row in legislators_data:
          batch.append((row['id'], row['name']))

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
