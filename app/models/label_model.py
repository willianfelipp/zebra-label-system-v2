class LabelModel:

    def __init__(
        self,
        material_code="",
        material_name="",
        quantity=0,
        unit="",
        barcode="",
        lot="",
        layout_name="default",
        copies=1,
        extra_data=None
    ):

        self.material_code = material_code
        self.material_name = material_name
        self.quantity = quantity
        self.unit = unit
        self.barcode = barcode
        self.lot = lot
        self.layout_name = layout_name
        self.copies = copies
        self.extra_data = extra_data or {}

    def to_dict(self):

        return {
            "material_code": self.material_code,
            "material_name": self.material_name,
            "quantity": self.quantity,
            "unit": self.unit,
            "barcode": self.barcode,
            "lot": self.lot,
            "layout_name": self.layout_name,
            "copies": self.copies,
            "extra_data": self.extra_data,
        }