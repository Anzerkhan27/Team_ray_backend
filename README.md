

---

🚀 **Team Ray | Django Backend API**

This is the **Django REST API** powering the Team Ray website — the official platform for the University of Huddersfield’s **first aerospace student society**. It handles content management, data storage, and API access for projects, team members, posts, and public queries.

🔗 Deployed API: [https://web-production-7860.up.railway.app/api/](https://web-production-7860.up.railway.app/api/)
🔐 Admin Panel: /admin (with Django superuser)

---

🔧 **Tech Stack**

* 🧠 Django 5.1 + Django REST Framework
* 🗄️ PostgreSQL (via Railway in production)
* 🌐 CORS support for frontend integration
* 🛠️ Django Admin for content management
* 📦 WhiteNoise for static file serving
* ☁️ Railway for backend deployment

---

📚 **Core Models & Features**

1. 📸 **Project**

   * name, description, image, created\_at
   * Used to display team engineering projects

2. 👤 **Member**

   * name, role, bio, image
   * Showcased in "Our Team" section

3. 📰 **Post**

   * title, content, type (news/event/announcement), created\_at
   * PostImage model (one-to-many) for photo galleries

4. 📬 **Contact**

   * full\_name, email, phone, message
   * Data collected from "Join Us" form

---

🔌 **API Endpoints**
Base path: `/api/`

* `/projects/` — List all team projects
* `/members/` — List team members
* `/posts/` — List blog posts with optional images
* `/contacts/` — Accept POST form submissions from public users

---

🛠️ **Admin Panel**
Admin is used for managing:

* Posts (with inline PostImages)
* Members
* Projects
* Contact queries

To create an admin:

```bash
python manage.py createsuperuser
```

Then visit `/admin` in your browser.

---

🌐 **Deployment Info**

* **Hosted on Railway** (PostgreSQL database used in production)
* **Supports local SQLite** for development fallback
* **CORS-enabled** for React frontend communication
* **Static files via WhiteNoise**
* **Image uploads served from `/media/` directory**

---

🔐 **Environment Config**

Set in `.env` (you can rename to `.env.production` or use Railway secrets):

* `SECRET_KEY=your-secret`
* `DATABASE_URL=your-db-url` (used in production)
* `DEBUG=False` in production

CORS allowed origins:

* `http://localhost:3000`
* `https://team-ray-frontend.pages.dev`

CSRF trusted origin:

* `https://web-production-7860.up.railway.app`

---

🚀 **Local Development**

```bash
# Clone the repo
git clone https://github.com/your-username/team-ray-backend.git
cd team-ray-backend

# Create virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

---

📂 **Project Structure Highlights**

team\_ray/
├── core/ → models, views, serializers, admin
├── media/ → uploaded images
├── staticfiles/ → auto-collected static files
├── team\_ray/ → settings, URLs, WSGI

---

👨‍💻 **Maintainer**
Built by **Anzer Khan**,
Software Lead & Founding Committee Member of Team Ray

LinkedIn: [https://linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)
Portfolio: [https://your-portfolio.com](https://your-portfolio.com)

---


