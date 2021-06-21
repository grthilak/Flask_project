# Base image
From python:3.8.0-buster AS builder

# Make a directory for app
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY /app .

FROM python:3.8-alpine
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY --from=builder /app .

# Run application
CMD ["python", "index.py"]
