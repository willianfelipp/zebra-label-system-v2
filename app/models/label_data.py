from dataclasses import dataclass


@dataclass
class LabelData:

    material_code: str = ""
    description: str = ""
    quantity: str = ""
    lot: str = ""
    barcode: str = ""
    unit: str = ""
    weight: str = ""