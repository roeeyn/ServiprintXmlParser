from os import getenv
from typing import List

import uvicorn
from fastapi import FastAPI, File, Response, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.csv_creation import create_csv_file, fieldnames
from src.xml_processing import create_csv_row_from_xml

port = getenv("PORT", 5000)
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.post("/upload-xmls/")
async def process_xmls(xml_files: List[UploadFile] = File(...)):
    processed_files = [create_csv_row_from_xml(xml_file) for xml_file in xml_files]
    csv_content = create_csv_file(processed_files)
    return Response(content=csv_content, media_type="text/csv")


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "csv_columns": fieldnames}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
