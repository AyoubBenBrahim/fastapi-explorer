# FastAPI Explorer

A FastAPI application with PostgreSQL database and Adminer for database management.

## Services

When running, you'll see these containers:
```bash
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS                    PORTS                    NAMES
xxxxxxxx       fastapi_docker-web   "uvicorn app.main:ap…"   x minutes ago    Up x minutes              0.0.0.0:8000->8000/tcp   fastapi_docker-web-1
xxxxxxxx       postgres:15-alpine   "docker-entrypoint.s…"   x minutes ago    Up x minutes (healthy)    0.0.0.0:5432->5432/tcp   fastapi_docker-db-1
xxxxxxxx       adminer              "entrypoint.sh php -…"   x minutes ago    Up x minutes              0.0.0.0:8080->8080/tcp   fastapi_docker-adminer-1
```

## API Examples

### Create a message
```bash

curl -X POST -H "Content-Type: application/json" -d '{"content":"Hello Again!"}' http://localhost:8000/messages/

{"id":2,"content":"Hello Again!"}
```

### Get all messages
```bash

curl http://localhost:8000/messages/ 

[{"id":1,"content":"Hello Docker!"},{"id":2,"content":"Hello Again!"}]%

```

interactive API documentation : Swagger 

http://localhost:8000/docs