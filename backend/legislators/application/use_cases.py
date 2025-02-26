import csv


class GetLegislatorVoteStatsUseCase:
  def __init__(self, legislator_repo):
    self.legislator_repo = legislator_repo
  

  def execute(self):
    return self.legislator_repo.get_legislators_with_vote_counts()


class ImportLegislatorsFromCSVUseCase:
  def __init__(self, legislator_repo):
    self.legislator_repo = legislator_repo


  def execute(self, csv_file):
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    csv_reader = csv.DictReader(decoded_file)

    legislators_data = []
    for row in csv_reader:
      legislators_data.append({'id': row['id'], 'name': row['name']})

    self.legislator_repo.save_bulk(legislators_data)

    return {'message': 'Legislator CSV file uploaded successfully'}