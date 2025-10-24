# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY stock_pipeline.py .

# Create directory for output
RUN mkdir -p stock_data

# Set environment variable for API key (will be passed at runtime)
ENV ALPHA_VANTAGE_API_KEY=""

# Run the pipeline
CMD ["python", "stock_pipeline.py"]