import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path

# 1. Aktifkan autolog (Syarat mutlak untuk Kriteria 2 - 2 poin)
mlflow.sklearn.autolog()

def run_training():
    print("Memuat dataset...")
    # 2. Muat dataset yang sudah bersih
    # Pastikan path ini sesuai dengan struktur folder Anda
    base_path = Path(__file__).resolve().parent

    # Membuat path lengkap menuju file
    clean_path = base_path / "insurance_preprocessing" / "clean_data.csv"
    df = pd.read_csv(clean_path)
    
    # 3. Pisahkan fitur (X) dan target (y)
    # Target prediksi kita adalah kolom 'charges'
    X = df.drop("charges", axis=1) 
    y = df["charges"]

    X = X.astype(float)
    
    # Membagi data menjadi training (80%) dan testing (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Eksekusi eksperimen dengan MLflow
    # Kita berikan nama run agar mudah dicari di dashboard MLflow
    with mlflow.start_run(run_name="Basic_RandomForest_Regression"):
        print("Memulai pelatihan model...")
        
        # Menggunakan Regressor karena target berupa angka kontinu
        model = RandomForestRegressor(random_state=42)
        model.fit(X_train, y_train)
        
        mlflow.sklearn.log_model(model, "model")

        print("Pelatihan selesai! Metrik, parameter, dan artefak model telah dicatat otomatis oleh MLflow autolog.")

if __name__ == "__main__":
    run_training()