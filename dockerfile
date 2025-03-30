# etapa 1: construir el frontend
FROM node:18.12.1-buster-slim AS builder
WORKDIR /frontend
COPY ./frontend .
RUN npm install
RUN npm run build

# etapa 2: construir el backend + servir el frontend
FROM python:3.12-slim-bookworm

# mejor manejo de logs
ENV PYTHONUNBUFFERED=1

# crear y posicionarse en carpeta del backend
WORKDIR /backend

# instalar dependencias
COPY ./backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copiar código del backend
COPY ./backend .

# copiar el frontend compilado dentro del backend como "static"
COPY --from=builder /frontend/dist ./static

# definir punto de entrada
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
