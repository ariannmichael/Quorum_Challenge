from celery import shared_task
from legislators.infrastructure.db.repositories import LegislatorRepository
from legislators.application.use_cases import ImportLegislatorsFromCSVUseCase

@shared_task
def import_legislators_from_csv_task(csv_file_data):
    repo = LegislatorRepository()
    use_case = ImportLegislatorsFromCSVUseCase(repo)
    use_case.execute(csv_file_data)
    return "Legislators imported successfully"