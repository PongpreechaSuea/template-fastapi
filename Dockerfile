FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libjpeg-dev \
    libmagic-dev \
    libpng-dev \
    libxml2-dev \
    libxslt-dev && \
    rm -rf /var/lib/apt/lists/* && \

    groupadd -r appuser && \
    useradd -r -g appuser -s /bin/bash -d /home/appuser appuser && \
    mkdir -p /home/appuser && \
    chown -R appuser:appuser /home/appuser

WORKDIR /workspace
RUN mkdir -p /workspace && chown -R appuser:appuser /workspace

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="/workspace"

COPY --chown=root:root --chmod=0444 ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=root:root logging_config.yaml .
COPY --chown=root:root ./app .

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "./logging_config.yaml"]
