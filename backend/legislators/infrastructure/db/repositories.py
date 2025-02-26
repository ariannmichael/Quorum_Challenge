from django.db import connection
from legislators.domain.models import Legislator


class LegislatorRepository:
  def get_all(self):
    with connection.cursor() as cursor:
      cursor.execute("SELECT id, name FROM legislators_legislator")
      rows = cursor.fetchall()

    return [Legislator(id=rows[0], name=rows[1]) for rows in rows]


  def get_legislators_with_vote_counts(self):
    with connection.cursor() as cursor:
      cursor.execute("""
        SELECT legislator.id, legislator.name,
        (SELECT COUNT(*) from vote_results as vr WHERE vr.legislator_id = legislator.id AND vr.vote_type = 1) as supported_bills,
        (SELECT COUNT(*) from vote_results as vr WHERE vr.legislator_id = legislator.id AND vr.vote_type = 2) as opposed_bills,
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
    with connection.cursor() as cursor:
      query = """
        INSERT INTO legislators_legislator (id, name)
        VALUES (%s, %s)
        ON CONFLICT (id) DO NOTHING
      """

    cursor.executemany(query, [(row['id'], row['name']) for row in legislators_data])