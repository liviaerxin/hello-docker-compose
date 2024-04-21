# Pull official base image
FROM python:3.10

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

CMD ["uvicorn", "server:app", "--host", "0.0.0.0"]