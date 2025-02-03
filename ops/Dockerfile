FROM python:3.10

RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /car_service

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

ENV PYTHONPATH="/car_service/src"

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
