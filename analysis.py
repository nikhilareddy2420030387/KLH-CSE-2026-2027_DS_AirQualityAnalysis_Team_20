import pandas as pd
import numpy as np

POLLUTANTS = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]


def load_data(file):
    df = pd.read_csv(file)

    required_columns = ["City", "Date", "AQI"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Required column missing: {col}")

    return df


def clean_data(df):
    data = df.copy()

    data["Date"] = pd.to_datetime(
        data["Date"], errors="coerce"
    )

    data["AQI"] = pd.to_numeric(
        data["AQI"], errors="coerce"
    )

    for col in POLLUTANTS:
        if col in data.columns:
            data[col] = pd.to_numeric(
                data[col], errors="coerce"
            )

    data.drop_duplicates(inplace=True)

    data.dropna(
        subset=["City", "Date"],
        inplace=True
    )

    for col in POLLUTANTS:
        if col in data.columns:
            if data[col].notna().any():
                data[col] = data[col].fillna(
                    data[col].median()
                )

    data["AQI_Category"] = data["AQI"].apply(
        classify_aqi
    )

    return data


def classify_aqi(value):

    if pd.isna(value):
        return "Unknown"

    if value <= 50:
        return "Good"

    elif value <= 100:
        return "Satisfactory"

    elif value <= 200:
        return "Moderate"

    elif value <= 300:
        return "Poor"

    elif value <= 400:
        return "Very Poor"

    else:
        return "Severe"


def get_pollutants(df):

    return [
        col for col in POLLUTANTS
        if col in df.columns
    ]