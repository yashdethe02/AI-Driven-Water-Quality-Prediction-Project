# Backend Stage
FROM python:3.9-slim as backend
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .
CMD ["python", "app.py"]

# Frontend Stage
FROM node:14 as frontend
WORKDIR /app
COPY frontend/package.json .
RUN npm install
COPY frontend/ .
RUN npm run build

# Final Stage
FROM nginx:alpine
COPY --from=frontend /app/build /usr/share/nginx/html
COPY --from=backend /app /backend
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]