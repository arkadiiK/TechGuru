# Use the official Python image as the base image
FROM python
# Set the working directory inside the container
WORKDIR TechGuru
# Copy the requirements.txt file inside the container
COPY requirements.txt ./
# Install the dependencies described in the requirements.txt file
RUN pip install -r requirements.txt