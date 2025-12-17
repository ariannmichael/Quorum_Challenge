from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('legislators', '0001_create_legislators_table'),
        ('votes', '0001_create_votes_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteResult',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('vote_type', models.IntegerField()),
                ('legislator', models.ForeignKey(db_column='legislator_id', on_delete=django.db.models.deletion.CASCADE, to='legislators.legislator')),
                ('vote', models.ForeignKey(db_column='vote_id', on_delete=django.db.models.deletion.CASCADE, to='votes.vote')),
            ],
            options={
                'db_table': 'vote_results_vote_result',
            },
        ),
    ]
