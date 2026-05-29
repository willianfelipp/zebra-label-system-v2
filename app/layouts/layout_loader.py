import json
from pathlib import Path


class LayoutLoader:

    @staticmethod
    def load(layout_name="default"):

        layout_path = (
            Path("layouts")
            / f"{layout_name}.json"
        )

        if not layout_path.exists():
            raise FileNotFoundError(
                f"Layout não encontrado: {layout_path}"
            )

        with open(
            layout_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)