from .database import DatabaseManager
from .cruds.UserCRUD import UserCRUD

class Crud(UserCRUD):
    def __init__(self, db_manager: DatabaseManager) -> None:
	    self.db_manager = db_manager
