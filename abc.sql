-- Active: 1771784571765@@127.0.0.1@3306@sqlbycodewithharry
CREATE TABLE life (
    happiness VARCHAR(50),
    peace VARCHAR(50),
    love VARCHAR(50),
    regrets INT,
    stress INT,
    money INT,
    needs INT,
    health VARCHAR(20)
);

INSERT INTO life
(happiness, peace, love, regrets, stress, money, needs, health)
VALUES
('Unlimited', 'Finally', 'Mom ❤️', 0, 0, 50000, 30000, 'good'),

('Medium', 'Loading...', 'None 💔', 0, 0, 500, 1000, 'good'),

('Monday', '404 Not Found', 'SQL ❤️', 0, 0, 100000, 50000, 'good'),

('High', 'Chill', 'Coffee ☕', 0, 0, 2000, 1500, 'good'),

('Exam Result', 'Gone', 'Sleep 😴', 0, 0, 1000000, 100, 'good');

SELECT happiness, peace, love
FROM life
WHERE regrets = 0
AND stress = 0
AND money >= needs
AND health = 'good';