class GetLegislatorsUseCase:
  def __init__(self, legislator_repo):
    self.legislator_repo = legislator_repo
  

  def execute(self):
    return self.legislator_repo.get_all()