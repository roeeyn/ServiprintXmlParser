from os import getenv
from typing import List

import uvicorn
from fastapi import FastAPI, File, Response, UploadFile
from fastapi.responses import HTMLResponse

from src.csv_creation import create_csv_file
from src.xml_processing import create_csv_row_from_xml

port = getenv("PORT", 5000)
app = FastAPI()


@app.post("/upload-xmls/")
async def process_xmls(xml_files: List[UploadFile] = File(...)):
    processed_files = [create_csv_row_from_xml(xml_file) for xml_file in xml_files]
    csv_content = create_csv_file(processed_files)
    return Response(content=csv_content, media_type="text/csv")


@app.get("/")
async def main():
    content = """
<body>
<form action="/upload-xmls/" enctype="multipart/form-data" method="post">
<input name="xml_files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
