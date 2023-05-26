# Python baseimage
FROM python:3.6

# Working directory
WORKDIR /usr/src/app

# Copy requirements to container
# COPY requirements.txt /usr/src/app/

# Install dependencies (--no-cache-dir -r requirements.txt)
RUN pip install

# Copy the rest of the application to container
COPY . /usr/src/app

# For Django
EXPOSE 8000
CMD ["python", "app.py", "manage.py", "runserver", "0.0.0.0:8000"]
