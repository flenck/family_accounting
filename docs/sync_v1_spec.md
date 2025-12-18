# Sync v1 Specification

## 1. Overview

This project uses a timestamp-based incremental synchronization model
to support multi-device usage within a household environment.

The sync system is designed for:
- Multiple devices
- Offline-first usage
- Low to medium concurrency
- Predictable conflict resolution

---

## 2. Sync Model

### 2.1 Stateless Server

The backend server is stateless with regard to synchronization.

- The server does NOT store any per-device sync state
- Each client manages its own synchronization progress

The server only responds to queries based on timestamps provided by clients.

---

### 2.2 Client-side Sync State

Each client MUST store a local value called:


This value represents the latest `updated_at` timestamp that the client
has successfully applied.

---

## 3. Data Fields for Sync

Each transaction record contains the following sync-related fields:

| Field        | Description |
|-------------|-------------|
| updated_at  | Timestamp of the last modification (create/update/delete) |
| is_deleted  | Soft-delete flag |

### Rules

- Any create, update, or delete operation MUST update `updated_at`
- Deletions are soft deletions (`is_deleted = true`)

---

## 4. Sync API

### 4.1 Incremental Changes Endpoint


#### Query Parameters

| Name           | Type   | Description |
|----------------|--------|-------------|
| updated_after  | string | Return records updated after this timestamp (YYYY-MM-DD HH:MM:SS) |

#### Behavior

- Returns all transactions where:


#### Query Parameters

| Name           | Type   | Description |
|----------------|--------|-------------|
| updated_after  | string | Return records updated after this timestamp (YYYY-MM-DD HH:MM:SS) |

#### Behavior

- Returns all transactions where:

- Returned records MAY include deleted records (`is_deleted = true`)

---

## 5. Client Sync Procedure

A standard client sync cycle MUST follow these steps:

1. Read local `last_sync_time`
2. Call:

3. Apply all returned changes locally:
- Create or update records
- Remove records where `is_deleted = true`
4. Update `last_sync_time` to the maximum `updated_at` value returned

IMPORTANT:
- `last_sync_time` MUST only be updated AFTER all changes are successfully applied

---

## 6. Deletion Handling

- Records are never physically deleted on the server
- Deletions are represented as:
