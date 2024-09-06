FROM python:3.12.5

COPY . .
RUN pip install -r requirements.txt

CMD ["fastapi", "dev", "main.py"]
