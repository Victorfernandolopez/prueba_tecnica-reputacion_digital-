# Visualización de Datos con FastAPI, Svelte y eCharts

Este proyecto es una aplicación web fullstack construida como parte de una prueba técnica. Su objetivo es visualizar datos provenientes de un archivo JSON mediante gráficos interactivos, utilizando una API en FastAPI y una interfaz en Svelte con eCharts.

## Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) – Backend API en Python
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI para correr FastAPI
- [Svelte](https://svelte.dev/) – Framework frontend
- [eCharts](https://echarts.apache.org/) – Librería de visualización de gráficos
- [Docker](https://www.docker.com/) – Contenerización del proyecto
- [Docker Compose](https://docs.docker.com/compose/) – Orquestación del entorno

## Instrucciones de instalación y ejecución

### Prerrequisitos
- **Este proyecto corre completamente en contenedores Docker.**
- No es necesario tener instalado Python, Node o ningún entorno de desarrollo local. 
- Solo necesitas tener instalado [Docker Desktop](https://www.docker.com/products/docker-desktop) (con WSL2 habilitado si estás en Windows).
- Tener habilitado WSL2 y virtualización en la BIOS (si usás Windows)

### Pasos para ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/Victorfernandolopez/prueba_tecnica-reputacion_digital-.git
cd prueba_tecnica-reputacion_digital-
```

### Ejecutar el entorno con docker compose
```bash
docker-compose up --build
```

### Abrir el navegador en
- http://localhost:8000 – Interfaz principal
- http://localhost:8000/data – API de datos


#### 5. ¿Cómo funciona la app?

```markdown
# ¿Cómo funciona?

- El backend está construido con **FastAPI** y expone un único endpoint `/data`, que devuelve el contenido de `data.json` montado como volumen.
- El frontend está desarrollado con **Svelte**. Al cargar la página, realiza una petición `fetch("/data")` y procesa la respuesta para mostrar dos gráficos usando **eCharts**:
  - Un gráfico circular que muestra la distribución de productos.
  - Un gráfico de barras que muestra valores por mes.
- Ambos componentes (frontend y backend) se integran y se ejecutan desde un mismo contenedor.

# Personalizar los datos
El archivo `data.json` se encuentra en la raíz del proyecto y contiene los datos que se grafican.
Podés editar sus valores para cambiar lo que se muestra en los gráficos, sin necesidad de recompilar el frontend. Solo reiniciá Docker:
```bash
docker-compose down
docker-compose up
```
```