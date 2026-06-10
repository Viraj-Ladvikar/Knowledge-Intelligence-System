
# Use official Python 3.11 image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file first
COPY requirements.txt .

# Install all Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy complete project into container
COPY . .

# Expose Flask port
EXPOSE 8080

# Start Flask application
CMD ["python", "app/main.py"]
