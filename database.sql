-- Create the database
CREATE DATABASE IF NOT EXISTS gaming_db;
USE gaming_db;

-- 1. Create the Tournaments table
CREATE TABLE IF NOT EXISTS tournaments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    game_title VARCHAR(255),
    event_date DATE,
    prize_pool VARCHAR(100)
);

-- 2. Create the Players table
CREATE TABLE IF NOT EXISTS players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    tournament_id INT,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tournament_id) REFERENCES tournaments(id) ON DELETE CASCADE
);

-- 3. Insert some seed data so the app isn't empty
INSERT INTO tournaments (name, game_title, event_date, prize_pool) VALUES
('Winter Clash 2024', 'Valorant', '2024-12-15', '$5,000'),
('Grand Slam Masters', 'League of Legends', '2025-01-20', '$10,000'),
('Street Fighter Showdown', 'SF6', '2024-11-05', '$2,500');
