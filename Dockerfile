FROM python:3.13.5-slim

RUN mkdir "code"
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py

EXPOSE 80
CMD ["fastapi", "run", "/code/main.py", "--port", "80"]
