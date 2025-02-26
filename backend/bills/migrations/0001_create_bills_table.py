from django.db import migrations, connection

def create_bills_table(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE bills_bill (
                id SERIAL PRIMARY KEY,
                title VARCHAR(500) NOT NULL,
                primary_sponsor INTEGER
            );
        """)

def drop_bills_table(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS bills_bill;")

class Migration(migrations.Migration):

    dependencies = [
        ('legislators', '0001_create_legislators_table'),
    ]

    operations = [
        migrations.RunPython(create_bills_table, drop_bills_table),
    ]
