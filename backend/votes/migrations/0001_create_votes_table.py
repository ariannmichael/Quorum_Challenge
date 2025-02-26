from django.db import migrations, connection

def create_votes_table(apps, schema_editor):
    """
    Creates the votes table using raw SQL.
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE votes_vote (
                id SERIAL PRIMARY KEY,
                bill_id INTEGER NOT NULL,
                CONSTRAINT fk_bill FOREIGN KEY (bill_id) REFERENCES bills_bill(id) ON DELETE CASCADE
            );
        """)

def drop_votes_table(apps, schema_editor):
    """
    Drops the votes table if migration is rolled back.
    """
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS votes_vote;")

class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_create_bills_table'),  # Ensure 'bills' table exists first
    ]

    operations = [
        migrations.RunPython(create_votes_table, drop_votes_table),
    ]
