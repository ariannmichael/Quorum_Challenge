from django.db import migrations, connection

def create_legislators_table(apps, schema_editor):
    """
    Custom migration to create the legislators table using raw SQL.
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE legislators_legislator (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            );
        """)

def drop_legislators_table(apps, schema_editor):
    """
    Rollback function to drop the legislators table if needed.
    """
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS legislators_legislator;")

class Migration(migrations.Migration):

    dependencies = []  # No dependencies because we are not using Django ORM

    operations = [
        migrations.RunPython(create_legislators_table, drop_legislators_table),
    ]
