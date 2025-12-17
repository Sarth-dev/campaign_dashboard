# Campaign Dashboard – Backend API

A production-ready **Django + Django REST Framework** backend for managing marketing campaigns, analytics, and a simple dashboard view. The project is deployed on **Render** with **PostgreSQL (Supabase)** as the database.

---

## 🚀 Live Deployment

**Base URL:**

```
https://campaign-dashboard-25c9.onrender.com
```

---

## 🧠 Project Overview

This backend application provides:

* CRUD APIs for managing ad campaigns
* Aggregated campaign analytics for dashboards
* USD → INR exchange rate API integration
* Production deployment using Gunicorn + Render

The project follows clean backend structure and real-world deployment practices.

---

## 🛠 Tech Stack

* **Backend Framework:** Django 6.0
* **API Layer:** Django REST Framework (DRF)
* **Database:** PostgreSQL (Supabase)
* **ORM:** Django ORM
* **Server:** Gunicorn
* **Hosting:** Render
* **Language:** Python 3.13

---

## 📁 Project Structure

```
campaign_dashboard/
├── backend/
│   ├── manage.py
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── campaign/
│       ├── migrations/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       └── admin.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔌 API Endpoints

### Campaign APIs

| Method | Endpoint               | Description        |
| ------ | ---------------------- | ------------------ |
| GET    | `/api/campaigns/`      | List all campaigns |
| POST   | `/api/campaigns/`      | Create a campaign  |
| GET    | `/api/campaigns/{id}/` | Retrieve campaign  |
| PUT    | `/api/campaigns/{id}/` | Update campaign    |
| DELETE | `/api/campaigns/{id}/` | Delete campaign    |

### Dashboard View

| Method | Endpoint      | Description                  |
| ------ | ------------- | ---------------------------- |
| GET    | `/dashboard/` | Campaign analytics dashboard |

### Exchange Rate API

| Method | Endpoint              | Description                |
| ------ | --------------------- | -------------------------- |
| GET    | `/api/exchange-rate/` | USD → INR rate (CoinGecko) |

---

## ⚙️ Local Setup (Run on Your Machine)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sarth-dev/campaign_dashboard.git
cd campaign_dashboard
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Environment Variables

Create a `.env` file inside the `backend/` directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=your-supabase-host
DB_PORT=5432
```


---

### 5️⃣ Run Migrations

```bash
cd backend
python manage.py migrate
```

---

### 6️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### 7️⃣ Run Development Server

```bash
python manage.py runserver
```

App will be available at:

```
http://127.0.0.1:8000/
```

---

## 🚀 Deployment (Render)

### 1️⃣ Render Service Settings

* **Service Type:** Web Service
* **Root Directory:** `backend`
* **Build Command:**

```bash
pip install -r requirements.txt && python manage.py migrate
```

* **Start Command:**

```bash
gunicorn backend.wsgi:application
```

---

### 2️⃣ Environment Variables on Render

Add the following in Render Dashboard → Environment:

```
DEBUG=False
SECRET_KEY=your-secret-key
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=your-supabase-pooler-host
DB_PORT=5432
```

✅ Use **Supabase Transaction Pooler** for production

---

### 3️⃣ Database Notes (Supabase)

* PostgreSQL hosted on Supabase
* Transaction pooler used for Render compatibility
* psycopg2-binary used as DB driver

---

## 🧪 Testing

* APIs tested using **Postman**
* CRUD operations verified
* Deployment logs validated on Render

---

## ⚠️ Known Limitations

* Dashboard UI is minimal (focus is backend)
* Static files not configured for production
* Authentication not implemented (out of scope)

---

## 🔮 Future Improvements

* Add JWT authentication
* Add pagination & filtering
* Improve dashboard UI with charts
* Add unit & integration tests

---

## 👨‍💻 Author

**Sarthak Kale**
Backend / Full Stack Developer

GitHub: [https://github.com/Sarth-dev](https://github.com/Sarth-dev)

---

## ✅ Final Notes

This project demonstrates real-world backend development, API design, database integration, and production deployment using Django.
