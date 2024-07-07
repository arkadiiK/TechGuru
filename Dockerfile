# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl

# Copy the requirements file into the container
COPY requirements.txt /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./entrypoints/entrypoint.sh /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./entrypoints/django.sh /django
RUN sed -i 's/\r$//g' /django
RUN chmod +x /django


# Copy the current directory contents into the container
COPY . .

# Expose port 8000
EXPOSE 8000

ENTRYPOINT ["/entrypoint"]
