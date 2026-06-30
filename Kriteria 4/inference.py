import requests
import random

def make_prediction():
    url = "http://127.0.0.1:5001/invocations"
    # Format JSON split yang dikenali MLflow 2.x
    data = {
        "dataframe_split": {
            "columns": ["age", "bmi", "children", "sex_female", "sex_male", "smoker_no", "smoker_yes", "region_northeast", "region_northwest", "region_southeast", "region_southwest"],
            "data": [[
                random.random(), random.random(), float(random.randint(0, 3)), 
                1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0
            ]]
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data)
    return response.status_code