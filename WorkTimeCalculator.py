from icecream import ic
from config import *

class SettlementFolder(object):
    def __init__(self, settlement_path: str = ""):
        self._settlement_folder_name: str = ""
        self._settlement_folder_exist: bool = False
        self._settlement_path: str = settlement_path

        self.create_folder_name()

    @property
    def folder_name(self):
        return self._settlement_folder_name
    
    @property
    def foldel_exist(self):
        return self._settlement_path
    
    @property
    def path(self):
        return self._settlement_path
    
    @path.setter
    def path(self, path):
        assert(type(path) is str)
        self._settlement_path = path
    
    def create_folder_name(self) -> None:
        if self._settlement_folder_name == "":
            self._settlement_folder_name = ""
        
        if ANNUAL_SETTLEMENT_DATE == datetime.datetime(CURRENT_DATE.year, 1, 1) or ANNUAL_SETTLEMENT_DATE == datetime.datetime(CURRENT_DATE.year, 12, 31):
            self._settlement_folder_name =  f"Settlement_{CURRENT_DATE.year}"
        else:
            if TODAY < ANNUAL_SETTLEMENT_DATE:
                self._settlement_folder_name =  f"Settlement_{CURRENT_DATE.year - 1}-{CURRENT_DATE.year}"

            if TODAY >= ANNUAL_SETTLEMENT_DATE:
                self._settlement_folder_name =  f"Settlement_{CURRENT_DATE.year}-{CURRENT_DATE.year + 1}"
        
    def settlement_folder_exit(self) -> bool:
        if self._settlement_path == "":
            return os.path.exists(self._settlement_folder_name)
        else:
            return os.path.exists(os.path.join(self._settlement_path, self._settlement_folder_name))

    def create_folder(self) -> None:
        try:
            if self._settlement_path == "":
                os.mkdir(self._settlement_folder_name)
            else:
                os.mkdir(os.path.join(self._settlement_path, self._settlement_folder_name))
            print(f"Folder '{self._settlement_folder_name}' został pomyślnie utworzony.")
        except FileExistsError:
            print(f"Folder '{self._settlement_folder_name}' już istnieje.")
        except Exception as e:
            print(f"Wystąpił błąd podczas tworzenia folderu '{self._settlement_folder_name}': {e}")
            raise

if __name__ == "__main__":
    settlement_folder = SettlementFolder()
    settlement_folder.create_folder()


