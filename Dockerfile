# Multi-stage build for Python and Java

# Stage 1: Python base
FROM python:3.9-slim as python-base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy Python package
COPY python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY python/ .
RUN pip install --no-cache-dir -e .

# Stage 2: Java base
FROM openjdk:11-jdk-slim as java-base

WORKDIR /app

COPY java/pom.xml .
COPY java/src ./src

RUN apt-get update && apt-get install -y maven \
    && mvn clean compile \
    && apt-get remove -y maven \
    && rm -rf /var/lib/apt/lists/*

# Stage 3: Final image
FROM python:3.9-slim

WORKDIR /app

# Install Java runtime
RUN apt-get update && apt-get install -y \
    openjdk-11-jre-headless \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy Python from python-base
COPY --from=python-base /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=python-base /app/minecraft_server_utility ./minecraft_server_utility
COPY --from=python-base /app/examples ./examples

# Copy Java from java-base
COPY --from=java-base /app/target/classes ./java/classes
COPY --from=java-base /app/target/*.jar ./java/

# Create symbolic links
RUN ln -s /app/minecraft_server_utility /usr/local/lib/python3.9/site-packages/minecraft_server_utility

# Set environment variables
ENV PYTHONPATH=/app
ENV CLASSPATH=/app/java/classes:/app/java/*

# Create entrypoint script
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "from minecraft_server_utility import ServerPinger; print('Health check OK')"

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["python"]
