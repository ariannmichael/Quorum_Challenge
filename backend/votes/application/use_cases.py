import csv

class ImportVotesUseCase:
    def __init__(self, votes_repo):
        self.votes_repo = votes_repo

    def execute(self, csv_file):
        if isinstance(csv_file, str):
            decoded_file = csv_file.splitlines()
        else:
            decoded_file = csv_file.read().decode('utf-8').splitlines()

        csv_reader = csv.DictReader(decoded_file)

        votes_data = []
        for row in csv_reader:
            votes_data.append({'id': row['id'], 'bill_id': row['bill_id']})

        self.votes_repo.save_bulk(votes_data[1:])

        return {'message': 'Votes CSV file uploaded successfully'}