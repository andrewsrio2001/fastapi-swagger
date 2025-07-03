# Use official Python 3.10 slim base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY ./app ./app

# Expose both ports: 4082 and 80
EXPOSE 4082
EXPOSE 80

# Run the FastAPI app on both ports using two Uvicorn processes (optional)
# If you only want ONE port inside container to serve the app, use one CMD

# Default: run on 4082
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4082"]
