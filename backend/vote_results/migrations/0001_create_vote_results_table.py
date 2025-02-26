from django.db import migrations, connection

def create_vote_results_table(apps, schema_editor):
    """
    Creates the vote_results table using raw SQL.
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE vote_results_vote_result (
                id SERIAL PRIMARY KEY,
                legislator_id INTEGER NOT NULL,
                vote_id INTEGER NOT NULL,
                vote_type INTEGER NOT NULL CHECK (vote_type IN (1, 2)),
                CONSTRAINT fk_legislator FOREIGN KEY (legislator_id) REFERENCES legislators_legislator(id) ON DELETE CASCADE,
                CONSTRAINT fk_vote FOREIGN KEY (vote_id) REFERENCES votes_vote(id) ON DELETE CASCADE
            );
        """)

def drop_vote_results_table(apps, schema_editor):
    """
    Drops the vote_results table if the migration is reversed.
    """
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS vote_results_vote_result;")

class Migration(migrations.Migration):

    dependencies = [
        ('legislators', '0001_create_legislators_table'),  # Ensure legislators exist first
        ('votes', '0001_create_votes_table'),  # Ensure votes exist first
    ]

    operations = [
        migrations.RunPython(create_vote_results_table, drop_vote_results_table),
    ]
