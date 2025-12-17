from django.db import models
from legislators.models import Legislator
from votes.models import Vote


class VoteResult(models.Model):
    id = models.IntegerField(primary_key=True) # type: ignore
    legislator = models.ForeignKey(Legislator, on_delete=models.CASCADE, db_column='legislator_id') # type: ignore
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, db_column='vote_id') # type: ignore
    vote_type = models.IntegerField() # type: ignore # 1 for yea, 2 for nay

    class Meta:
        db_table = 'vote_results_vote_result'

