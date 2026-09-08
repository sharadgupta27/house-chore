# Shared Household Chores App — Scope Document

## Target Users
Multi-household, general-purpose tool — not limited to a single household. Anyone can create or join a household.

## Platform
**Mobile app** (iOS/Android native feel).

## Chore Assignment Model
**Rotating** — chores automatically cycle through household members.

## Rotation Logic
**Per-chore rotation** — each chore maintains its own independent sequence (A → B → C → A...), rather than a global fairness system across all chores.

*Why:* Simpler to implement and reason about. Global fairness would require weighting chores by effort/time, which adds complexity beyond MVP scope. Per-chore rotation is predictable and easy for users to understand (e.g., "it's my turn for trash again").

## Missed/Late Chore Handling
**Nudges/Reminders** — escalating notifications to the assigned person. No automatic reassignment, no scoring/streaks.

## Chore Structure
**Scheduled recurrence** — each chore has its own frequency (daily/weekly/every N days/monthly).

## Chore Creation
**Free-form + recurrence picker** — users name any chore and set its recurrence. No fixed template list or forced categorization.

*Why:* Keeps MVP flexible without building out a categorization system that wasn't requested.

## Household Structure
**Multiple households per install, invite-based.** Each household has its own member list and chore set. Users join via invite code/link.

*Why:* Required to support "anyone can use it" — needs to scale beyond one group.

## Notifications
**Push notifications, escalating:**
- Reminder on due date
- Second nudge if overdue by 1 day
- Visible "overdue" flag after that

## Completion Tracking
**Simple checkmark, timestamped.** Person marks the chore done; app logs who and when.

*Why:* Keeps friction low. No photo proof or approval step — avoids scope creep into "verification" features.

## Accounts & Permissions
**Basic auth** (email or phone) + local push tokens. No social login. Single role type (member) — no admin/member distinction in v1.

## Out of Scope for v1
- Streaks / gamification
- Workload-weighting or "smart" assignment
- Chat/comments on chores
- Web version
- Analytics/history dashboards

## Summary
A lean, buildable MVP: multi-household, mobile-first, recurring chores, per-chore rotation, and escalating push nudges for accountability — without added complexity from fairness algorithms, verification, or admin roles.
