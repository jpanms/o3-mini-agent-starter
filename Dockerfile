 # Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY ./src /app

# Expose port for FastAPI
EXPOSE 8000

# Start the app
CMD ["uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8000"]
