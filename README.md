# House Chore

A shared household chores app. Multiple households, mobile-first, recurring
chores with per-chore rotation among members, and escalating push nudges for
accountability.

Built as part of the [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)
homework 1, with an AI coding agent doing most of the implementation from a
plan (see [`_docs/plan.md`](_docs/plan.md)).

## Scope

- Multi-household, invite-based — anyone can create or join a household.
- Chores rotate per-chore (A → B → C → A...), advancing only on completion.
- Each chore has its own recurrence: daily / weekly / every N days / monthly.
- Completion is a simple timestamped checkmark — no photo proof or approval step.
- Missed chores get escalating push reminders, not automatic reassignment.
- Single role type (member) — no admin/member distinction in v1.

See [_docs/plan.md](_docs/plan.md) for the full scope document.

## Backend

Planned as Django + Django REST Framework, serving a native mobile client
(iOS/Android). See [_docs/epics.md](_docs/epics.md) for the epic-by-epic
build plan, or [_docs/backlog.md](_docs/backlog.md) for the near-term task
list.

## Out of scope for v1

Streaks/gamification, workload-weighted assignment, chat/comments on chores,
web version, analytics/history dashboards.
