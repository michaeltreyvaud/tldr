FROM python:3.11
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY .env /code/src/.env
COPY ./src /code/src
CMD ["uvicorn", "src.app.app:app", "--host", "0.0.0.0", "--port", "3000"]
