-- Migration 001
-- Add category field to transactions table

ALTER TABLE transactions
ADD COLUMN category TEXT NOT NULL DEFAULT '未分类';