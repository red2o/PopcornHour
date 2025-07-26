# 🎬 PopcornHour

**PopcornHour** es una plataforma web para recomendar, calificar y discutir películas y series. Cuenta con un sistema de roles que permite a usuarios **moderadores** subir películas y a usuarios **estándar** calificar, comentar y agregar a favoritos.

---

## 🚀 Características principales

- Registro e inicio de sesión por tipo de usuario (Estándar / Moderador)
- Catálogo de películas accesible para usuarios registrados
- Moderadores pueden:
  - Subir películas
  - Ver sus películas subidas en un panel exclusivo
- Detalle de película con:
  - Imagen, título y descripción
  - Agregar o quitar de favoritos
  - Calificar de 1 a 5 estrellas
  - Dejar comentarios visibles a todos
- Panel de perfil del usuario
- Página de favoritos personalizada

---

## 🛠 Tecnologías utilizadas

- **Python 3.10+**
- **Flask**
- **Flask-Login**
- **Flask-WTF**
- **SQLAlchemy**
- **Supabase** (PostgreSQL)
- **Bootstrap 5**
- **UUID para IDs**

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/red2o/PopcornHour.git
cd PopcornHour
```

### 2. Crear entorno virtual

```bash
python -m venv venv
.
env\Scripts ctivate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si aún no tienes `requirements.txt`, puedes generarlo con:

```bash
pip freeze > requirements.txt
```

### 4. Configurar base de datos

Usamos **Supabase** como backend:

```
postgresql://postgres:car152141711081@db.lmmsxpwbxwwgwbzdnsan.supabase.co:5432/postgres
```

Asegúrate de que tu archivo `app/__init__.py` o `config.py` contenga la URL de conexión a la base de datos en `SQLALCHEMY_DATABASE_URI`.

### 5. Inicializar la base de datos

Abre PowerShell:

```bash
python
>>> from app import db
>>> from app import create_app
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
```

---

## ▶️ Ejecutar el proyecto

```bash
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

Accede a `http://127.0.0.1:5000/` desde tu navegador.

---

## 👤 Tipos de usuarios

- **Moderador**:
  - Puede subir películas
  - Accede al panel de moderador
- **Estándar**:
  - Puede calificar, comentar y agregar películas a favoritos

---

## 📁 Estructura de carpetas

```
PopcornHour/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   ├── decorators.py
│   ├── templates/
│   └── static/
│
├── venv/
├── run.py
├── requirements.txt
└── README.md
```

---

## 🧪 Pruebas sugeridas

- Crear usuario estándar y moderador
- Verificar redirección correcta tras login
- Subir película como moderador
- Agregar/quitar de favoritos
- Agregar calificación y comentario
- Ver películas en catálogo y perfil

---

## 📬 Contacto

Desarrollado por **@red2o**  para la tarea en hybridge
GitHub: [https://github.com/red2o](https://github.com/red2o)
