# EventHub — Project Journal
**CMPE-202: Software Systems Engineering | Spring 2026**
**Team:** Atharva, Maitreya, Shefali, Shubham

---

## Table of Contents
1. [Team Component Ownership](#team-component-ownership)
2. [Weekly Scrum Reports](#weekly-scrum-reports)
3. [XP Core Values](#xp-core-values)
4. [Scrum Backlog](#scrum-backlog)
5. [Burndown Chart](#burndown-chart)

---

## Team Component Ownership

| Team Member | Owned Component | Design Patterns |
|-------------|----------------|-----------------|
| **Atharva** | Authentication & User Management (`app/routers/auth.py`, `app/services/auth_service.py`, `app/database.py`, `app/config.py`, `app/dependencies.py`, `app/crud/user_crud.py`) | Singleton (DB session via `lru_cache`), Dependency Injection |
| **Maitreya** | Event Management & Notifications (`app/routers/events.py`, `app/services/event_service.py`, `app/services/notification_service.py`, `app/services/s3_service.py`, `app/services/calendar_service.py`) | Factory (notification channels), Observer (`EventStatusSubject`), Strategy (sort/filter) |
| **Shefali** | Frontend Application (`eventhub-ui/src/` — all pages, components, hooks, store) | Custom Hook Pattern (`useAuth`, `useEvents`, `useRegistration`, `useAdmin`) |
| **Shubham** | Registrations, Tickets, Admin & Infrastructure (`app/routers/registrations.py`, `app/services/registration_service.py`, `app/routers/admin.py`, `docker-compose.yml`, `tests/`) | Repository (base CRUD), DTO (schemas) |

---

## Weekly Scrum Reports

---

### Week 1 — Feb 16–22, 2026
**Sprint 1 kickoff: Project setup, environment, initial data models**

#### Atharva
- **Completed:** Initialized GitHub repository, added README and `.gitignore`. Set up FastAPI project skeleton with `requirements.txt`. Implemented `app/database.py` (async SQLAlchemy engine + session factory using `lru_cache` Singleton) and `app/config.py` (Pydantic settings). Added `app/models/base.py` with `TimestampMixin`. Added `User` model (`app/models/user.py`) and user schemas (`app/schemas/user.py`) using DTO pattern.
- **Planning next:** Complete JWT auth service, `app/dependencies.py`, and the `/auth` router.
- **Blocked:** None.

#### Maitreya
- **Completed:** Reviewed project requirements and PRD. Contributed to initial FastAPI app structure (`app/main.py`). Started drafting `Event` and `Category` models.
- **Planning next:** Finalize `app/models/event.py`, `app/models/category.py`, and corresponding schemas.
- **Blocked:** Waiting on `base.py` model from Atharva (resolved by Feb 20).

#### Shefali
- **Completed:** Initialized React + Vite project (`eventhub-ui/`), configured Tailwind CSS, PostCSS. Reviewed component structure and decided on page-based routing with React Router v6.
- **Planning next:** Set up Axios API client, Zustand auth store, `App.jsx` routing, and layout components (Navbar, Footer).
- **Blocked:** None.

#### Shubham
- **Completed:** Set up `docker-compose.yml` with PostgreSQL + API + UI services. Added `Dockerfile` for the API. Drafted `Registration` and `TicketType` model schemas.
- **Planning next:** Finalize registration/ticket models and schemas once Event model is merged.
- **Blocked:** Waiting on `Event` model from Maitreya (expected Feb 24).

---

### Week 2 — Feb 23 – Mar 1, 2026
**Auth implementation, frontend foundation, registration models**

#### Atharva
- **Completed:** Implemented `app/services/auth_service.py` (JWT token generation/verification, bcrypt password hashing). Added `app/dependencies.py` (FastAPI DI for current user extraction). Added `app/routers/auth.py` with `/register` and `/login` endpoints. Registered all routers in `app/main.py`.
- **Planning next:** Add `app/crud/user_crud.py` (Repository pattern) and `/users` profile endpoints.
- **Blocked:** None.

#### Maitreya
- **Completed:** Added `app/models/event.py` and `app/models/category.py`. Added `app/schemas/event.py`, `app/schemas/category.py`, `app/schemas/common.py` (pagination schema).
- **Planning next:** Implement event CRUD repository and event service with Observer + Strategy patterns.
- **Blocked:** None.

#### Shefali
- **Completed:** Added `eventhub-ui/src/api/client.js` (Axios with JWT interceptor). Added `eventhub-ui/src/store/authStore.js` (Zustand). Added `App.jsx` with protected route logic, `Navbar.jsx`, `Footer.jsx`. Added `LoginPage.jsx`, `RegisterPage.jsx`.
- **Planning next:** Add `useAuth` custom hook, `EventsPage`, and reusable UI components.
- **Blocked:** None.

#### Shubham
- **Completed:** Added `app/models/registration.py`, `app/models/ticket_type.py`. Added `app/schemas/registration.py`, `app/schemas/ticket.py`. Added Alembic initial migration `001_initial_schema.py`.
- **Planning next:** Implement registration CRUD, registration service, and registrations/tickets routers.
- **Blocked:** None.

---

### Week 3 — Mar 2–8, 2026
**CRUD repositories, event service, notification foundation**

#### Atharva
- **Completed:** Added `app/crud/base_crud.py` (generic Repository base class), `app/crud/user_crud.py`, and `app/routers/users.py` (GET/PATCH profile, change password).
- **Planning next:** Add password reset token flow.
- **Blocked:** None.

#### Maitreya
- **Completed:** Added `app/crud/event_crud.py` (Repository pattern, complex filter queries), `app/crud/category_crud.py`. Implemented `app/services/event_service.py` with `EventStatusSubject` (Observer pattern) and `EventSortStrategy` (Strategy pattern). Added `app/routers/events.py` and `app/routers/categories.py`.
- **Planning next:** Implement `app/services/notification_service.py` using Factory pattern for notification channels.
- **Blocked:** None.

#### Shefali
- **Completed:** Added `useAuth.js` custom hook. Added reusable UI components: `Button.jsx`, `Input.jsx`, `Badge.jsx`, `Modal.jsx`, `Spinner.jsx`, `Alert.jsx`.
- **Planning next:** Build `EventCard`, `EventsPage`, `SearchBar`, `FilterPanel`.
- **Blocked:** Needs events API to be stable before wiring data — coordinated with Maitreya.

#### Shubham
- **Completed:** Implemented `app/crud/registration_crud.py`, `app/crud/ticket_crud.py`. Added `app/services/registration_service.py` (capacity management, ticket inventory). Added `app/routers/registrations.py`, `app/routers/tickets.py`.
- **Planning next:** Add email service and admin router.
- **Blocked:** None.

---

### Week 4 — Mar 9–15, 2026
**Notification service, event UI pages, ticket selector**

#### Atharva
- **Completed:** Team sync on API contract — aligned request/response schemas with Shefali's frontend expectations. Reviewed Maitreya's Observer pattern implementation.
- **Planning next:** Add password reset endpoint and frontend page.
- **Blocked:** None.

#### Maitreya
- **Completed:** Implemented `app/services/notification_service.py` (Factory pattern — creates `EmailNotifier`, `InAppNotifier` based on channel type). Wired Observer into event service so status changes dispatch notifications. Began `app/services/s3_service.py` for image uploads.
- **Planning next:** Complete S3 service and `app/services/calendar_service.py`.
- **Blocked:** AWS credentials needed from Atharva — resolved mid-week.

#### Shefali
- **Completed:** Added `EventCard.jsx`, `EventsPage.jsx` (with search + filter), `SearchBar.jsx`, `FilterPanel.jsx`. Added `EventDetailPage.jsx` with ticket purchase flow. Added `TicketSelector.jsx`. Added `useEvents.js` custom hook.
- **Planning next:** Add `CreateEventPage`, `EditEventPage`, `DashboardPage`, `MyEventsPage`.
- **Blocked:** None.

#### Shubham
- **Completed:** Added `app/services/email_service.py` (SMTP with template rendering). Added `app/routers/admin.py` (user ban/unban, event approval, stats endpoints).
- **Planning next:** Build `AdminPage` and `useAdmin` hook on frontend. Set up test infrastructure.
- **Blocked:** None.

---

### Week 5 — Mar 16–22, 2026
**Event management pages, dashboard, admin UI**

#### Atharva
- **Completed:** Added password reset token generation in auth service. Added `ResetPasswordPage.jsx` on frontend (coordinated with Shefali). Reviewed registration service for correctness.
- **Planning next:** Begin writing unit tests for auth service.
- **Blocked:** None.

#### Maitreya
- **Completed:** Completed `app/services/s3_service.py` (presigned URL upload flow). Completed `app/services/calendar_service.py` (Google Calendar + iCal link generation). Both integrated into events router.
- **Planning next:** Write unit tests for event service patterns. Optimize queries with eager loading.
- **Blocked:** None.

#### Shefali
- **Completed:** Added `CreateEventPage.jsx`, `EditEventPage.jsx` (with image upload via S3 presigned URL). Added `DashboardPage.jsx`, `MyEventsPage.jsx`, `MyRegistrationsPage.jsx`, `QRCodeDisplay.jsx`, `useRegistration.js`, `ProfilePage.jsx`. Added `index.css` with Tailwind base styles.
- **Planning next:** Add `EventMap.jsx`, utility functions, and `useAdmin.js`/`AdminPage.jsx`.
- **Blocked:** None.

#### Shubham
- **Completed:** Added `AdminPage.jsx` and `useAdmin.js` with user management and event approval UI. Added `NotFoundPage.jsx` and 404 routing.
- **Planning next:** Set up `pytest.ini`, `tests/conftest.py`, and write integration tests for registration flow.
- **Blocked:** None.

---

### Week 6 — Mar 23–29, 2026
**Map component, utilities, tests setup, UI polish**

#### Atharva
- **Completed:** Added `tests/test_auth.py` covering register, login, JWT validation, and protected route access. Set up `pytest.ini` config.
- **Planning next:** Fix edge cases found in testing: duplicate email, expired token handling.
- **Blocked:** None.

#### Maitreya
- **Completed:** Finalized `s3_service.py` and `calendar_service.py` integration. Added `tests/test_events.py` for event CRUD and sort strategies.
- **Planning next:** Fix event capacity race condition identified during testing.
- **Blocked:** None.

#### Shefali
- **Completed:** Added `EventMap.jsx` (Leaflet integration). Added `utils/formatDate.js`, `utils/buildCalendarLink.js`, `utils/luhn.js` (ticket number validation). Added global `index.css`. Fixed responsive layout issues on mobile breakpoints.
- **Planning next:** Final accessibility pass — ARIA labels, keyboard navigation.
- **Blocked:** None.

#### Shubham
- **Completed:** Added `tests/conftest.py` (async test client, in-memory SQLite DB fixture). Added `tests/test_registrations.py` and `tests/test_admin.py`. Added seed script (`scripts/seed.py`) and DB reset script (`scripts/reset_db.py`).
- **Planning next:** Add GitHub Actions CI/CD workflow. Add health check endpoint.
- **Blocked:** None.

---

### Week 7 — Mar 30 – Apr 5, 2026
**Bug fixes from testing, CI/CD setup**

#### Atharva
- **Completed:** Fixed JWT token expiry handling — refresh logic wasn't clearing the Zustand store on 401. Fixed duplicate email validation returning 500 instead of 422. Added rate limiting middleware to auth endpoints.
- **Planning next:** Final security audit: CORS configuration review, input sanitization.
- **Blocked:** None.

#### Maitreya
- **Completed:** Fixed event capacity race condition (added `SELECT FOR UPDATE` in registration service). Updated Observer to correctly unsubscribe when event is cancelled. Added API docstrings for OpenAPI auto-generation.
- **Planning next:** Database query optimization with eager loading for event list endpoint.
- **Blocked:** None.

#### Shefali
- **Completed:** Added accessibility improvements: ARIA labels on all interactive elements, focus rings, keyboard-navigable modal. Fixed React Query cache invalidation bug after event creation.
- **Planning next:** Final UI polish — loading skeletons, error boundaries.
- **Blocked:** None.

#### Shubham
- **Completed:** Added `.github/workflows/ci.yml` (GitHub Actions: lint + test on push). Added `/health` endpoint to API. Verified Docker Compose works end-to-end.
- **Planning next:** Performance testing, monitoring setup.
- **Blocked:** None.

---

### Week 8 — Apr 6–12, 2026
**Performance optimization, security, documentation**

#### Atharva
- **Completed:** Completed security audit — tightened CORS origins, added `Content-Security-Policy` header, sanitized event description input. Reviewed all endpoints for authorization gaps.
- **Planning next:** Final review of test coverage. Update README deployment instructions.
- **Blocked:** None.

#### Maitreya
- **Completed:** Optimized event list query — added `selectinload` for categories and ticket types, reducing N+1 queries. Added Alembic index migration for `event.start_datetime`. Completed OpenAPI descriptions for all event endpoints.
- **Planning next:** Final review of design pattern documentation for submission.
- **Blocked:** None.

#### Shefali
- **Completed:** Added loading skeleton components. Added React error boundary around page routes. Improved form error messages. Minor Tailwind spacing/typography polish pass.
- **Planning next:** Final cross-browser testing. Update project journal frontend section.
- **Blocked:** None.

#### Shubham
- **Completed:** Ran k6 load test against events endpoint — resolved timeout on unindexed query (fixed by Maitreya). Verified all 4 test files pass in CI. Documented deployment steps in README.
- **Planning next:** Deployment preparation — finalize Docker images, confirm environment variables.
- **Blocked:** None.

---

### Week 9 — Apr 13–20, 2026
**Final polish, deployment prep, submission**

#### Atharva
- **Completed:** Final README updates. Recorded demo video walkthrough of auth + user management flows. Updated project journal.
- **Planning next:** Final submission review.
- **Blocked:** None.

#### Maitreya
- **Completed:** Final merge of `develop` into `main`. Verified all design patterns are documented in README. Updated project journal with sprint 4 entry.
- **Planning next:** Submission.
- **Blocked:** None.

#### Shefali
- **Completed:** Final cross-browser test (Chrome, Firefox, Safari). Verified mobile layout on 375px viewport. Updated `index.css` final pass.
- **Planning next:** Submission.
- **Blocked:** None.

#### Shubham
- **Completed:** Deployment verification on Docker Compose. Added final environment variable documentation. Verified CI passes on `main`. Updated project journal.
- **Planning next:** Submission.
- **Blocked:** None.

---

## XP Core Values

### 1. Communication

Throughout the project, the team maintained consistent communication to ensure everyone stayed aligned without creating unnecessary overhead.

**How we practiced Communication:**

- **Weekly Scrum Standups:** Every week the team held a structured standup answering the three Scrum questions. This kept everyone aware of progress and blockers without requiring lengthy meetings.
- **Shared API Contract Early:** In Week 3, Atharva and Shefali held a focused sync to align the frontend's expected request/response shapes with the backend schemas (DTOs). This prevented mismatches that would have caused rework later.
- **Cross-component Coordination:** When Maitreya's `EventStatusSubject` (Observer pattern) needed to integrate with Shubham's `registration_service.py`, both team members communicated the interface contract explicitly before implementation, keeping the integration clean.
- **PR-based Code Review:** Every feature branch was reviewed by at least one other team member before merging to `develop`. This surfaced issues early (e.g., the capacity race condition) before they reached integration.
- **Shared Design Decisions:** Major decisions — choosing Zustand over Redux, using `selectinload` for query optimization, the Factory approach in `notification_service.py` — were communicated in the team channel with brief rationale so everyone understood the "why," not just the "what."
- **Unblocking Quickly:** When Shubham was blocked on the Event model (Week 1) and Maitreya was blocked on AWS credentials (Week 4), the blockers were surfaced in standup and resolved within 1–2 days rather than stalling silently.

The team treated communication as a tool to reduce waste — not to create process. Short, targeted exchanges replaced long meetings.

---

### 2. Simplicity

The team consistently chose the simplest design that satisfied the current requirement, avoiding over-engineering and speculative abstraction.

**How we practiced Simplicity:**

- **4-Layer Architecture (No More, No Less):** The backend follows a strict Router → Service → CRUD → Database layering. There are no unnecessary abstraction layers. Each layer has exactly one responsibility.
- **Generic Repository Base:** `app/crud/base_crud.py` provides a simple generic CRUD base, eliminating copy-paste boilerplate across `user_crud.py`, `event_crud.py`, `registration_crud.py`, etc., without introducing a complex ORM wrapper or query builder.
- **Singleton via `lru_cache`:** Rather than implementing a hand-rolled Singleton class, `app/config.py` and `app/database.py` use Python's built-in `@lru_cache` decorator — the simplest correct solution.
- **Strategy Pattern Without Class Explosion:** `EventSortStrategy` in `event_service.py` uses callable strategies passed as parameters rather than a deep class hierarchy. New sort orders can be added in one line.
- **Frontend: Hooks Over HOCs:** Shefali chose custom hooks (`useAuth`, `useEvents`, `useRegistration`, `useAdmin`) over Higher-Order Components or complex context providers. Hooks compose cleanly and remain easy to understand.
- **Zustand Over Redux:** The team chose Zustand for frontend state management — it provides the same capabilities as Redux with a fraction of the boilerplate. The auth store (`authStore.js`) is ~40 lines.
- **Docker Compose for Local Dev:** Rather than introducing Kubernetes or Helm for local development, the team uses a single `docker-compose.yml` that spins up the full stack in one command.
- **Avoiding Premature Optimization:** The team deferred query optimization (eager loading, DB indexes) until Week 8, after performance testing revealed actual bottlenecks, rather than optimizing speculatively.

The "simplest thing that works" rule prevented scope creep and kept the codebase approachable for all four contributors.

---

## Scrum Backlog

The team's Scrum backlog is maintained in a Google Sheet tracking user stories, story points, sprint assignment, and completion status.

**Backlog Sheet:** [EventHub Scrum Backlog — Google Sheets](#) *(link to be added by team)*

**Sprint Summary:**

| Sprint | Dates | Stories Planned | Stories Completed | Velocity |
|--------|-------|-----------------|-------------------|----------|
| Sprint 1 | Feb 16 – Mar 6 | 12 | 12 | 34 pts |
| Sprint 2 | Mar 7 – Mar 27 | 14 | 13 | 38 pts |
| Sprint 3 | Mar 28 – Apr 13 | 10 | 10 | 28 pts |
| Sprint 4 | Apr 14 – Apr 20 | 5 | 5 | 12 pts |

**Key User Stories by Sprint:**

*Sprint 1:*
- As a user, I can register and log in with email/password (8 pts)
- As a user, I can view a list of events (5 pts)
- As a developer, the database schema is created via Alembic migration (3 pts)
- As a developer, Docker Compose spins up the full stack (3 pts)
- As a developer, JWT auth middleware protects private endpoints (5 pts)
- As a user, I can browse the frontend app (React, Tailwind) (5 pts)

*Sprint 2:*
- As an organizer, I can create, edit, and delete events (8 pts)
- As an attendee, I can register for an event and receive a ticket (8 pts)
- As a user, I can search and filter events by category/date/location (5 pts)
- As an organizer, I can upload an event banner image (5 pts)
- As an admin, I can manage users and approve/reject events (5 pts)
- As an attendee, I can view my QR code ticket (3 pts)
- As a user, I receive email notifications on registration (5 pts) *(partial)*

*Sprint 3:*
- As a developer, auth/event/registration/admin flows have passing tests (8 pts)
- As a user, the app works correctly on mobile (5 pts)
- As a developer, CI/CD runs tests on every push (5 pts)
- As a developer, event list queries are optimized (3 pts)
- As a user, I can reset my password via email (3 pts)
- As a user, I can add an event to Google Calendar (3 pts) *(carry from Sprint 2)*

*Sprint 4:*
- As a developer, the project is deployable with Docker Compose (3 pts)
- As a team, the Project Journal is complete (5 pts)
- As a developer, API documentation is complete via OpenAPI (3 pts)

---

## Burndown Chart

The team's burndown chart tracks remaining story points per sprint day.

**Burndown Sheet:** [EventHub Burndown Chart — Google Sheets](#) *(link to be added by team)*

**Sprint 1 Burndown Summary:** Started at 34 pts; steady burn of ~2 pts/day; completed on schedule by Mar 6.

**Sprint 2 Burndown Summary:** Started at 38 pts; slight spike mid-sprint (email service scope expanded); 1 story (calendar integration) carried to Sprint 3; otherwise on track.

**Sprint 3 Burndown Summary:** Started at 28 pts (27 new + 1 carried); resolved capacity race condition mid-sprint caused a 2-day delay; recovered by adding bandwidth from Atharva to unblock Maitreya.

**Sprint 4 Burndown Summary:** Final 12 pts completed smoothly over 5 days.

---

*Project Journal maintained by all team members. Last updated: Apr 20, 2026.*
