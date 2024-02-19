from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from src.routes import router_endpoints, router_contacts, auth

app = FastAPI()

app.include_router(router_endpoints.router, prefix="/contacts")
app.include_router(router_contacts.router, prefix="/contacts")
app.include_router(auth.router, prefix="")

origins = ["http://localhost:8000", "https://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)