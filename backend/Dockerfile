# Use an official lightweight Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
RUN pip install --no-cache-dir -r ../requirements.txt

COPY . .

# Expose the API port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
