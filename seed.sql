DROP DATABASE IF EXISTS feedback_exercise;

CREATE DATABASE feedback_exercise;

CREATE TABLE users (
    username VARCHAR(20) PRIMARY KEY,
    password TEXT NOT NULL,
    email VARCHAR(50) NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL
);