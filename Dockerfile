# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=TechGuru.settings

# Set work directory
WORKDIR /TechGuru

# Install dependencies
COPY requirements.txt /TechGuru/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to the container
COPY . /TechGuru/
