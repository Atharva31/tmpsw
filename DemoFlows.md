# EventHub — Demo Flows
**CMPE-202 | Spring 2026**
**Team:** Atharva · Maitreya · Shefali · Shubham

> Each flow is a continuous screen-share narrative. Present in the order below for a smooth end-to-end story.

---

## Flow 1 — Atharva: Authentication & Role-Based Access

**Narrative:** Show how the system secures every role and that all traffic goes to the cloud backend.

### Steps

1. Open the app in Chrome. Open DevTools → Network tab (keep it visible throughout).
2. **Register as a new Attendee** — fill name/email/password, submit.
   - In the Network tab, point to `POST /api/auth/register` → cloud ALB URL → 201 response.
3. **Log in** with the new Attendee account.
   - Point to `POST /api/auth/login` → JWT returned in response body.
   - Show Application → Local Storage → JWT token stored.
4. **Show role-based nav** — Attendee sees "Browse Events", "My Registrations" only.
5. **Log out** → token cleared → attempt to visit `/dashboard` directly → redirected to login.
6. **Log in as Organizer** → show "Create Event" and "My Events" nav items appear.
7. **Log in as Admin** → show Admin panel link.
8. Attempt to visit `/admin` as Organizer → confirm access denied.
9. Close by highlighting: JWT is verified on every API call (show Authorization: Bearer header in Network tab on any request).

**Duration:** ~4 minutes

---

## Flow 2 — Shefali: Attendee Discovery & Registration

**Narrative:** A first-time user finds an event, explores it, registers, and saves it to their calendar.

### Steps

1. Log in as the Attendee account.
2. Land on the **Home Page** — point out featured events grid, hero section.
3. Navigate to **Browse Events (`/events`)**.
4. **Search** — type "Tech" in the search bar → results filter to tech events.
5. **Category filter** — click "Music" category → show only music events.
6. **Date filter** — set a date range → results narrow further.
7. Click on an event card → **Event Detail Page**.
   - Scroll through: title, description, organizer info, date/time/location, capacity remaining.
   - Show the **Leaflet map** with the venue pin — pan and zoom.
8. **Select ticket** — choose quantity 1 (free ticket) → click "Register".
9. Registration confirmation screen — show the **QR code** ticket.
10. Navigate to **My Registrations** → confirm event listed with QR code.
11. Back on the event detail page: click **"Add to Google Calendar"** → Google Calendar pre-fill opens in new tab with correct data.

**Duration:** ~5 minutes

---

## Flow 3 — Maitreya: Organizer Event Management & Notifications

**Narrative:** An organizer creates an event, watches it get approved, manages attendees, and sees notifications fire.

### Steps

1. Log in as Organizer.
2. Navigate to **Create Event**.
   - Fill in: title ("AI Workshop"), category (Tech), description, date/time (future), location (SJSU Engineering Building), capacity (10), ticket type (Free).
   - Upload a banner image → show S3 upload happening in Network tab (`PUT` to S3 presigned URL).
   - Submit → event created with status **Pending Approval**.
3. Navigate to **My Events** → confirm event shows "Pending" badge.
4. Switch to Admin account (separate tab) → approve the event → status becomes **Published**.
5. Switch back to Organizer → refresh My Events → status shows **Published**.
6. Click into the event → **Attendee List** — show RSVP tracking table (empty initially).
7. Open a new incognito window → log in as Attendee → register for "AI Workshop".
8. Back on Organizer dashboard → refresh attendee list → attendee appears with name, email, timestamp.
9. Show **email inbox** → registration confirmation email received by the attendee.
10. As Organizer, **cancel the event** (change status to Cancelled).
    - Show Observer pattern briefly in code: `EventStatusSubject` in `event_service.py`.
    - Switch to attendee email → cancellation notification received.
11. Briefly show the **Calendar Service** (`calendar_service.py`) — Google Calendar and iCal link generation logic.

**Duration:** ~6 minutes

---

## Flow 4 — Shubham: Admin Moderation & Cloud Infrastructure

**Narrative:** Show the admin approval workflow in action, then prove the deployment is real cloud infrastructure.

### Steps

**Part A — Admin Moderation**

1. Log in as Admin → navigate to `/admin`.
2. **Event Approval Queue** — show pending event from the Organizer flow above (or a fresh one).
   - Click "Approve" → event goes live.
   - Create a second test event (as Organizer) → in Admin, click "Reject" → confirm removed from public listing.
3. **User Management** — show user table: list of all users, roles, status.
   - Promote an Attendee to Organizer → verify role updates.
   - Suspend a test user → show they cannot log back in.

**Part B — Cloud Infrastructure**

4. Open **AWS Console** (pre-logged in, share screen).
5. **EC2 → Instances** — show running API server instances (2+), status = running, public DNS.
6. **EC2 → Load Balancers** — click the Application Load Balancer:
   - Show DNS name (same URL as in Network tab from Flow 1).
   - Show Target Group → both instances status **healthy**.
   - Show Listener Rules routing to the target group.
7. **RDS → Databases** — show the PostgreSQL instance:
   - Endpoint, instance class, status = available.
   - Show it is in a private subnet (not publicly accessible directly).
8. **S3 → Buckets** — show `eventhub-assets` bucket → open the `events/` prefix → confirm banner images from the demo are stored.
9. **Return to browser Network tab** — make a fresh API call (e.g., load events list) → highlight the request URL matches the ALB DNS shown in AWS console.
10. Wrap up: "Backend on AWS EC2 behind ALB → PostgreSQL on RDS → images on S3 — fully cloud-deployed."

**Duration:** ~5 minutes

---

## Combined Run Order

| Order | Presenter | Flow | Duration |
|-------|-----------|------|----------|
| 1 | Atharva | Authentication & Role-Based Access | ~4 min |
| 2 | Shefali | Attendee Discovery & Registration | ~5 min |
| 3 | Maitreya | Organizer Event Management & Notifications | ~6 min |
| 4 | Shubham | Admin Moderation & Cloud Infrastructure | ~5 min |
| **Total** | | | **~20 min** |

---

## Pre-Demo Checklist

- [ ] Cloud backend is up; health check endpoint returns 200
- [ ] At least 3 seeded events exist (one per category) with images
- [ ] Three accounts pre-created: `attendee@test.com`, `organizer@test.com`, `admin@test.com`
- [ ] Admin account credentials available to all presenters
- [ ] S3 bucket has at least one test image to show
- [ ] AWS Console open and logged in before demo starts
- [ ] Email inbox (for notification demo) accessible and cleared of old test emails
- [ ] Google Calendar tab ready for calendar integration demo
- [ ] Browser DevTools Network tab open and cleared before Flow 1
