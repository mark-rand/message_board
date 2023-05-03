-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS mode;

CREATE TABLE mode (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR2 UNIQUE NOT NULL,
  json TEXT UNIQUE NOT NULL
);
