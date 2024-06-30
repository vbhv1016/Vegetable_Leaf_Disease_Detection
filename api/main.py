from fastapi import FastAPI, UploadFile, File
import uvicorn
app=FastAPI()

@app.get("/ping")
async def ping():
    return "Tomato Leaf Diease Detection"

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    pass
    
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)