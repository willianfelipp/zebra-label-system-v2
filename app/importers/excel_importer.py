from pathlib import Path

import pandas as pd


class ExcelImporter:

    @staticmethod
    def read_excel(file_path):

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"Arquivo não encontrado: {file_path}"
            )

        df = pd.read_excel(file_path)

        return df