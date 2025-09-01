FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: runtime image
FROM python:3.11-slim

WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY . .

# Non-root user (security best practice)
RUN useradd -m appuser
USER appuser

ENV PORT=8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]