FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# ADD .python-version /app
ADD pyproject.toml /app
ADD uv.lock /app

WORKDIR /app
RUN uv sync --locked

ADD main.py /app
ADD /api /app/api

CMD ["uv", "run", "-m", "fastapi", "run", "main.py"]
