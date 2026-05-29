class LayoutModel:

    def __init__(
        self,
        name,
        width_mm,
        height_mm,
        fields
    ):

        self.name = name
        self.width_mm = width_mm
        self.height_mm = height_mm
        self.fields = fields

    def to_dict(self):

        return {
            "name": self.name,
            "width_mm": self.width_mm,
            "height_mm": self.height_mm,
            "fields": self.fields,
        }