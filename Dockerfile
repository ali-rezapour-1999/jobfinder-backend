FROM python:3.12 AS builder

RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

RUN pip install 
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN chmod +x /app/entrypoint.prod.sh

CMD ["/app/entrypoint.prod.sh"]
