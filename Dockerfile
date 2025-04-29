# Dockerfile

# Imagen base con Python 3.11
FROM python:3.11-slim

# Evita crear archivos .pyc y salida sin buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# Copia requirements e instala dependencias
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Expone el puerto de la app
EXPOSE 8000

# Comando por defecto
CMD ["gunicorn", "pokedex_project.wsgi:application", "--bind", "0.0.0.0:8000"]
