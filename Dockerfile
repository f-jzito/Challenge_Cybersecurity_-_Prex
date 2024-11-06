# Base image with Python
FROM python:3.9-slim-buster

# Working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container's working directory
COPY . /app

# Expose the port used by the application (adjust if needed)
EXPOSE 8080

# Command to run the application (adjust according to your main file)
CMD ["python", "run.py"]