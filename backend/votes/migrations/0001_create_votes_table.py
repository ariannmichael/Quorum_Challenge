from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bills', '0001_create_bills_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('bill', models.ForeignKey(db_column='bill_id', on_delete=django.db.models.deletion.CASCADE, to='bills.bill')),
            ],
            options={
                'db_table': 'votes_vote',
            },
        ),
    ]
