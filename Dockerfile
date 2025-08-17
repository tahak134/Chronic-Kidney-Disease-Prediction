# Use a slim Python base
FROM python:3.11-slim

# Prevent Python from writing .pyc files and ensure unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# (xgboost runtime needs libgomp)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
 && rm -rf /var/lib/apt/lists/*

# Workdir
WORKDIR /app

# Install Python deps first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code + model
COPY api/ api/
COPY models/ models/

# Expose HTTP port
EXPOSE 80

# Run the FastAPI app with uvicorn
# (api.main:app = folder.module:FastAPI_instance)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]
