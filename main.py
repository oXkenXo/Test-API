from typing import Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI(
    title="AI Prediction API",
    description="API sederhana untuk pengecekan status server, pengambilan data dummy, "
    "dan prediksi label dari teks.",
    version="1.0.0",
)

DUMMY_DATA = [
    {"id": 1, "category": "electronics", "name": "Laptop"},
    {"id": 2, "category": "electronics", "name": "Smartphone"},
    {"id": 3, "category": "electronics", "name": "Headphone"},
    {"id": 4, "category": "furniture", "name": "Meja Belajar"},
    {"id": 5, "category": "furniture", "name": "Kursi Gaming"},
    {"id": 6, "category": "stationery", "name": "Buku Tulis"},
]


class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=500)
    threshold: float = Field(..., ge=0.0, le=1.0)

    model_config = {
        "json_schema_extra": {
            "example": {
                "text": "Aplikasi ini sangat membantu pekerjaan saya sehari-hari",
                "threshold": 0.7,
            }
        }
    }


class PredictResponse(BaseModel):
    label: str
    confidence: float
    input_text: str


@app.get("/health", tags=["System"], summary="Cek status server")
def health():
    return {"status": "ok"}


@app.get("/data", tags=["Data"], summary="Ambil daftar data dummy")
def get_data(
    category: Optional[str] = Query(None, description="Filter berdasarkan kategori"),
    limit: Optional[int] = Query(None, ge=1, description="Jumlah maksimal data"),
):
    result = DUMMY_DATA
    if category:
        result = [d for d in result if d["category"] == category]
    if limit is not None:
        result = result[:limit]
    return result


@app.post(
    "/predict",
    tags=["Prediction"],
    summary="Prediksi label dari teks",
    description="Endpoint ini digunakan untuk memprediksi label dari input teks. "
    "Hasil prediksi bersifat dummy dan dibandingkan dengan nilai threshold.",
    response_model=PredictResponse,
)
def predict(body: PredictRequest):
    confidence = 0.85
    label = "positif" if confidence >= body.threshold else "tidak yakin"
    return PredictResponse(label=label, confidence=confidence, input_text=body.text)