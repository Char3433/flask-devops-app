# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
