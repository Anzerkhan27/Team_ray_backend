🚀 **Team Ray | Django Backend API**

This is the **Django REST API** powering the Team Ray website — the official platform for the University of Huddersfield’s **first aerospace student society**. It handles content management, data storage, and API access for projects, team members, posts, and public queries.

🔗 Deployed API: [https://web-production-7860.up.railway.app/api/](https://web-production-7860.up.railway.app/api/)  
🔐 Admin Panel: /admin (with Django superuser)

---

🔧 **Tech Stack**

* 🧠 Django 5.1 + Django REST Framework  
* 🗄️ PostgreSQL (via Railway in production)  
* ☁️ **Cloudinary** for media file storage (images)  
* 🌐 CORS support for frontend integration  
* 🛠️ Django Admin for content management  
* 📦 WhiteNoise for static file serving  
* 🚉 Railway for backend deployment  

---

### ☁️ Cloudinary Integration

Team Ray backend now uses **Cloudinary** for all media file uploads (such as project and post images), instead of storing them locally in the `/media/` folder. This change ensures:

* 🌍 **Global content delivery** through a CDN
* ⚡ **Faster loading** of images for end-users
* 💾 **Reduced storage load** on our own server
* 🔒 **Secure and scalable media management**

In production, uploaded images are now hosted at URLs like:

```
https://res.cloudinary.com/<your-cloud-name>/image/upload/v<timestamp>/image-name.jpg
```

This is configured using the `CLOUDINARY_URL` environment variable (set in Railway under project variables):

```
CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
```


📚 **Core Models & Features**

1. 📸 **Project**
   * `name`, `description`, `image`, `created_at`
   * Used to display team engineering projects

2. 👤 **Member**
   * `name`, `role`, `bio`, `image`
   * Showcased in "Our Team" section

3. 📰 **Post**
   * `title`, `content`, `type` (news/event/announcement), `created_at`
   * Related `PostImage` model for gallery images

4. 📬 **Contact**
   * `full_name`, `email`, `phone`, `message`
   * Captures input from the Join form

---

🔌 **API Endpoints**

Base path: `/api/`

* `/projects/` — List all team projects  
* `/members/` — List team members  
* `/posts/` — List blog posts (with images)  
* `/contacts/` — Accepts POST queries from website form  

---

🛠️ **Admin Panel**

Admin is used for managing:

* Posts (with inline PostImages)  
* Members  
* Projects  
* Contact queries  

Create a superuser:

```bash
python manage.py createsuperuser
````

Visit `/admin` in your browser.

---

☁️ **Cloudinary Integration**

Media file uploads (e.g. project and post images) are stored and served through **Cloudinary CDN**, ensuring:

* ⚡ Faster global image delivery via CDN
* 📦 Optimized image formats and compression
* ✅ Persistent, scalable storage

In production, media files are no longer served from the `/media/` folder.

Set this in your `.env` or Railway secrets:

```
CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
```

Example Cloudinary file URL:
`https://res.cloudinary.com/<cloud_name>/image/upload/v.../post_image.jpg`

---

🌐 **Deployment Info**

* **Hosted on Railway** (PostgreSQL in production)
* **Cloudinary** used for image/media uploads
* **Supports local SQLite** fallback
* **CORS-enabled** for frontend on Cloudflare
* **Static files via WhiteNoise**

---

🔐 **Environment Config**

Environment variables (set via `.env` or Railway secrets):

```
SECRET_KEY=your-secret
DATABASE_URL=your-db-url
DEBUG=False
CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://teamray.team
CSRF_TRUSTED_ORIGINS=https://web-production-7860.up.railway.app,https://teamray.team
```

---

💻 **Local Development**

```bash
git clone https://github.com/Anzerkhan27/team-ray-backend.git
cd team-ray-backend

python -m venv env
source env/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

📂 **Project Structure Highlights**

```
team_ray/
├── core/            # models, views, serializers, admin
├── media/           # (local only) uploaded images
├── staticfiles/     # collected static files
├── team_ray/        # settings, urls, wsgi
└── manage.py
```

---

👨‍💻 **Maintainer**
Built by **Anzer Khan**
Software Lead & Founding Committee Member of Team Ray

LinkedIn: [https://linkedin.com/in/anzer-khan-31a14a209](https://linkedin.com/in/anzer-khan-31a14a209)


---


