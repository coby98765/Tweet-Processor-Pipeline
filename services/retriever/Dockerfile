# --- Stage 1: Build dependencies in a virtual environment ---
FROM python:3.12-slim AS builder

WORKDIR /app
ARG SERVICE_DIR=services/retriever


# Create a virtual environment to isolate dependencies
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy and install dependencies
COPY ${SERVICE_DIR}/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# --- Stage 2: Build the final, lightweight image ---
FROM python:3.12-slim

WORKDIR /app

# Copy the virtual environment with installed dependencies from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Set environment variables to use the virtual environment
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#Declare ENV var's
ENV DB_NAME=""
ENV DB_COLL=""
ENV DB_USER=""
ENV DB_PASS=""
ENV DB_HOST=""
ENV KAFKA_HOST=""

# Copy the application source code
ENV PYTHONPATH=/app
ARG SERVICE_DIR=services/retriever
COPY services ./services

# Set working dir to the specific service and run
WORKDIR /app/${SERVICE_DIR}

CMD ["python", "main.py"]