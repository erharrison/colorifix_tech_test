import pandas as pd


def create_data(data):
    df = pd.DataFrame(data)
    return df


def export_data(data_to_export,
                export_path,
                file_type="csv",
                sep="\t",
                encoding="utf-8"):
    if