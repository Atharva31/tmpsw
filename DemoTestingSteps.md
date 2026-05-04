# EventHub — Demo Testing Steps
**CMPE-202 | Spring 2026**
**Team:** Atharva · Maitreya · Shefali · Shubham

---

## Atharva — Authentication & Backend Verification

### 1. User Registration
- Navigate to `/register`
- Register a new **Attendee** account (name, email, password)
- Verify redirect to home/login on success
- Register a second account as **Organizer** role
- Attempt registration with a duplicate email → expect error message

### 2. Login & JWT Auth
- Log in with the Attendee account → verify JWT stored in browser (Application → Local Storage)
- Log in with the Organizer account → verify role-based nav items appear (e.g., "Create Event", "Dashboard")
- Log in with the Admin account → verify Admin panel link appears
- Log out → confirm token cleared, redirect to login, protected routes inaccessible

### 3. Role-Based Access Control
- While logged out, attempt to navigate to `/dashboard` → expect redirect to login
- While logged in as Attendee, attempt to navigate to `/admin` → expect 403 / redirect
- While logged in as Organizer, attempt to access admin routes → expect 403 / redirect
- Log in as Admin → confirm access to `/admin`

### 4. Network Tab — Backend URL Verification
- Open DevTools → Network tab (Right-click → Inspect → Network)
- Perform a login → show the POST `/api/auth/login` call hitting the cloud backend URL (e.g., `http://<ALB-DNS>/api/...`)
- Perform an event search → show the GET `/api/events` call to the same cloud URL
- Point out the response payload and 200 status code
- Show Authorization header with Bearer token on authenticated requests

### 5. Rate Limiting
- Attempt to submit the login form 6+ times in rapid succession with wrong credentials
- Verify a `429 Too Many Requests` response appears in the Network tab

---

## Maitreya — Event Management & Notifications

### 6. Event Creation (Organizer)
- Log in as Organizer
- Navigate to "Create Event" → fill in: title, description, category, date/time, location (address), capacity, ticket types (free)
- Upload an event banner image
- Submit → verify event appears in "My Events" list with status **Pending Approval**

### 7. Event Editing
- Open an existing own event → click "Edit"
- Change the event title, date, and capacity
- Save → confirm changes reflected on the event detail page

### 8. Calendar Integration
- Open any approved event's detail page
- Click "Add to Google Calendar" → verify the Google Calendar pre-fill URL opens in a new tab with correct event title, date/time, and location
- Click "Download .ics" (iCal) → verify file downloads and opens in Calendar app with correct data

### 9. Notification Service (Email)
- Register for a free event as Attendee
- Check the registered email inbox for a confirmation email with event details and ticket info
- On the organizer side, create an event → verify an organizer confirmation notification is sent
- Show the notification service in code: `app/services/notification_service.py` — Factory pattern creating email vs. in-app channels

### 10. Event Cancellation / Status Observer
- As Organizer, cancel a published event (change status to Cancelled)
- Verify registered attendees receive a cancellation notification email
- Show the Observer pattern in `app/services/event_service.py` — `EventStatusSubject` notifying subscribers on status change

---

## Shefali — Frontend UI & Attendee Experience

### 11. Home Page
- Navigate to `/` — verify featured/upcoming events render with images, titles, dates
- Confirm responsive layout at desktop and mobile viewport sizes (DevTools → Toggle device toolbar)

### 12. Event Discovery — Search
- Navigate to `/events`
- Type a keyword in the search bar → verify results filter in real-time (or on submit)
- Clear the search → verify full list restores

### 13. Event Discovery — Filters & Categories
- Use the category filter (e.g., "Music", "Tech", "Sports") → verify only matching events shown
- Apply a date range filter → verify events outside range disappear
- Apply a location filter → verify filtered results
- Combine category + date filters → verify intersection of results

### 14. Event Detail Page
- Click on any event card → verify navigation to `/events/:id`
- Confirm page shows: full description, schedule (date/time), organizer name, location, capacity/remaining tickets
- Verify event image renders correctly
- Verify the Leaflet map displays the event's location pin (in-person events)
- Pan and zoom the map

### 15. Ticket Selection & Registration
- On the event detail page, select a ticket quantity
- Click "Register" / "Get Tickets" (free event)
- Complete mock registration flow → verify success confirmation screen with ticket/QR code
- Navigate to "My Registrations" → verify the event appears with QR code

### 16. My Registrations Page
- Confirm all registered events are listed
- Click on a registration → verify QR code display is crisp and scannable

### 17. Profile Page
- Navigate to `/profile`
- Edit display name and save → verify updated name appears in Navbar
- Verify form validation: empty name field should show error

---

## Shubham — Registrations, Admin & Cloud Infrastructure

### 18. RSVP Tracking (Organizer)
- Log in as Organizer
- Navigate to Dashboard → "My Events" → click on a specific event
- View the attendee list with names, emails, and registration timestamps
- Verify total registered count matches remaining capacity calculation

### 19. Capacity Enforcement
- Create an event with capacity = 2
- Register 2 attendees (use two different accounts or incognito)
- Attempt a 3rd registration → verify error: "Event is at full capacity" (no over-booking)

### 20. Admin — Event Approval Workflow
- Log in as Admin → navigate to `/admin`
- Verify the pending events queue shows the organizer's newly created event
- Click "Approve" → verify event status changes to **Published** and appears in public event listing
- Create another test event → in Admin, click "Reject" → verify event removed from public listing and organizer notified

### 21. Admin — User Management
- In Admin panel, view the user list
- Change an Attendee's role to Organizer → verify that user now has organizer permissions on next login
- Suspend a test user account → verify that user cannot log in

### 22. Cloud Configuration — AWS Infrastructure
- Open AWS Console → EC2 → show the running API instances (at least 2 for load balancing)
- Show the Application Load Balancer (ALB) — listener rules, target group, and health check status (healthy)
- Navigate to RDS → show the PostgreSQL database instance: endpoint, instance class, Multi-AZ or single-AZ status
- Show S3 bucket → confirm event images uploaded during the demo are present

### 23. Load Balancer Verification
- In the browser Network tab, make several API requests
- Show that requests route to the cloud ALB DNS endpoint
- In AWS, show ALB access logs or target group metrics showing traffic distributed across instances

### 24. Docker / CI Verification (bonus)
- Show `docker-compose.yml` for local dev reference
- Show GitHub Actions CI workflow passing on the main branch (green checkmark)
