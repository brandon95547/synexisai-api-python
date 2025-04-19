from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from email_utils import send_email
# from other_script import some_function  # Optional: import your other Python logic

app = FastAPI()

# Allow frontend access (adjust origin in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use your domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/send-email")
async def email_endpoint(request: Request):
    try:
        data = await request.json()
        result = await send_email(data)
        return {"status": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
