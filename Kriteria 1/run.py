import os
import pandas as pd
from preprocessing.automate_BagusAkbarAssidiqi import data_preprocessing
from pathlib import Path


if __name__ == "__main__":
    # Mencari direktori tempat file skrip ini disimpan
    base_path = Path(__file__).resolve().parent

    # Membuat path lengkap menuju file
    raw_path = base_path / "insurance_raw.csv"
    export_path = base_path / "preprocessing" / "export"

    os.makedirs(export_path, exist_ok=True)

    # Load data
    df = pd.read_csv(raw_path)
    data_preprocessing(df, export_path)