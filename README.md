# fastapi-explorer


doc ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS                   PORTS                    NAMES
9283d0de5aac   fastapi_docker-web   "uvicorn app.main:ap…"   8 minutes ago   Up 8 minutes             0.0.0.0:8000->8000/tcp   fastapi_docker-web-1
703644ce26c1   postgres:15-alpine   "docker-entrypoint.s…"   8 minutes ago   Up 8 minutes (healthy)   0.0.0.0:5432->5432/tcp   fastapi_docker-db-1

curl -X POST -H "Content-Type: application/json" -d '{"content":"Hello Docker!"}' http://localhost:8000/messages/

{"id":1,"content":"Hello Docker!"}%

curl http://localhost:8000/messages/

curl http://localhost:8000/messages/
[{"id":1,"content":"Hello Docker!"},{"id":2,"content":"Hello Again!"}]%