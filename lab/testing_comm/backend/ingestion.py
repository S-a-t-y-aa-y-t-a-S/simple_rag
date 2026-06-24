from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

@app.post(path='/ingestion/ingest')
async def gateway_func(
    file: UploadFile = File(...),
    upload_source: str = Form(...)
):
    
    contents = await file.read()

    return {
        'status': "success",
        "filename": file.filename,
        "bytes_processed": len(contents)
    }
