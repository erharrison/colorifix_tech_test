import pandas as pd


def create_data(data):
    df = pd.DataFrame(data)
    return df


def export_data(dataframe_to_export,
                export_path,
                file_type="csv"):
    if file_type == "csv":
        dataframe_to_export.to_csv(export_path, index=False)
