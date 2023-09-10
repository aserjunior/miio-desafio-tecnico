# Use the Dockerfile located in the same directory as requirements.txt
FROM python:3.11.4-alpine

# Install PostgreSQL development libraries
RUN apk add --no-cache postgresql-dev musl-dev

# Set the working directory within the container
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements.txt file from your local directory into the container
COPY requirements.txt /usr/src/app/requirements.txt

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the entrypoint.sh script into the container
COPY entrypoint.sh /usr/src/app/entrypoint.sh

# Copy the rest of your Django project files into the container
COPY . /usr/src/app/

# Make manage.py executable
RUN chmod +x manage.py

# Set the entrypoint for the container
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
