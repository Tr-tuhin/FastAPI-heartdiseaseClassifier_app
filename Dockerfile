# Dockerfile

# 1. Use an official Python base image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy application code and model
COPY ./app ./app
COPY ./model ./model

# 5. Expose the port
EXPOSE 8000

# 6. Run FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
