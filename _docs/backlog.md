# Backlog

Small, dependency-ordered slice to get a working MVP on top of the current
`config` project / `chores` app scaffold. Full epic breakdown lives in
[_docs/epics.md](epics.md); this is the near-term subset.

1. [x] Add Django REST Framework + `djangorestframework-simplejwt`; wire up
   `/api/v1/` URL namespace
2. [ ] `Household` and `HouseholdMembership` models (chores app), registered
   in `admin.py`
3. [ ] Invite-by-code: generate code on household creation, join-by-code
   endpoint
4. [ ] `Chore` model — household FK, name, recurrence rule (daily/weekly/every
   N days/monthly), rotation order (member list)
5. [ ] `ChoreInstance` model — chore FK, due_date, assigned_user, status
   (pending/done/overdue)
6. [ ] Management command to generate upcoming `ChoreInstance` rows from each
   chore's recurrence rule
7. [ ] Mark-done endpoint: timestamps completion, advances that chore's
   rotation pointer
8. [ ] Household dashboard endpoint: today's/upcoming chores + assignees +
   overdue flags
9. [ ] Unit tests: rotation advancement (single-member household, member
   removed mid-cycle) and recurrence-to-instance generation
10. [ ] Push notification stub: due-date reminder + +1 day overdue nudge
    (log-only, no real FCM/APNs integration yet)
