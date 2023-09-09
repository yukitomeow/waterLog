# Use the ARG for dynamic Python version
ARG PYTHON_VERSION=3.8-slim
FROM python:${PYTHON_VERSION}

# Setting Python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies for psycopg2 and image processing libraries
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libtiff5-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /code

# Copy requirements first to leverage Docker cache
COPY requirements.txt /tmp/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# Cleanup
RUN apt-get autoremove -y && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the rest of the code
COPY . /code

# It's not recommended to set the SECRET_KEY like this. Consider other methods.
# ENV SECRET_KEY "NzgWkwDq9fQ2YnspRxHCXtXMtIlXsbDedD1maeP1TVLsMUHFcP"
RUN python manage.py collectstatic --noinput

# Expose port for the app
EXPOSE 8000

# Run command
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "waterLog.wsgi"]
