# api-gateway/Dockerfile

FROM python:3.9-slim

# Create non-root user
RUN useradd -m appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app
USER appuser
WORKDIR /app

RUN echo PATH
ENV PATH="/home/appuser/.local/bin:${PATH}"
RUN echo $PATH

# Install dependencies
COPY --chown=appuser:appuser ../infra/central_requirements.txt .
RUN pip install --no-cache-dir -r central_requirements.txt

# Copy application code
COPY --chown=appuser:appuser app .

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
