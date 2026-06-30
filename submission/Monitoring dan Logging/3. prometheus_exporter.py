from prometheus_client import start_http_server, Counter, Summary, Gauge
import time
from inference import make_prediction

# Mendefinisikan Metrik Monitoring
# Metrik 1: Total prediksi yang berhasil
PREDICTION_TOTAL = Counter(
    'model_predictions_total',
    'Total prediksi yang berhasil dilakukan'
)

# Metrik 2: Latensi prediksi (dalam detik)
PREDICTION_LATENCY = Summary(
    'model_prediction_latency_seconds',
    'Waktu latensi prediksi dalam detik'
)

# Metrik 3: Total prediksi yang gagal (error)
PREDICTION_ERRORS = Counter(
    'model_errors_total',
    'Total prediksi yang gagal'
)

# Metrik 4: Nilai prediksi terakhir (biaya asuransi)
PREDICTION_VALUE = Gauge(
    'model_prediction_value',
    'Nilai prediksi biaya asuransi terakhir (dalam USD)'
)

def run_exporter():
    # Menjalankan HTTP server exporter di port 8000
    start_http_server(8000)
    print("Prometheus exporter berjalan di port 8000...")
    print("Akses metrics di: http://localhost:8000/metrics")

    while True:
        start_time = time.time()
        try:
            status, predicted_value = make_prediction()
            if status == 200:
                PREDICTION_TOTAL.inc()
                if predicted_value is not None:
                    PREDICTION_VALUE.set(predicted_value)
            else:
                PREDICTION_ERRORS.inc()
        except Exception as e:
            print(f"Error saat prediksi: {e}")
            PREDICTION_ERRORS.inc()

        # Mencatat latensi setiap iterasi
        elapsed = time.time() - start_time
        PREDICTION_LATENCY.observe(elapsed)

        time.sleep(2)  # Hit endpoint setiap 2 detik

if __name__ == '__main__':
    run_exporter()