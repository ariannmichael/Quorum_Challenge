import csv


class GetBillAnalyticsUseCase:
    def __init__(self, bill_repo):
        self.bill_repo = bill_repo


    def execute(self):
        bills = self.bill_repo.get_bill_with_supporter_and_opposer_count()


class ImportBillsFromCSVUseCase:
    def __init__(self, bill_repo):
        self.bill_repo = bill_repo


    def execute(self, csv_file):
        decode_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.reader(decode_file)

        bill_data = []
        for row in csv_reader:
            bill_data.append({'id': row[0], 'title': row[1], 'primary_sponsor': row[2]})
            
        
        self.bill_repo.save_bulk(bill_data[1:])

        return {'message': 'Bill CSV file uploaded successfully'}

