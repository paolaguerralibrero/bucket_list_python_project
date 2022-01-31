DROP TABLE IF EXISTS visit;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS countries;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    continent VARCHAR(255),
    flag VARCHAR(255)
);

CREATE TABLE visit (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    visited BOOLEAN
)