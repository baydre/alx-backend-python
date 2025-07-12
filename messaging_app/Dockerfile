# Use official Python image
FROM python:3.10

# Set work directory
WORKDIR /messaging_app

# Copy requirements and install
COPY requirements.txt .
RUN apt-get update && apt-get install -y default-libmysqlclient-dev pkg-config && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

# Copy project files
COPY . /messaging_app/

# Expose Django's default port
EXPOSE 8000

# Launch the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
