import csv


class GetBillAnalyticsUseCase:
    def __init__(self, bill_repo):
        self.bill_repo = bill_repo


    def execute(self):
        return self.bill_repo.get_bill_with_supporter_and_opposer_count()


class ImportBillsFromCSVUseCase:
    def __init__(self, bill_repo):
        self.bill_repo = bill_repo


    def execute(self, csv_file):
        if isinstance(csv_file, str):
            decoded_file = csv_file.splitlines()
        else:
            decoded_file = csv_file.read().decode('utf-8').splitlines()

        csv_reader = csv.DictReader(decoded_file)

        bill_data = []
        for row in csv_reader:
            bill_data.append({'id': row['id'], 'title': row['title'], 'primary_sponsor': row['sponsor_id']})

        self.bill_repo.save_bulk(bill_data)

        return {'message': 'Bill CSV file uploaded successfully'}

