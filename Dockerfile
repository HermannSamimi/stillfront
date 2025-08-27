# ---- base image ----
    FROM python:3.11-slim

    # Ensure stdout/stderr are unbuffered
    ENV PYTHONDONTWRITEBYTECODE=1 \
        PYTHONUNBUFFERED=1 \
        PIP_NO_CACHE_DIR=1
    
    # Create a non-root user
    RUN useradd -m appuser
    
    # Set workdir
    WORKDIR /app
    
    # System deps (only if you need them later; safe to keep minimalist)
    # RUN apt-get update && apt-get install -y --no-install-recommends \
    #     build-essential && \
    #     rm -rf /var/lib/apt/lists/*
    
    # Copy only dependency file first (leverages Docker layer cache)
    COPY requirements.txt .
    
    # Install Python deps
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy the app
    COPY . .
    
    # Switch to non-root
    USER appuser
    
    # Expose FastAPI default port
    EXPOSE 8000
    
    # Start the API
    CMD ["uvicorn", "service.app:app", "--host", "0.0.0.0", "--port", "8000"]