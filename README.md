# Caronte_challenge_ingreso

**Aplicación web con Django y Django REST Framework** que consume la PokéAPI para listar y detallar Pokémon con paginación, búsqueda y vistas server-render.

---

## 📋 Tecnologías

- **Python** 3.11
- **Django** 5.2
- **Django REST Framework**
- **django-filter**
- **requests**
- **Bootstrap 5** (vía CDN)
- **Gunicorn** (WSGI server)
- **pytest** / **pytest-django** / **responses**
- **SQLite** (por defecto)

---

## 🛠️ Configuración previa

1. Instala las herramientas:
   - Python 3.11  
   - Git  
   - (Opcional) Docker y Docker Compose

2. Clona el repositorio y navega al proyecto:
   ```
   git clone https://github.com/HonaWaveSoftwareInnovations/Caronte_challenge_ingreso.git
   cd Caronte_challenge_ingreso
   ```

3. Crea `.env.example` con este contenido mínimo:
   ```
   POKEAPI_BASE_URL=https://pokeapi.co/api/v2
   SECRET_KEY=tu_super_secret_key
   DEBUG=True
   ```

4. Copia y edita tu entorno:
   ```
   cp .env.example .env
   ```

5. Ajusta `.env` si es necesario.

---

## 🚀 Ejecución local (sin Docker)

1. Crea y activa un entorno virtual:
   ```
   python -m venv venv
   # PowerShell
   .\venv\Scripts\Activate.ps1
   # CMD
   venv\Scripts\activate.bat
   # macOS/Linux
   source venv/bin/activate
   ```

2. Instala dependencias:
   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Aplica migraciones:
   ```
   python manage.py migrate
   ```

4. (Opcional) Crea superusuario:
   ```
   python manage.py createsuperuser
   ```

5. Inicia servidor:
   ```
   python manage.py runserver
   ```

6. Prueba en el navegador:
   - **Lista HTML**: http://127.0.0.1:8000/api/  
   - **Detalle HTML**: http://127.0.0.1:8000/api/pokemon/bulbasaur/  
   - **API JSON**: http://127.0.0.1:8000/api/pokemon/?page=1&page_size=10

---

## 📦 Despliegue con Docker & Docker Compose

1. Asegúrate de tener Docker y Docker Compose.

2. Copia `.env` si aún no existe:
   ```
   cp .env.example .env
   ```

3. Construye y levanta contenedores:
   ```
   docker-compose up --build -d
   ```

4. Ejecuta migraciones en el contenedor:
   ```
   docker-compose run web python manage.py migrate
   ```

5. (Opcional) Crea superusuario:
   ```
   docker-compose run web python manage.py createsuperuser
   ```

6. Accede:
   - http://localhost:8000/api/  
   - http://localhost:8000/api/pokemon/charizard/  
   - http://localhost:8000/api/pokemon/?page=1&page_size=10

7. Ver logs:
   ```
   docker-compose logs -f
   ```

8. Detener:
   ```
   docker-compose down
   ```

---

## 🧪 Pruebas Automatizadas

Ejecuta:
```
pytest
```

Cubre:
- Servicios de PokéAPI  
- Endpoints JSON (DRF)  
- Vistas HTML (index, detail)

---

¡Gracias por revisar mi proyecto!
