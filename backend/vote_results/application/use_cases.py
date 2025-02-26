import csv

class ImportVoteResultsUseCase:
    def __init__(self, votes_repo):
        self.votes_repo = votes_repo

    def execute(self, csv_file):
        if isinstance(csv_file, str):
            decoded_file = csv_file.splitlines()
        else:
            decoded_file = csv_file.read().decode('utf-8').splitlines()

        csv_reader = csv.DictReader(decoded_file)

        vote_results_data = []
        for row in csv_reader:
            vote_results_data.append({'id': row['id'], 'legislator_id': row['legislator_id'],
                               'vote_id': row['vote_id'], 'vote_type': row['vote_type']})

        self.votes_repo.save_bulk(vote_results_data[1:])

        return {'message': 'Vote Results CSV file uploaded successfully'}