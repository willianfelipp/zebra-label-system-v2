from app.models.label_data import LabelData


class DataNormalizer:

    @staticmethod
    def normalize(df):

        normalized_data = []

        for _, row in df.iterrows():

            label = LabelData(
                material_code=str(row.iloc[0]),
                quantity=str(row.iloc[1]),
                description=str(row.iloc[2])
                if len(row) > 2
                else "",
            )

            normalized_data.append(label)

        return normalized_data