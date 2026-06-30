from prometheus_client import start_http_server, Counter, Summary
import time
from inference import make_prediction

# Mendefinisikan 3 Metrik
PREDICTION_TOTAL = Counter('model_predictions_total', 'Total prediksi yang dilakukan')
PREDICTION_LATENCY = Summary('model_prediction_latency_seconds', 'Waktu latensi prediksi dalam detik')
PREDICTION_ERRORS = Counter('model_errors_total', 'Total prediksi gagal')

def run_exporter():
    # Menjalankan exporter di port 8000
    start_http_server(8000)
    print("Prometheus exporter berjalan di port 8000...")
    
    while True:
        start_time = time.time()
        try:
            status = make_prediction()
            if status == 200:
                PREDICTION_TOTAL.inc()
            else:
                PREDICTION_ERRORS.inc()
        except Exception:
            PREDICTION_ERRORS.inc()
        
        # Mencatat latensi
        PREDICTION_LATENCY.observe(time.time() - start_time)
        time.sleep(2) # Hit endpoint setiap 2 detik

if __name__ == '__main__':
    run_exporter()