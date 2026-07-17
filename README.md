# Family Accounting

A lightweight family bookkeeping system with multi-device sync support.

## Features

- **Multi-device sync** - Timestamp-based incremental synchronization
- **Offline-first** - Works without internet, syncs when connected
- **Soft-delete** - Safe data recovery with `is_deleted` flag
- **Flutter + FastAPI** - Cross-platform frontend with Python backend

## Project Structure

```
family_accounting/
├── app/              # Backend application code
├── docs/             # Documentation
│   ├── sync_v1_spec.md
│   ├── client_sync_flow.md
│   └── client_local_db_schema.md
├── migrations/       # Database migrations
├── init_db.py        # Database initialization
├── migrate_sync_fields.py  # Sync field migration
└── test_db.py        # Database tests
```

## Sync Architecture

The system uses a **stateless server** with **client-managed sync state**:

- Server does NOT store per-device sync progress
- Each client tracks its own `last_sync_time`
- Incremental changes fetched via `updated_after` timestamp
- Soft deletes with `is_deleted` flag

See [docs/sync_v1_spec.md](docs/sync_v1_spec.md) for full specification.

## Recent Updates

- **2026-07-17** - Daily auto-sync: repository up to date, sync-dev branch active, no new changes since 2026-07-16
- **2026-07-16** - Daily auto-sync: pushed pending commit (2026-07-15) to remote sync-dev branch, local and remote now in sync, no new local changes to commit
- **2026-07-15** - Daily auto-sync: GitHub API connection timeout (TLS/GnuTLS recv error -110), network latency detected, local repo up to date with sync-dev branch, no new local changes to commit, previous commits from 2026-07-14 remain pending push
- **2026-07-14** - Daily auto-sync: GitHub API reachable, local repo ahead of remote by 2 commits (2026-07-12, 2026-07-13), push operation timed out (network latency), no new local changes to commit, sync-dev branch active
- **2026-07-13** - Daily auto-sync: GitHub API reachable, local repo ahead of remote by 1 commit (2026-07-12), push operation timed out (network latency), no new local changes to commit, sync-dev branch active
- **2026-07-12** - Daily auto-sync: network issue detected (GitHub empty reply), local repo up to date with remote, sync-dev branch active, no new changes since 2026-07-11
- **2026-07-11** - Daily auto-sync: repository up to date, sync-dev branch active, no new changes since 2026-07-10
- **2026-07-10** - Daily auto-sync: repository up to date, sync-dev branch active, no new changes since 2026-07-08
- **2026-07-08** - Daily auto-sync: repository up to date, sync-dev branch active, no new changes since 2026-07-07
- **2026-07-07** - Daily auto-sync: repository up to date, sync-dev branch active, no new changes since 2026-07-06
- **2026-07-06** - Daily auto-sync: repository up to date, sync-dev branch active, no new changes since 2026-07-05
- **2026-07-05** - Daily auto-sync: repository up to date, sync-dev branch active, no new changes since 2026-07-04
- **2026-07-04** - Daily auto-sync: repository up to date, sync-dev branch active, no new changes since 2026-06-30
- **2026-06-30** - Daily auto-sync: repository up to date, sync-dev branch active, no new changes
- **2026-06-29** - Daily auto-sync: repository up to date, sync-dev branch active
- **2026-06-27** - Auto-sync with GitHub, README added
- **2026-06-26** - Added `category` field to transactions
- **2026-06-26** - Backend + Flutter web connected, transactions API working
- **2026-06-26** - Stable v1 baseline with CRUD and incremental sync

## License

MIT
