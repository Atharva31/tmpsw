# EventHub — Event Management & Ticketing Platform

EventHub is a full-stack Eventbrite-like platform built for the **CMPE-202 Software Systems Engineering** course. It demonstrates low-level design principles, 8 OOP design patterns, and Agile/Scrum methodology.

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | FastAPI · Python 3.11 · SQLAlchemy (async) · PostgreSQL 15 |
| **Frontend** | React 18 · Vite · Tailwind CSS · Zustand · React Query |
| **Auth** | JWT (access + refresh tokens) · bcrypt |
| **Infrastructure** | Docker Compose · AWS (EC2 + RDS + S3 + ALB) |
| **CI/CD** | GitHub Actions |

## Design Patterns Implemented

| Pattern | Location |
|---|---|
| **Repository** | `eventhub-api/app/crud/base_crud.py` + domain cruds |
| **Factory** | `eventhub-api/app/services/notification_service.py` |
| **Observer** | `eventhub-api/app/services/event_service.py` (EventStatusSubject) |
| **Strategy** | `eventhub-api/app/services/event_service.py` (EventSortStrategy) |
| **Singleton** | `eventhub-api/app/config.py` (`@lru_cache`) + `database.py` |
| **Dependency Injection** | `eventhub-api/app/dependencies.py` (FastAPI `Depends`) |
| **DTO** | `eventhub-api/app/schemas/` (Pydantic models) |
| **Custom Hook** | `eventhub-ui/src/hooks/` (React Query wrappers) |

---

## Quick Start (Docker Compose)

```bash
# 1. Clone the repo
git clone https://github.com/your-org/eventhub.git
cd eventhub

# 2. Create env files
cp eventhub-api/.env.example eventhub-api/.env
# Edit eventhub-api/.env with your settings

# 3. Start all services
docker compose up

# 4. Run migrations
docker compose exec api alembic upgrade head

# 5. Seed mock data (optional)
docker compose exec api python scripts/seed.py
```

The API is at **http://localhost:8000** · Swagger UI at **http://localhost:8000/docs**
The React UI is at **http://localhost:5173**

---

## Local Development (without Docker)

### Backend

```bash
cd eventhub-api

# Install dependencies
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Set up env
cp .env.example .env
# Edit .env — set DATABASE_URL to your local Postgres

# Run migrations
alembic upgrade head

# Seed data
python scripts/seed.py

# Start dev server
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd eventhub-ui
npm install
# Create .env.local
echo "VITE_API_URL=http://localhost:8000" > .env.local
npm run dev
```

---

## Running Tests

```bash
cd eventhub-api

# Install test deps (aiosqlite for in-memory test DB)
pip install aiosqlite

# Run all tests with coverage
pytest tests/ -v --cov=app --cov-report=term-missing
```

Target: ≥ 70% line coverage.

---

## Project Structure

```
eventhub/
├── eventhub-api/              # FastAPI backend
│   ├── app/
│   │   ├── main.py            # App factory, CORS, lifespan (Observer startup)
│   │   ├── config.py          # Settings singleton (@lru_cache)
│   │   ├── database.py        # Async engine singleton
│   │   ├── dependencies.py    # DI: get_db, get_current_user, require_role
│   │   ├── models/            # SQLAlchemy ORM models
│   │   ├── schemas/           # Pydantic DTOs (Create/Read/Update)
│   │   ├── crud/              # Repository pattern (BaseCRUD + domain repos)
│   │   ├── services/          # Business logic + Factory, Observer, Strategy
│   │   └── routers/           # HTTP layer — parse → service → JSON
│   ├── alembic/               # DB migrations (incl. search trigger)
│   ├── tests/                 # pytest test suite
│   ├── scripts/               # seed.py, reset_db.py
│   └── Dockerfile
├── eventhub-ui/               # React frontend
│   ├── src/
│   │   ├── api/client.js      # Axios + JWT interceptor
│   │   ├── store/authStore.js # Zustand auth state
│   │   ├── hooks/             # Custom Hook pattern (useEvents, useRegistration…)
│   │   ├── pages/             # One file per route
│   │   ├── components/        # Reusable UI + EventCard, Map, TicketSelector
│   │   └── utils/             # luhn.js, formatDate.js, buildCalendarLink.js
│   └── package.json
├── docker-compose.yml
└── .github/workflows/deploy.yml
```

---

## API Endpoints Summary

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/v1/auth/register` | Public | Register (attendee or organizer) |
| POST | `/api/v1/auth/login` | Public | Login, get JWT tokens |
| GET | `/api/v1/events` | Public | Search & filter events (full-text, category, city, date…) |
| POST | `/api/v1/events` | Organizer | Create event (starts as draft) |
| POST | `/api/v1/events/{id}/submit` | Organizer | Submit for admin review |
| POST | `/api/v1/registrations` | Auth | Register for event (Luhn card validation, SELECT FOR UPDATE) |
| PUT | `/api/v1/admin/events/{id}/approve` | Admin | Approve → published (Observer fires email) |
| PUT | `/api/v1/admin/events/{id}/reject` | Admin | Reject with reason (Observer fires email) |
| GET | `/api/v1/events/{id}/calendar.ics` | Public | Download .ics calendar file |
| GET | `/api/v1/health` | Public | Health check (used by AWS ALB) |

Full API docs available at `/docs` (Swagger UI) or `/redoc`.

---

## Seed Accounts

After running `python scripts/seed.py`:

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@eventhub.dev | Admin1234! |
| Organizer | (random) | Passw0rd! |
| Attendee | (random) | Passw0rd! |

---

## AWS Deployment (Sprint 6)

See PRD Section 12 for full infrastructure setup. Overview:

1. **VPC** — 2 public + 2 private subnets, 2 AZs
2. **RDS** — PostgreSQL 15 `db.t3.micro` in private subnet
3. **EC2 Auto Scaling Group** — min 2, max 4, scale on CPU > 70%
4. **ALB** — Internet-facing, health check `GET /api/v1/health`
5. **S3** — Hosts React `dist/` + banner images
6. **GitHub Actions** — test → deploy on push to `main`

---

## Scrum Sprint Plan

| Sprint | Dates | Deliverables |
|--------|-------|-------------|
| 1 | Feb 8–22 | Auth, models, Alembic, React scaffold |
| 2 | Feb 22–Mar 8 | Events CRUD, category filter, event cards |
| 3 | Mar 8–22 | Registrations, Luhn payment, QR codes |
| 4 | Mar 22–Apr 5 | Admin panel, Observer emails, map |
| 5 | Apr 5–19 | Calendar .ics, reminder scheduler, search |
| 6 | Apr 19–May 3 | AWS deploy, CI/CD, final polish |
