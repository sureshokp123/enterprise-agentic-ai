# FastAPI Development Standards

## API Design

RESTful APIs should follow standard HTTP methods.

GET

POST

PUT

DELETE

PATCH

---

## Validation

Use Pydantic models for request validation.

Never trust raw client input.

---

## Response Models

Every API should define response models.

---

## Dependency Injection

Use Depends() for reusable dependencies.

---

## Error Responses

Return proper HTTP status codes.

200 Success

201 Created

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

500 Internal Server Error

---

## API Documentation

Swagger UI should always be enabled.

OpenAPI documentation should remain updated.

---

## Authentication

JWT Authentication is preferred.

OAuth2 may be used where required.

---

## Middleware

Common middleware:

CORS

Logging

Authentication

Request Tracking

---

## Project Structure

api/

services/

models/

database/

config/

utils/

---

## Best Practices

Keep business logic inside service layer.

API routes should remain lightweight.