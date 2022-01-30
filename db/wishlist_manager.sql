DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS countries;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255)
);