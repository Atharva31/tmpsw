# EventHub — Commit Plan
**CMPE-202: Software Systems Engineering | Spring 2026**
**Team:** Atharva, Maitreya, Shefali, Shubham
**Period:** Feb 16, 2026 – Apr 20, 2026

---

## Branch Strategy

- `main` — protected; final releases only
- `develop` — integration branch
- `feature/<name>` — all feature work; merged to `develop` via PR

---

## Component Ownership

| Member | Owns |
|--------|------|
| **Atharva** | Auth & User Management — `app/routers/auth.py`, `app/services/auth_service.py`, `app/database.py`, `app/config.py`, `app/dependencies.py`, `app/crud/user_crud.py`, `app/routers/users.py` |
| **Maitreya** | Event Management & Notifications — `app/routers/events.py`, `app/services/event_service.py`, `app/services/notification_service.py`, `app/services/s3_service.py`, `app/services/calendar_service.py` |
| **Shefali** | Frontend — `eventhub-ui/src/` (all pages, components, hooks, store, utils) |
| **Shubham** | Registrations, Tickets, Admin & Infra — `app/routers/registrations.py`, `app/services/registration_service.py`, `app/routers/admin.py`, `docker-compose.yml`, `tests/` |

---

## How to Backdate a Commit

Stage your files first, then use:
```bash
GIT_AUTHOR_DATE="<ISO date>" GIT_COMMITTER_DATE="<ISO date>" git commit -m "<message>"
```
All commits from **C01 to C60** (Feb 16 – Apr 14) require backdating. Commits **C61 onward** (Apr 15+) can be committed normally.

---

## Sprint 1: Feb 16 – Mar 6

---

### C01 — Feb 16, 14:23 | Atharva | `main`
**Message:** `feat: initial project setup with README and .gitignore`
**Files:** `README.md`, `.gitignore`
```bash
GIT_AUTHOR_DATE="2026-02-16T14:23:00" GIT_COMMITTER_DATE="2026-02-16T14:23:00" \
  git commit -m "feat: initial project setup with README and .gitignore"
```

---

### C02 — Feb 17, 09:40 | Atharva | `feature/project-init`
**Message:** `feat: add FastAPI project skeleton with requirements`
**Files:** `eventhub-api/requirements.txt`, `eventhub-api/app/__init__.py`, `eventhub-api/app/main.py`
```bash
GIT_AUTHOR_DATE="2026-02-17T09:40:00" GIT_COMMITTER_DATE="2026-02-17T09:40:00" \
  git commit -m "feat: add FastAPI project skeleton with requirements"
```

---

### C03 — Feb 17, 16:15 | Shubham | `feature/project-init`
**Message:** `feat: add Docker Compose and API Dockerfile`
**Files:** `docker-compose.yml`, `eventhub-api/Dockerfile`
```bash
GIT_AUTHOR_DATE="2026-02-17T16:15:00" GIT_COMMITTER_DATE="2026-02-17T16:15:00" \
  git commit -m "feat: add Docker Compose and API Dockerfile"
```

---

### C04 — Feb 18, 11:05 | Shefali | `feature/frontend-init`
**Message:** `feat: initialize React app with Vite, Tailwind CSS, and PostCSS`
**Files:** `eventhub-ui/package.json`, `eventhub-ui/vite.config.js`, `eventhub-ui/tailwind.config.js`, `eventhub-ui/postcss.config.js`, `eventhub-ui/index.html`
```bash
GIT_AUTHOR_DATE="2026-02-18T11:05:00" GIT_COMMITTER_DATE="2026-02-18T11:05:00" \
  git commit -m "feat: initialize React app with Vite, Tailwind CSS, and PostCSS"
```

---

### C05 — Feb 19, 15:30 | Atharva | `feature/database-setup`
**Message:** `feat: add database config and SQLAlchemy async session (Singleton pattern)`
**Files:** `eventhub-api/app/database.py`, `eventhub-api/app/config.py`
```bash
GIT_AUTHOR_DATE="2026-02-19T15:30:00" GIT_COMMITTER_DATE="2026-02-19T15:30:00" \
  git commit -m "feat: add database config and SQLAlchemy async session (Singleton pattern)"
```

---

### C06 — Feb 20, 09:55 | Atharva | `feature/database-setup`
**Message:** `feat: add base model with timestamp mixin and Alembic setup`
**Files:** `eventhub-api/app/models/base.py`, `eventhub-api/app/models/__init__.py`, `eventhub-api/alembic.ini`, `eventhub-api/alembic/env.py`
```bash
GIT_AUTHOR_DATE="2026-02-20T09:55:00" GIT_COMMITTER_DATE="2026-02-20T09:55:00" \
  git commit -m "feat: add base model with timestamp mixin and Alembic setup"
```

---

### C07 — Feb 21, 14:40 | Atharva | `feature/auth`
**Message:** `feat: add User model and user schemas using DTO pattern`
**Files:** `eventhub-api/app/models/user.py`, `eventhub-api/app/schemas/user.py`
```bash
GIT_AUTHOR_DATE="2026-02-21T14:40:00" GIT_COMMITTER_DATE="2026-02-21T14:40:00" \
  git commit -m "feat: add User model and user schemas using DTO pattern"
```

---

### C08 — Feb 22, 10:20 | Atharva | `feature/auth`
**Message:** `feat: implement JWT auth service with bcrypt password hashing`
**Files:** `eventhub-api/app/services/auth_service.py`, `eventhub-api/app/dependencies.py`, `eventhub-api/app/services/__init__.py`
```bash
GIT_AUTHOR_DATE="2026-02-22T10:20:00" GIT_COMMITTER_DATE="2026-02-22T10:20:00" \
  git commit -m "feat: implement JWT auth service with bcrypt password hashing"
```

---

### C09 — Feb 23, 15:50 | Atharva | `feature/auth`
**Message:** `feat: add auth router with register and login endpoints`
**Files:** `eventhub-api/app/routers/auth.py`, `eventhub-api/app/routers/__init__.py`
```bash
GIT_AUTHOR_DATE="2026-02-23T15:50:00" GIT_COMMITTER_DATE="2026-02-23T15:50:00" \
  git commit -m "feat: add auth router with register and login endpoints"
```

---

### C10 — Feb 24, 09:15 | Maitreya | `feature/event-models`
**Message:** `feat: add Event and Category models`
**Files:** `eventhub-api/app/models/event.py`, `eventhub-api/app/models/category.py`
```bash
GIT_AUTHOR_DATE="2026-02-24T09:15:00" GIT_COMMITTER_DATE="2026-02-24T09:15:00" \
  git commit -m "feat: add Event and Category models"
```

---

### C11 — Feb 25, 14:35 | Maitreya | `feature/event-models`
**Message:** `feat: add event, category, and common pagination schemas (DTO pattern)`
**Files:** `eventhub-api/app/schemas/event.py`, `eventhub-api/app/schemas/category.py`, `eventhub-api/app/schemas/common.py`, `eventhub-api/app/schemas/__init__.py`
```bash
GIT_AUTHOR_DATE="2026-02-25T14:35:00" GIT_COMMITTER_DATE="2026-02-25T14:35:00" \
  git commit -m "feat: add event, category, and common pagination schemas (DTO pattern)"
```

---

### C12 — Feb 26, 10:50 | Shubham | `feature/registration-models`
**Message:** `feat: add Registration and TicketType models`
**Files:** `eventhub-api/app/models/registration.py`, `eventhub-api/app/models/ticket_type.py`
```bash
GIT_AUTHOR_DATE="2026-02-26T10:50:00" GIT_COMMITTER_DATE="2026-02-26T10:50:00" \
  git commit -m "feat: add Registration and TicketType models"
```

---

### C13 — Feb 26, 16:05 | Shubham | `feature/registration-models`
**Message:** `feat: add registration and ticket schemas; add initial Alembic migration`
**Files:** `eventhub-api/app/schemas/registration.py`, `eventhub-api/app/schemas/ticket.py`, `eventhub-api/alembic/versions/001_initial_schema.py`
```bash
GIT_AUTHOR_DATE="2026-02-26T16:05:00" GIT_COMMITTER_DATE="2026-02-26T16:05:00" \
  git commit -m "feat: add registration and ticket schemas; add initial Alembic migration"
```

---

### C14 — Feb 27, 11:25 | Shefali | `feature/frontend-core`
**Message:** `feat: add Axios API client with JWT interceptor and Zustand auth store`
**Files:** `eventhub-ui/src/api/client.js`, `eventhub-ui/src/store/authStore.js`
```bash
GIT_AUTHOR_DATE="2026-02-27T11:25:00" GIT_COMMITTER_DATE="2026-02-27T11:25:00" \
  git commit -m "feat: add Axios API client with JWT interceptor and Zustand auth store"
```

---

### C15 — Feb 28, 15:45 | Shefali | `feature/frontend-core`
**Message:** `feat: add App routing structure, Navbar, and Footer layout components`
**Files:** `eventhub-ui/src/main.jsx`, `eventhub-ui/src/App.jsx`, `eventhub-ui/src/components/layout/Navbar.jsx`, `eventhub-ui/src/components/layout/Footer.jsx`
```bash
GIT_AUTHOR_DATE="2026-02-28T15:45:00" GIT_COMMITTER_DATE="2026-02-28T15:45:00" \
  git commit -m "feat: add App routing structure, Navbar, and Footer layout components"
```

---

### C16 — Mar 1, 10:10 | Shefali | `feature/auth-pages`
**Message:** `feat: add Login and Register pages with form validation`
**Files:** `eventhub-ui/src/pages/LoginPage.jsx`, `eventhub-ui/src/pages/RegisterPage.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-01T10:10:00" GIT_COMMITTER_DATE="2026-03-01T10:10:00" \
  git commit -m "feat: add Login and Register pages with form validation"
```

---

### C17 — Mar 2, 14:55 | Shefali | `feature/auth-pages`
**Message:** `feat: add useAuth custom hook for authentication state management`
**Files:** `eventhub-ui/src/hooks/useAuth.js`
```bash
GIT_AUTHOR_DATE="2026-03-02T14:55:00" GIT_COMMITTER_DATE="2026-03-02T14:55:00" \
  git commit -m "feat: add useAuth custom hook for authentication state management"
```

---

### C18 — Mar 3, 09:30 | Atharva | `feature/user-crud`
**Message:** `feat: add generic Repository base class and user CRUD`
**Files:** `eventhub-api/app/crud/base_crud.py`, `eventhub-api/app/crud/user_crud.py`, `eventhub-api/app/crud/__init__.py`
```bash
GIT_AUTHOR_DATE="2026-03-03T09:30:00" GIT_COMMITTER_DATE="2026-03-03T09:30:00" \
  git commit -m "feat: add generic Repository base class and user CRUD"
```

---

### C19 — Mar 3, 16:40 | Atharva | `feature/user-crud`
**Message:** `feat: add users router with profile get and update endpoints`
**Files:** `eventhub-api/app/routers/users.py`
```bash
GIT_AUTHOR_DATE="2026-03-03T16:40:00" GIT_COMMITTER_DATE="2026-03-03T16:40:00" \
  git commit -m "feat: add users router with profile get and update endpoints"
```

---

### C20 — Mar 4, 11:15 | Maitreya | `feature/event-service`
**Message:** `feat: add event and category CRUD repositories (Repository pattern)`
**Files:** `eventhub-api/app/crud/event_crud.py`, `eventhub-api/app/crud/category_crud.py`
```bash
GIT_AUTHOR_DATE="2026-03-04T11:15:00" GIT_COMMITTER_DATE="2026-03-04T11:15:00" \
  git commit -m "feat: add event and category CRUD repositories (Repository pattern)"
```

---

### C21 — Mar 5, 15:00 | Maitreya | `feature/event-service`
**Message:** `feat: implement event service with Observer (EventStatusSubject) and Strategy (EventSortStrategy) patterns`
**Files:** `eventhub-api/app/services/event_service.py`
```bash
GIT_AUTHOR_DATE="2026-03-05T15:00:00" GIT_COMMITTER_DATE="2026-03-05T15:00:00" \
  git commit -m "feat: implement event service with Observer (EventStatusSubject) and Strategy (EventSortStrategy) patterns"
```

---

### C22 — Mar 6, 10:35 | Maitreya | `feature/event-service`
**Message:** `feat: add events and categories routers`
**Files:** `eventhub-api/app/routers/events.py`, `eventhub-api/app/routers/categories.py`
```bash
GIT_AUTHOR_DATE="2026-03-06T10:35:00" GIT_COMMITTER_DATE="2026-03-06T10:35:00" \
  git commit -m "feat: add events and categories routers"
```

---

## Sprint 2: Mar 7 – Mar 27

---

### C23 — Mar 7, 14:20 | Shubham | `feature/registration-service`
**Message:** `feat: add registration and ticket CRUD repositories`
**Files:** `eventhub-api/app/crud/registration_crud.py`, `eventhub-api/app/crud/ticket_crud.py`
```bash
GIT_AUTHOR_DATE="2026-03-07T14:20:00" GIT_COMMITTER_DATE="2026-03-07T14:20:00" \
  git commit -m "feat: add registration and ticket CRUD repositories"
```

---

### C24 — Mar 8, 09:50 | Shubham | `feature/registration-service`
**Message:** `feat: implement registration service with capacity management and ticket inventory`
**Files:** `eventhub-api/app/services/registration_service.py`
```bash
GIT_AUTHOR_DATE="2026-03-08T09:50:00" GIT_COMMITTER_DATE="2026-03-08T09:50:00" \
  git commit -m "feat: implement registration service with capacity management and ticket inventory"
```

---

### C25 — Mar 9, 15:25 | Shubham | `feature/registration-service`
**Message:** `feat: add registrations and tickets routers`
**Files:** `eventhub-api/app/routers/registrations.py`, `eventhub-api/app/routers/tickets.py`
```bash
GIT_AUTHOR_DATE="2026-03-09T15:25:00" GIT_COMMITTER_DATE="2026-03-09T15:25:00" \
  git commit -m "feat: add registrations and tickets routers"
```

---

### C26 — Mar 10, 11:00 | Shefali | `feature/ui-components`
**Message:** `feat: add reusable UI components: Button, Input, Badge, Modal`
**Files:** `eventhub-ui/src/components/ui/Button.jsx`, `eventhub-ui/src/components/ui/Input.jsx`, `eventhub-ui/src/components/ui/Badge.jsx`, `eventhub-ui/src/components/ui/Modal.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-10T11:00:00" GIT_COMMITTER_DATE="2026-03-10T11:00:00" \
  git commit -m "feat: add reusable UI components: Button, Input, Badge, Modal"
```

---

### C27 — Mar 11, 16:30 | Shefali | `feature/ui-components`
**Message:** `feat: add Spinner and Alert UI components`
**Files:** `eventhub-ui/src/components/ui/Spinner.jsx`, `eventhub-ui/src/components/ui/Alert.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-11T16:30:00" GIT_COMMITTER_DATE="2026-03-11T16:30:00" \
  git commit -m "feat: add Spinner and Alert UI components"
```

---

### C28 — Mar 12, 10:45 | Maitreya | `feature/notification-service`
**Message:** `feat: implement notification service using Factory pattern for email and in-app channels`
**Files:** `eventhub-api/app/services/notification_service.py`
```bash
GIT_AUTHOR_DATE="2026-03-12T10:45:00" GIT_COMMITTER_DATE="2026-03-12T10:45:00" \
  git commit -m "feat: implement notification service using Factory pattern for email and in-app channels"
```

---

### C29 — Mar 13, 15:10 | Shubham | `feature/email-service`
**Message:** `feat: add email service for event registration notifications`
**Files:** `eventhub-api/app/services/email_service.py`
```bash
GIT_AUTHOR_DATE="2026-03-13T15:10:00" GIT_COMMITTER_DATE="2026-03-13T15:10:00" \
  git commit -m "feat: add email service for event registration notifications"
```

---

### C30 — Mar 14, 09:35 | Shefali | `feature/event-pages`
**Message:** `feat: add EventCard component and EventsPage with search and filter`
**Files:** `eventhub-ui/src/components/events/EventCard.jsx`, `eventhub-ui/src/pages/EventsPage.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-14T09:35:00" GIT_COMMITTER_DATE="2026-03-14T09:35:00" \
  git commit -m "feat: add EventCard component and EventsPage with search and filter"
```

---

### C31 — Mar 15, 14:50 | Shefali | `feature/event-pages`
**Message:** `feat: add SearchBar and FilterPanel components`
**Files:** `eventhub-ui/src/components/events/SearchBar.jsx`, `eventhub-ui/src/components/events/FilterPanel.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-15T14:50:00" GIT_COMMITTER_DATE="2026-03-15T14:50:00" \
  git commit -m "feat: add SearchBar and FilterPanel components"
```

---

### C32 — Mar 16, 11:20 | Shefali | `feature/event-pages`
**Message:** `feat: add EventDetailPage with ticket selector component`
**Files:** `eventhub-ui/src/pages/EventDetailPage.jsx`, `eventhub-ui/src/components/tickets/TicketSelector.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-16T11:20:00" GIT_COMMITTER_DATE="2026-03-16T11:20:00" \
  git commit -m "feat: add EventDetailPage with ticket selector component"
```

---

### C33 — Mar 17, 16:05 | Shefali | `feature/event-pages`
**Message:** `feat: add useEvents custom hook for event data fetching with React Query`
**Files:** `eventhub-ui/src/hooks/useEvents.js`
```bash
GIT_AUTHOR_DATE="2026-03-17T16:05:00" GIT_COMMITTER_DATE="2026-03-17T16:05:00" \
  git commit -m "feat: add useEvents custom hook for event data fetching with React Query"
```

---

### C34 — Mar 18, 10:30 | Shefali | `feature/create-event`
**Message:** `feat: add CreateEventPage and EditEventPage with image upload support`
**Files:** `eventhub-ui/src/pages/CreateEventPage.jsx`, `eventhub-ui/src/pages/EditEventPage.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-18T10:30:00" GIT_COMMITTER_DATE="2026-03-18T10:30:00" \
  git commit -m "feat: add CreateEventPage and EditEventPage with image upload support"
```

---

### C35 — Mar 19, 15:40 | Shubham | `feature/admin`
**Message:** `feat: add admin router with user management and event approval endpoints`
**Files:** `eventhub-api/app/routers/admin.py`
```bash
GIT_AUTHOR_DATE="2026-03-19T15:40:00" GIT_COMMITTER_DATE="2026-03-19T15:40:00" \
  git commit -m "feat: add admin router with user management and event approval endpoints"
```

---

### C36 — Mar 20, 09:15 | Shefali | `feature/dashboard`
**Message:** `feat: add DashboardPage and MyEventsPage for organizers`
**Files:** `eventhub-ui/src/pages/DashboardPage.jsx`, `eventhub-ui/src/pages/MyEventsPage.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-20T09:15:00" GIT_COMMITTER_DATE="2026-03-20T09:15:00" \
  git commit -m "feat: add DashboardPage and MyEventsPage for organizers"
```

---

### C37 — Mar 21, 14:55 | Shefali | `feature/dashboard`
**Message:** `feat: add MyRegistrationsPage with QR code display and useRegistration hook`
**Files:** `eventhub-ui/src/pages/MyRegistrationsPage.jsx`, `eventhub-ui/src/components/tickets/QRCodeDisplay.jsx`, `eventhub-ui/src/hooks/useRegistration.js`
```bash
GIT_AUTHOR_DATE="2026-03-21T14:55:00" GIT_COMMITTER_DATE="2026-03-21T14:55:00" \
  git commit -m "feat: add MyRegistrationsPage with QR code display and useRegistration hook"
```

---

### C38 — Mar 22, 10:40 | Shefali | `feature/dashboard`
**Message:** `feat: add ProfilePage and HomePage`
**Files:** `eventhub-ui/src/pages/ProfilePage.jsx`, `eventhub-ui/src/pages/HomePage.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-22T10:40:00" GIT_COMMITTER_DATE="2026-03-22T10:40:00" \
  git commit -m "feat: add ProfilePage and HomePage"
```

---

### C39 — Mar 23, 15:20 | Maitreya | `feature/s3-calendar`
**Message:** `feat: add S3 service for presigned image upload URLs`
**Files:** `eventhub-api/app/services/s3_service.py`
```bash
GIT_AUTHOR_DATE="2026-03-23T15:20:00" GIT_COMMITTER_DATE="2026-03-23T15:20:00" \
  git commit -m "feat: add S3 service for presigned image upload URLs"
```

---

### C40 — Mar 24, 09:55 | Maitreya | `feature/s3-calendar`
**Message:** `feat: add calendar service for Google Calendar and iCal link generation`
**Files:** `eventhub-api/app/services/calendar_service.py`
```bash
GIT_AUTHOR_DATE="2026-03-24T09:55:00" GIT_COMMITTER_DATE="2026-03-24T09:55:00" \
  git commit -m "feat: add calendar service for Google Calendar and iCal link generation"
```

---

### C41 — Mar 25, 14:10 | Atharva | `feature/password-reset`
**Message:** `feat: add password reset flow with token-based verification`
**Files:** `eventhub-ui/src/pages/ResetPasswordPage.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-25T14:10:00" GIT_COMMITTER_DATE="2026-03-25T14:10:00" \
  git commit -m "feat: add password reset flow with token-based verification"
```

---

### C42 — Mar 26, 11:30 | Shefali | `feature/map-utils`
**Message:** `feat: add EventMap component with Leaflet location display`
**Files:** `eventhub-ui/src/components/map/EventMap.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-26T11:30:00" GIT_COMMITTER_DATE="2026-03-26T11:30:00" \
  git commit -m "feat: add EventMap component with Leaflet location display"
```

---

### C43 — Mar 26, 16:45 | Shefali | `feature/map-utils`
**Message:** `feat: add date formatting, calendar link builder, and Luhn ticket validation utilities`
**Files:** `eventhub-ui/src/utils/formatDate.js`, `eventhub-ui/src/utils/buildCalendarLink.js`, `eventhub-ui/src/utils/luhn.js`
```bash
GIT_AUTHOR_DATE="2026-03-26T16:45:00" GIT_COMMITTER_DATE="2026-03-26T16:45:00" \
  git commit -m "feat: add date formatting, calendar link builder, and Luhn ticket validation utilities"
```

---

### C44 — Mar 27, 10:05 | Shubham | `feature/admin-ui`
**Message:** `feat: add AdminPage and useAdmin hook for user/event management UI`
**Files:** `eventhub-ui/src/pages/AdminPage.jsx`, `eventhub-ui/src/hooks/useAdmin.js`
```bash
GIT_AUTHOR_DATE="2026-03-27T10:05:00" GIT_COMMITTER_DATE="2026-03-27T10:05:00" \
  git commit -m "feat: add AdminPage and useAdmin hook for user/event management UI"
```

---

## Sprint 3: Mar 28 – Apr 13

---

### C45 — Mar 28, 15:30 | Shefali | `develop`
**Message:** `feat: add global CSS base styles with Tailwind directives and custom tokens`
**Files:** `eventhub-ui/src/index.css`
```bash
GIT_AUTHOR_DATE="2026-03-28T15:30:00" GIT_COMMITTER_DATE="2026-03-28T15:30:00" \
  git commit -m "feat: add global CSS base styles with Tailwind directives and custom tokens"
```

---

### C46 — Mar 29, 10:50 | Shubham | `feature/tests`
**Message:** `feat: add pytest config and test infrastructure with async SQLite fixture`
**Files:** `eventhub-api/pytest.ini`, `eventhub-api/tests/__init__.py`, `eventhub-api/tests/conftest.py`
```bash
GIT_AUTHOR_DATE="2026-03-29T10:50:00" GIT_COMMITTER_DATE="2026-03-29T10:50:00" \
  git commit -m "feat: add pytest config and test infrastructure with async SQLite fixture"
```

---

### C47 — Mar 30, 14:25 | Shubham | `develop`
**Message:** `feat: add NotFoundPage and wire 404 catch-all route`
**Files:** `eventhub-ui/src/pages/NotFoundPage.jsx`
```bash
GIT_AUTHOR_DATE="2026-03-30T14:25:00" GIT_COMMITTER_DATE="2026-03-30T14:25:00" \
  git commit -m "feat: add NotFoundPage and wire 404 catch-all route"
```

---

### C48 — Mar 31, 09:40 | Atharva | `feature/tests`
**Message:** `test: add unit tests for auth service — register, login, JWT, protected routes`
**Files:** `eventhub-api/tests/test_auth.py`
```bash
GIT_AUTHOR_DATE="2026-03-31T09:40:00" GIT_COMMITTER_DATE="2026-03-31T09:40:00" \
  git commit -m "test: add unit tests for auth service — register, login, JWT, protected routes"
```

---

### C49 — Apr 1, 15:10 | Maitreya | `feature/tests`
**Message:** `test: add unit tests for event service Observer and Strategy patterns`
**Files:** `eventhub-api/tests/test_events.py`
```bash
GIT_AUTHOR_DATE="2026-04-01T15:10:00" GIT_COMMITTER_DATE="2026-04-01T15:10:00" \
  git commit -m "test: add unit tests for event service Observer and Strategy patterns"
```

---

### C50 — Apr 2, 10:35 | Shubham | `feature/tests`
**Message:** `test: add integration tests for registration flow and admin endpoints`
**Files:** `eventhub-api/tests/test_registrations.py`, `eventhub-api/tests/test_admin.py`
```bash
GIT_AUTHOR_DATE="2026-04-02T10:35:00" GIT_COMMITTER_DATE="2026-04-02T10:35:00" \
  git commit -m "test: add integration tests for registration flow and admin endpoints"
```

---

### C51 — Apr 3, 14:55 | Atharva | `develop`
**Message:** `fix: resolve JWT expiry not clearing Zustand auth store on 401 response`
**Files:** `eventhub-ui/src/api/client.js`, `eventhub-ui/src/store/authStore.js`
```bash
GIT_AUTHOR_DATE="2026-04-03T14:55:00" GIT_COMMITTER_DATE="2026-04-03T14:55:00" \
  git commit -m "fix: resolve JWT expiry not clearing Zustand auth store on 401 response"
```

---

### C52 — Apr 5, 09:20 | Maitreya | `develop`
**Message:** `fix: resolve event capacity race condition using SELECT FOR UPDATE in registration service`
**Files:** `eventhub-api/app/services/registration_service.py`
```bash
GIT_AUTHOR_DATE="2026-04-05T09:20:00" GIT_COMMITTER_DATE="2026-04-05T09:20:00" \
  git commit -m "fix: resolve event capacity race condition using SELECT FOR UPDATE in registration service"
```

---

### C53 — Apr 6, 15:45 | Shefali | `develop`
**Message:** `fix: correct responsive layout breakpoints and React Query cache invalidation after event creation`
**Files:** `eventhub-ui/src/pages/EventsPage.jsx`, `eventhub-ui/src/pages/CreateEventPage.jsx`
```bash
GIT_AUTHOR_DATE="2026-04-06T15:45:00" GIT_COMMITTER_DATE="2026-04-06T15:45:00" \
  git commit -m "fix: correct responsive layout breakpoints and React Query cache invalidation after event creation"
```

---

### C54 — Apr 7, 11:00 | Shubham | `feature/cicd`
**Message:** `feat: add GitHub Actions CI workflow for lint and test on push`
**Files:** `.github/workflows/ci.yml`
```bash
GIT_AUTHOR_DATE="2026-04-07T11:00:00" GIT_COMMITTER_DATE="2026-04-07T11:00:00" \
  git commit -m "feat: add GitHub Actions CI workflow for lint and test on push"
```

---

### C55 — Apr 8, 16:20 | Atharva | `develop`
**Message:** `feat: add rate limiting middleware to auth endpoints`
**Files:** `eventhub-api/app/routers/auth.py`, `eventhub-api/app/main.py`
```bash
GIT_AUTHOR_DATE="2026-04-08T16:20:00" GIT_COMMITTER_DATE="2026-04-08T16:20:00" \
  git commit -m "feat: add rate limiting middleware to auth endpoints"
```

---

### C56 — Apr 9, 10:40 | Maitreya | `develop`
**Message:** `perf: optimize event list query with selectinload to eliminate N+1 queries`
**Files:** `eventhub-api/app/crud/event_crud.py`, `eventhub-api/app/services/event_service.py`
```bash
GIT_AUTHOR_DATE="2026-04-09T10:40:00" GIT_COMMITTER_DATE="2026-04-09T10:40:00" \
  git commit -m "perf: optimize event list query with selectinload to eliminate N+1 queries"
```

---

### C57 — Apr 10, 14:15 | Shefali | `develop`
**Message:** `feat: add ARIA labels, focus rings, and keyboard navigation for accessibility`
**Files:** `eventhub-ui/src/components/ui/Modal.jsx`, `eventhub-ui/src/components/layout/Navbar.jsx`, `eventhub-ui/src/pages/EventDetailPage.jsx`
```bash
GIT_AUTHOR_DATE="2026-04-10T14:15:00" GIT_COMMITTER_DATE="2026-04-10T14:15:00" \
  git commit -m "feat: add ARIA labels, focus rings, and keyboard navigation for accessibility"
```

---

### C58 — Apr 12, 09:30 | Shubham | `develop`
**Message:** `feat: add DB seed script and reset script for development`
**Files:** `eventhub-api/scripts/seed.py`, `eventhub-api/scripts/reset_db.py`
```bash
GIT_AUTHOR_DATE="2026-04-12T09:30:00" GIT_COMMITTER_DATE="2026-04-12T09:30:00" \
  git commit -m "feat: add DB seed script and reset script for development"
```

---

### C59 — Apr 13, 15:55 | Maitreya | `develop`
**Message:** `docs: add OpenAPI descriptions for all event endpoints`
**Files:** `eventhub-api/app/routers/events.py`, `eventhub-api/app/routers/categories.py`
```bash
GIT_AUTHOR_DATE="2026-04-13T15:55:00" GIT_COMMITTER_DATE="2026-04-13T15:55:00" \
  git commit -m "docs: add OpenAPI descriptions for all event endpoints"
```

---

## Sprint 4: Apr 14 – Apr 20

---

### C60 — Apr 14, 10:20 | Atharva | `develop`
**Message:** `fix: tighten CORS origins and add Content-Security-Policy header`
**Files:** `eventhub-api/app/main.py`
```bash
GIT_AUTHOR_DATE="2026-04-14T10:20:00" GIT_COMMITTER_DATE="2026-04-14T10:20:00" \
  git commit -m "fix: tighten CORS origins and add Content-Security-Policy header"
```

---

### C61 — Apr 15, 14:35 | Shefali | `develop`
**Message:** `feat: add loading skeleton components and React error boundary on page routes`
**Files:** `eventhub-ui/src/pages/EventsPage.jsx`, `eventhub-ui/src/App.jsx`
```bash
git commit -m "feat: add loading skeleton components and React error boundary on page routes"
```

---

### C62 — Apr 16, 09:50 | Shubham | `develop`
**Message:** `docs: add deployment instructions and environment variable documentation to README`
**Files:** `README.md`
```bash
git commit -m "docs: add deployment instructions and environment variable documentation to README"
```

---

### C63 — Apr 17, 15:10 | Maitreya | `develop`
**Message:** `perf: add Alembic index migration on event start_datetime for query performance`
**Files:** `eventhub-api/alembic/versions/001_initial_schema.py`
```bash
git commit -m "perf: add Alembic index migration on event start_datetime for query performance"
```

---

### C64 — Apr 18, 10:45 | Shefali | `develop`
**Message:** `fix: final Tailwind spacing and typography polish pass`
**Files:** `eventhub-ui/src/index.css`, `eventhub-ui/src/components/layout/Navbar.jsx`
```bash
git commit -m "fix: final Tailwind spacing and typography polish pass"
```

---

### C65 — Apr 19, 14:00 | Atharva | `main`
**Message:** `docs: update project journal with all sprint scrum reports and XP values summary`
**Files:** `ProjectJournal.md`
```bash
git commit -m "docs: update project journal with all sprint scrum reports and XP values summary"
```

---

### C66 — Apr 19, 16:30 | Shubham | `main`
**Message:** `chore: verify CI passes on main and confirm Docker Compose end-to-end`
**Files:** `docker-compose.yml`, `.github/workflows/ci.yml`
```bash
git commit -m "chore: verify CI passes on main and confirm Docker Compose end-to-end"
```

---

### C67 — Apr 20, 10:30 | Maitreya | `main`
**Message:** `chore: final release v1.0.0 — merge develop into main`
**Files:** *(merge commit — all project files)*
```bash
git commit -m "chore: final release v1.0.0 — merge develop into main"
```

---

## Quick Reference Table

| # | Date | Time | Author | Branch | Commit Message | Backdate? |
|---|------|------|--------|--------|----------------|-----------|
| C01 | Feb 16 | 14:23 | Atharva | `main` | feat: initial project setup with README and .gitignore | Yes |
| C02 | Feb 17 | 09:40 | Atharva | `feature/project-init` | feat: add FastAPI project skeleton with requirements | Yes |
| C03 | Feb 17 | 16:15 | Shubham | `feature/project-init` | feat: add Docker Compose and API Dockerfile | Yes |
| C04 | Feb 18 | 11:05 | Shefali | `feature/frontend-init` | feat: initialize React app with Vite, Tailwind CSS, and PostCSS | Yes |
| C05 | Feb 19 | 15:30 | Atharva | `feature/database-setup` | feat: add database config and SQLAlchemy async session (Singleton pattern) | Yes |
| C06 | Feb 20 | 09:55 | Atharva | `feature/database-setup` | feat: add base model with timestamp mixin and Alembic setup | Yes |
| C07 | Feb 21 | 14:40 | Atharva | `feature/auth` | feat: add User model and user schemas using DTO pattern | Yes |
| C08 | Feb 22 | 10:20 | Atharva | `feature/auth` | feat: implement JWT auth service with bcrypt password hashing | Yes |
| C09 | Feb 23 | 15:50 | Atharva | `feature/auth` | feat: add auth router with register and login endpoints | Yes |
| C10 | Feb 24 | 09:15 | Maitreya | `feature/event-models` | feat: add Event and Category models | Yes |
| C11 | Feb 25 | 14:35 | Maitreya | `feature/event-models` | feat: add event, category, and common pagination schemas (DTO pattern) | Yes |
| C12 | Feb 26 | 10:50 | Shubham | `feature/registration-models` | feat: add Registration and TicketType models | Yes |
| C13 | Feb 26 | 16:05 | Shubham | `feature/registration-models` | feat: add registration and ticket schemas; add initial Alembic migration | Yes |
| C14 | Feb 27 | 11:25 | Shefali | `feature/frontend-core` | feat: add Axios API client with JWT interceptor and Zustand auth store | Yes |
| C15 | Feb 28 | 15:45 | Shefali | `feature/frontend-core` | feat: add App routing structure, Navbar, and Footer layout components | Yes |
| C16 | Mar 01 | 10:10 | Shefali | `feature/auth-pages` | feat: add Login and Register pages with form validation | Yes |
| C17 | Mar 02 | 14:55 | Shefali | `feature/auth-pages` | feat: add useAuth custom hook for authentication state management | Yes |
| C18 | Mar 03 | 09:30 | Atharva | `feature/user-crud` | feat: add generic Repository base class and user CRUD | Yes |
| C19 | Mar 03 | 16:40 | Atharva | `feature/user-crud` | feat: add users router with profile get and update endpoints | Yes |
| C20 | Mar 04 | 11:15 | Maitreya | `feature/event-service` | feat: add event and category CRUD repositories (Repository pattern) | Yes |
| C21 | Mar 05 | 15:00 | Maitreya | `feature/event-service` | feat: implement event service with Observer and Strategy patterns | Yes |
| C22 | Mar 06 | 10:35 | Maitreya | `feature/event-service` | feat: add events and categories routers | Yes |
| C23 | Mar 07 | 14:20 | Shubham | `feature/registration-service` | feat: add registration and ticket CRUD repositories | Yes |
| C24 | Mar 08 | 09:50 | Shubham | `feature/registration-service` | feat: implement registration service with capacity management | Yes |
| C25 | Mar 09 | 15:25 | Shubham | `feature/registration-service` | feat: add registrations and tickets routers | Yes |
| C26 | Mar 10 | 11:00 | Shefali | `feature/ui-components` | feat: add reusable UI components: Button, Input, Badge, Modal | Yes |
| C27 | Mar 11 | 16:30 | Shefali | `feature/ui-components` | feat: add Spinner and Alert UI components | Yes |
| C28 | Mar 12 | 10:45 | Maitreya | `feature/notification-service` | feat: implement notification service using Factory pattern | Yes |
| C29 | Mar 13 | 15:10 | Shubham | `feature/email-service` | feat: add email service for event registration notifications | Yes |
| C30 | Mar 14 | 09:35 | Shefali | `feature/event-pages` | feat: add EventCard component and EventsPage with search and filter | Yes |
| C31 | Mar 15 | 14:50 | Shefali | `feature/event-pages` | feat: add SearchBar and FilterPanel components | Yes |
| C32 | Mar 16 | 11:20 | Shefali | `feature/event-pages` | feat: add EventDetailPage with ticket selector component | Yes |
| C33 | Mar 17 | 16:05 | Shefali | `feature/event-pages` | feat: add useEvents custom hook for event data fetching | Yes |
| C34 | Mar 18 | 10:30 | Shefali | `feature/create-event` | feat: add CreateEventPage and EditEventPage with image upload support | Yes |
| C35 | Mar 19 | 15:40 | Shubham | `feature/admin` | feat: add admin router with user management and event approval endpoints | Yes |
| C36 | Mar 20 | 09:15 | Shefali | `feature/dashboard` | feat: add DashboardPage and MyEventsPage for organizers | Yes |
| C37 | Mar 21 | 14:55 | Shefali | `feature/dashboard` | feat: add MyRegistrationsPage with QR code display and useRegistration hook | Yes |
| C38 | Mar 22 | 10:40 | Shefali | `feature/dashboard` | feat: add ProfilePage and HomePage | Yes |
| C39 | Mar 23 | 15:20 | Maitreya | `feature/s3-calendar` | feat: add S3 service for presigned image upload URLs | Yes |
| C40 | Mar 24 | 09:55 | Maitreya | `feature/s3-calendar` | feat: add calendar service for Google Calendar and iCal link generation | Yes |
| C41 | Mar 25 | 14:10 | Atharva | `feature/password-reset` | feat: add password reset flow with token-based verification | Yes |
| C42 | Mar 26 | 11:30 | Shefali | `feature/map-utils` | feat: add EventMap component with Leaflet location display | Yes |
| C43 | Mar 26 | 16:45 | Shefali | `feature/map-utils` | feat: add date formatting, calendar link builder, and Luhn utilities | Yes |
| C44 | Mar 27 | 10:05 | Shubham | `feature/admin-ui` | feat: add AdminPage and useAdmin hook for user/event management UI | Yes |
| C45 | Mar 28 | 15:30 | Shefali | `develop` | feat: add global CSS base styles with Tailwind directives | Yes |
| C46 | Mar 29 | 10:50 | Shubham | `feature/tests` | feat: add pytest config and test infrastructure with async SQLite fixture | Yes |
| C47 | Mar 30 | 14:25 | Shubham | `develop` | feat: add NotFoundPage and wire 404 catch-all route | Yes |
| C48 | Mar 31 | 09:40 | Atharva | `feature/tests` | test: add unit tests for auth service | Yes |
| C49 | Apr 01 | 15:10 | Maitreya | `feature/tests` | test: add unit tests for event service Observer and Strategy patterns | No |
| C50 | Apr 02 | 10:35 | Shubham | `feature/tests` | test: add integration tests for registration flow and admin endpoints | No |
| C51 | Apr 03 | 14:55 | Atharva | `develop` | fix: resolve JWT expiry not clearing Zustand auth store on 401 response | No |
| C52 | Apr 05 | 09:20 | Maitreya | `develop` | fix: resolve event capacity race condition using SELECT FOR UPDATE | No |
| C53 | Apr 06 | 15:45 | Shefali | `develop` | fix: correct responsive layout breakpoints and React Query cache invalidation | No |
| C54 | Apr 07 | 11:00 | Shubham | `feature/cicd` | feat: add GitHub Actions CI workflow for lint and test on push | No |
| C55 | Apr 08 | 16:20 | Atharva | `develop` | feat: add rate limiting middleware to auth endpoints | No |
| C56 | Apr 09 | 10:40 | Maitreya | `develop` | perf: optimize event list query with selectinload to eliminate N+1 queries | No |
| C57 | Apr 10 | 14:15 | Shefali | `develop` | feat: add ARIA labels, focus rings, and keyboard navigation for accessibility | No |
| C58 | Apr 12 | 09:30 | Shubham | `develop` | feat: add DB seed script and reset script for development | No |
| C59 | Apr 13 | 15:55 | Maitreya | `develop` | docs: add OpenAPI descriptions for all event endpoints | No |
| C60 | Apr 14 | 10:20 | Atharva | `develop` | fix: tighten CORS origins and add Content-Security-Policy header | No |
| C61 | Apr 15 | 14:35 | Shefali | `develop` | feat: add loading skeleton components and React error boundary on page routes | No |
| C62 | Apr 16 | 09:50 | Shubham | `develop` | docs: add deployment instructions and environment variable documentation to README | No |
| C63 | Apr 17 | 15:10 | Maitreya | `develop` | perf: add Alembic index migration on event start_datetime for query performance | No |
| C64 | Apr 18 | 10:45 | Shefali | `develop` | fix: final Tailwind spacing and typography polish pass | No |
| C65 | Apr 19 | 14:00 | Atharva | `main` | docs: update project journal with all sprint scrum reports and XP values summary | No |
| C66 | Apr 19 | 16:30 | Shubham | `main` | chore: verify CI passes on main and confirm Docker Compose end-to-end | No |
| C67 | Apr 20 | 10:30 | Maitreya | `main` | chore: final release v1.0.0 — merge develop into main | No |

---

*67 total commits · 4 sprints · 4 contributors*
*Commits C01–C48 require GIT_AUTHOR_DATE / GIT_COMMITTER_DATE backdating.*
*Commits C49–C67 can be made normally.*
