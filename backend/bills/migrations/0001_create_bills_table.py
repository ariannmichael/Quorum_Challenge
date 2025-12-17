from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('legislators', '0001_create_legislators_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('primary_sponsor', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bills_bill',
            },
        ),
    ]
