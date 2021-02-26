FROM python:3.9-buster
EXPOSE $PORT
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD uvicorn main:app --proxy-headers --host 0.0.0.0 --port $PORT --workers 3
