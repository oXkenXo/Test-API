# AI Prediction API

API sederhana dengan FastAPI untuk pengecekan status server, pengambilan data dummy, dan prediksi label dari teks.

## Cara menjalankan

```
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

Dokumentasi Swagger tersedia di `http://127.0.0.1:8001/docs`.

## Endpoint

| Method | Path | Keterangan |
| --- | --- | --- |
| GET | /health | Cek status server |
| GET | /data | Ambil data dummy, query opsional `category` dan `limit` |
| POST | /predict | Prediksi label dari teks (`text` 1-500 karakter, `threshold` 0.0-1.0) |

## Hasil pengujian

### 1. GET /health

![/health di browser](screenshots/01-health-browser.png)

![/health di Swagger](screenshots/02-health-swagger.png)

### 2. GET /data

Tanpa parameter:

![/data tanpa parameter](screenshots/03-data-semua.png)

Dengan `category=electronics&limit=2`:

![/data dengan filter](screenshots/04-data-filter.png)

Dengan `limit=abcsds` (input tidak valid, kode 422):

![/data input tidak valid](screenshots/05-data-invalid.png)

### 3. POST /predict

Body valid (kode 200):

![/predict body valid](screenshots/06-predict-valid.png)

Body tidak valid (kode 422):

![/predict body tidak valid](screenshots/07-predict-invalid.png)

### 4. Dokumentasi Swagger

![Swagger UI](screenshots/08-swagger-docs.png)
