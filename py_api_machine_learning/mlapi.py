from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class ScoringItem(BaseModel):
  yearAtCompany: float
  employeeStatisfaction: float
  position: str
  salary: float


@app.post('/')
async def scoring_endpoint(item:ScoringItem):
  df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
  return df.to_dict()