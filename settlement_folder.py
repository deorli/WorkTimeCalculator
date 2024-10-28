import os
import datetime
from icecream import ic
from config import ANNUAL_SETTLEMENT_DATE, CURRENT_DATE, TODAY

class SettlementFolder:
    def __init__(self, path: str = "", folder_name: str = ""):
        self._settlement_folder_name: str = folder_name
        self._settlement_path: str = path
        self.create_folder_name()

    @property
    def folder_name(self) -> str:
        return self._settlement_folder_name

    @property
    def folder_exist(self) -> bool:
        return os.path.exists(self.full_path)

    @property
    def path(self) -> str:
        return self._settlement_path

    @path.setter
    def path(self, new_path: str) -> None:
        if isinstance(new_path, str):
            self._settlement_path = new_path
        else:
            raise ValueError("Path must be a string")

    @property
    def full_path(self) -> str:
        if self._settlement_path:
            return os.path.join(self._settlement_path, self._settlement_folder_name)
        return self._settlement_folder_name

    def create_folder_name(self) -> None:
        if not self._settlement_folder_name:
            if self._is_annual_settlement():
                self._settlement_folder_name = f"Settlement_{CURRENT_DATE.year}"
            else:
                self._settlement_folder_name = self._generate_settlement_name()

    def _is_annual_settlement(self) -> bool:
        return ANNUAL_SETTLEMENT_DATE in [
            datetime.datetime(CURRENT_DATE.year, 1, 1),
            datetime.datetime(CURRENT_DATE.year, 12, 31)
        ]

    def _generate_settlement_name(self) -> str:
        if TODAY < ANNUAL_SETTLEMENT_DATE:
            return f"Settlement_{CURRENT_DATE.year - 1}-{CURRENT_DATE.year}"
        return f"Settlement_{CURRENT_DATE.year}-{CURRENT_DATE.year + 1}"

    def create_folder(self) -> None:
        try:
            if not os.path.exists(self.full_path):
                os.mkdir(self.full_path)
                print(f"Folder '{self.full_path}' was successfully created.")
            else:
                print(f"Folder '{self.full_path}' already exists.")
        except Exception as e:
            print(f"An error occurred while creating folder '{self.full_path}': {e}")
            raise

if __name__ == "__main__":
    settlement_folder = SettlementFolder()
    settlement_folder.create_folder()
