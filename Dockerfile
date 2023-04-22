FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY ./app /app

RUN pip install --upgrade pip && \
    pip install fastapi[all] && \
    pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]