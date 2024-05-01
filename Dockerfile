FROM python:3.11-slim
MAINTAINER Muhammad Ahsan <muhammad.ahsan@gmail.com>

RUN pip install pipenv
RUN apt-get -q update && apt-get install -y --no-install-recommends gcc supervisor && rm -rf /var/lib/apt/lists/*

WORKDIR sentiment-sage

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile

COPY main.py .
COPY nltk_data ./nltk_data

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]