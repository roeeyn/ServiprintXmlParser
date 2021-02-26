from os import getenv
from typing import List

import uvicorn
from fastapi import FastAPI, File, Response, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.csv_creation import create_csv_file, fieldnames
from src.xml_processing import create_csv_row_from_xml

# Try to get the environment variable PORT, and if it doesn't exist it defaults to 5000
port = int(getenv("PORT", 5000))
app = FastAPI()

# Create an 'independent' routing for static files, such as CSS, JS, etc
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.post("/upload-xmls/")
async def process_xmls(xml_files: List[UploadFile] = File(...)):
    # Create a CSV row from each one of the XML files
    processed_files = [create_csv_row_from_xml(xml_file) for xml_file in xml_files]

    # Use this list of CSV rows to create the CSV file
    csv_content = create_csv_file(processed_files)

    # Return it with a special media type, so it can be downloaded
    return Response(content=csv_content, media_type="text/csv")


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(
        "files_form.html", {"request": request, "csv_columns": fieldnames}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, workers=3, proxy_headers=True)
