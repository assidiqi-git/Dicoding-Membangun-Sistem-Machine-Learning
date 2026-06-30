import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def data_preprocessing(raw_df, export_path):
    # 1. Load Data
    df = raw_df
    
    # Menghapus atau Menangani Data Kosong (Missing Values)
    df.dropna()
    
    # Menghapus Data Duplikat
    df.drop_duplicates(inplace = True)
    
    # Normalisasi atau Standarisasi Fitur
    categorical_cols = df.select_dtypes(include=['object', 'string']).columns
    numerical_cols = df.select_dtypes(include=['number']).columns
    target_col = 'charges'
    numerical_cols = numerical_cols.drop(target_col)
    scaler = MinMaxScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Deteksi dan Penanganan Outlier
    for feature in numerical_cols:
        Q1 = df[feature].quantile(0.25)
        Q3 = df[feature].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[feature] >= lower_bound) & (df[feature] <= upper_bound)]
    
    # Encoding Data Kategorikal
    df = pd.get_dummies(df, columns=categorical_cols,dtype=int)

    df.to_csv(export_path / "clean_data.csv", index=False)

    return df

# if __name__ == "__main__":
#     path_dataset = "../insurance_raw.csv" 
#     clean_data = data_preprocessing(path_dataset)
#     print("Preprocessing selesai. Data siap dilatih!")
    # clean_data.to_csv("data_clean.csv", index=False)