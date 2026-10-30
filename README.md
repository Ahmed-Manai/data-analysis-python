# data-analysis-python

A minimal Flask app that streams chart data to the browser with Server-Sent Events and renders it as a Chart.js line chart.

## Features

- `GET /` serves a single page (Bootstrap 4 + Chart.js 2) with a "Data Charts with Flask" line chart
- `GET /chart-data` is a Server-Sent Events endpoint (`text/event-stream`) the page subscribes to with `EventSource`
- The page appends each received `{time, value}` message to the chart and keeps the last 20 points
- Runs locally with pip or Poetry, or in Docker via Docker Compose

> Current state: `/chart-data` emits one fixed sample message, `{"time": [1, 2, 3, 4, 5], "value": [6, 7, 8, 9, 10]}`, and then closes the stream (the browser reconnects automatically). The page expects a single number per field, so the sample payload does not plot as a proper series yet.

## Tech stack

- Python, Flask 2
- Chart.js 2.8, Bootstrap 4.3 and jQuery 3.4 (loaded from cdnjs)
- Poetry (dependency management), Docker / Docker Compose

## Project structure

```
.
├── application.py        # Flask app: "/" and "/chart-data" (SSE)
├── templates/index.html  # Chart page (EventSource + Chart.js)
├── requirements.txt      # Pinned pip requirements (exported from Poetry)
├── pyproject.toml        # Poetry project definition
├── Makefile              # `make requirements.txt` re-exports requirements from Poetry
├── Dockerfile            # python:3.8 image, installs deps with Poetry
└── docker-compose.yml    # Runs the app on host port 5010
```

## Prerequisites

- Python 3.8+ (tested with 3.11), or
- Docker with Docker Compose

An internet connection is needed in the browser, since the front-end libraries load from a CDN.

## Run locally (pip)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python application.py
```

Open http://localhost:5000.

The app runs Flask's development server with `debug=True` on `0.0.0.0:5000`; do not expose it publicly.

## Run locally (Poetry)

```bash
poetry install
poetry run python application.py
```

## Run with Docker

```bash
docker compose up --build
```

Open http://localhost:5010 (the container listens on 5000; Compose maps it to host port 5010). The project folder is mounted into the container, so code edits are picked up by Flask's reloader.

## Regenerating requirements.txt

```bash
make requirements.txt
```

This runs `poetry export` (on Poetry 2.x the `poetry-plugin-export` plugin is required).

## Configuration

There are no environment variables or configuration files; host, port and debug mode are set in `application.py`.
