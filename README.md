# 🎬 PopcornHour  
_Tarea 3 - Programación Avanzada_

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
