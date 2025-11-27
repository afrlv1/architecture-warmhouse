import random
from datetime import datetime
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/temperature")
def get_temperature(location: str = Query(...)):
    return {
        "value": round(random.uniform(-20, 35), 2),
        "status": "online",
    }


@app.get("/temperature/{sensor_id}")
def get_temperature_by_id(sensor_id: str):
    location = f"sensor-{sensor_id}"

    return {
        "value": round(random.uniform(-20, 35), 2),
        "status": "online",
    }
