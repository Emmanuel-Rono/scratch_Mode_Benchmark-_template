FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /workspace

COPY pyproject.toml ./
COPY benchmark_core/ ./benchmark_core/
RUN python -m pip install .

COPY scripts/ ./scripts/
COPY task_template/ ./task_template/
COPY example/ ./example/

CMD ["python", "scripts/self_test.py"]
