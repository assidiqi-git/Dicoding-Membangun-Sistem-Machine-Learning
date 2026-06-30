import requests
import random

def make_prediction():
    url = "http://127.0.0.1:5001/invocations"
    # Format JSON split yang dikenali MLflow 2.x
    data = {
        "dataframe_split": {
            "columns": ["age", "bmi", "children", "sex_female", "sex_male", "smoker_no", "smoker_yes", "region_northeast", "region_northwest", "region_southeast", "region_southwest"],
            "data": [[
                random.uniform(18, 64),       # age
                random.uniform(15.0, 53.0),   # bmi
                float(random.randint(0, 3)),  # children
                1.0, 0.0,                     # sex_female, sex_male
                1.0, 0.0,                     # smoker_no, smoker_yes
                0.0, 1.0, 0.0, 0.0           # region_northeast, northwest, southeast, southwest
            ]]
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data)

    predicted_value = None
    if response.status_code == 200:
        result = response.json()
        # MLflow 2.x mengembalikan {"predictions": [...]}
        predicted_value = result.get("predictions", [None])[0]

    return response.status_code, predicted_value