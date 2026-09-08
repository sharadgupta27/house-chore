# Django Backlog — Shared Household Chores App

Backlog assumes Django + Django REST Framework as the API backend for a native mobile client (iOS/Android), per the scope doc's "mobile app" and "basic auth" requirements. Ordered roughly by dependency.

## Epic 1: Project Foundation
- [ ] Initialize Django project, settings split (dev/prod), Postgres config
- [ ] Set up Django REST Framework, base API versioning (`/api/v1/`)
- [ ] Configure CORS/mobile-friendly auth (token or JWT via e.g. `djangorestframework-simplejwt`)
- [ ] Set up push notification service integration point (FCM/APNs) — config only, no logic yet
- [ ] CI pipeline: lint, test, migrations check

## Epic 2: Accounts & Auth
- [ ] `User` model (email or phone identifier, no social login)
- [ ] Signup/login/logout endpoints (basic auth, token issuance)
- [ ] Password reset flow (email or SMS, depending on identifier choice)
- [ ] Device/push-token registration endpoint (link token to user, support multiple devices per user)
- [ ] Single role type — confirm no permission scaffolding beyond "member" (skip admin logic entirely)

## Epic 3: Households
- [ ] `Household` model (name, created_by, created_at)
- [ ] `HouseholdMembership` model (user, household, joined_at) — many-to-many through table
- [ ] Create-household endpoint
- [ ] Invite system: generate invite code/link, expiry, redemption endpoint
- [ ] Join-household-via-code endpoint
- [ ] List households a user belongs to; switch active household in mobile client (backend just needs to scope requests by household_id)
- [ ] Leave-household endpoint

## Epic 4: Chores (Core Model)
- [ ] `Chore` model (household FK, name, recurrence type, recurrence interval, created_by)
- [ ] Recurrence logic: daily / weekly / every N days / monthly — represent as a simple rule field, not a full calendar/RRULE engine
- [ ] CRUD endpoints for chores within a household
- [ ] Chore soft-delete/archive (avoid breaking historical completion logs)

## Epic 5: Per-Chore Rotation
- [ ] `ChoreRotationOrder` model — ordered list of members per chore
- [ ] Logic: on chore creation, default rotation order = household member join order (editable)
- [ ] `ChoreInstance` model (chore FK, due_date, assigned_user, status: pending/done/overdue)
- [ ] Scheduled job (Celery beat or management command + cron) to generate upcoming `ChoreInstance` rows based on recurrence rule
- [ ] Advance rotation pointer only on completion (not on due-date rollover), per "it's my turn again" predictability
- [ ] Handle member added/removed from household — reconcile rotation order gracefully (append new members, skip removed ones without breaking sequence)

## Epic 6: Completion Tracking
- [ ] Mark-chore-done endpoint (timestamp, actor = current user, no approval step)
- [ ] Endpoint to fetch chore history (basic log only — explicitly not a dashboard, just list of past completions)
- [ ] Guard: only assigned user or any household member can mark done? — **needs a decision**, plan doesn't specify; default to "any member can mark done" since there's no admin/verification role

## Epic 7: Nudges & Notifications
- [ ] Scheduled job: on due date, trigger push reminder to assigned user
- [ ] Scheduled job: +1 day overdue, trigger second nudge push
- [ ] Overdue flag computed/stored on `ChoreInstance`, exposed via API for client to render
- [ ] Push-sending service wrapper (FCM/APNs abstraction) with retry/failure logging
- [ ] Notification preferences — out of scope unless requested; skip for v1

## Epic 8: API Surface for Mobile Client
- [ ] Household dashboard endpoint: today's/upcoming chores, who's assigned, overdue flags
- [ ] Chore detail endpoint: recurrence info, rotation order, completion history
- [ ] Pagination/filtering for chore lists (by household, by status)
- [ ] API docs (drf-spectacular/Swagger) for mobile team consumption

## Epic 9: Testing & Hardening
- [ ] Unit tests: rotation advancement logic (edge cases: single-member household, member removal mid-cycle)
- [ ] Unit tests: recurrence-to-instance generation
- [ ] Integration tests: invite/join flow, multi-household isolation (user A can't see household B's chores)
- [ ] Load-test scheduled job performance at moderate household/chore volume

## Explicitly Deferred (per scope doc, do not build)
- Workload-weighted/global fairness rotation
- Automatic reassignment on missed chores, streaks/scoring
- Photo proof or approval workflow for completion
- Admin/member role distinction
- Chat/comments on chores
- Web client, analytics/history dashboards beyond basic log

## Open Question Flagged During Planning
- The scope doc doesn't specify whether any member can mark another member's assigned chore as done, or whether only the assignee can. Recommend confirming before building Epic 6, since it affects the completion endpoint's permission logic.
