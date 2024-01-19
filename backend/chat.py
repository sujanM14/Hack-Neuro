from langchain.sql_database import SQLDatabase

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from pydantic import BaseModel
from typing import Any
import os




app = FastAPI()

# Define the allowed origins (replace with your specific domain)
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://0.0.0.0",
]

# Enable CORS with the specified origins and allowed headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  # Specify the headers you want to allow here
)

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def handle_query(request_data: QueryRequest) -> Any:
    query = request_data.query
    print(query)
    result = db_agent.run(query)
    print(result)
    return {"result": result}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("chat:app", host="127.0.0.1", port=8000, reload=True)
