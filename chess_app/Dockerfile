# Use a slim Python image
FROM python:3.11-slim

# Install system dependencies required for Tkinter (GUI)
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
# Copying src directory to /app/src
COPY src/ ./src/

# Command to run the application with virtual X11 display
CMD ["xvfb-run", "-a", "python", "src/main.py"]
