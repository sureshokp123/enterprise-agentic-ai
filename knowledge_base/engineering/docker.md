# Docker Deployment Guidelines

## Purpose

Docker provides consistent environments across development, testing, and production.

---

## Dockerfile

Every application must contain a Dockerfile.

---

## Build Image

docker build -t app-name .

---

## Run Container

docker run -p 8000:8000 app-name

---

## Docker Compose

Use docker-compose for multi-container applications.

Example services:

Application

PostgreSQL

Redis

pgAdmin

---

## Best Practices

Use slim base images.

Avoid running as root user.

Minimize image size.

Use .dockerignore.

---

## Environment Variables

Store secrets using environment variables.

Never hardcode credentials.

---

## Health Checks

Applications should expose health endpoints.

Example:

GET /health

---

## Logging

Container logs should be written to stdout.

Use:

docker logs container-name