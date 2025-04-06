from fastapi import FastAPI

app = FastAPI()

@app.get("/llm")
async def first_api():
    return {"message": "hello from Kana!"}

print("Success")
