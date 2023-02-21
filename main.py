from src.repository.repository import Repository
from src.service.service import Service
from src.ui.ui import Ui

repo = Repository("sentences.txt")
serv = Service(repo)
ui = Ui(serv)
ui.start()
