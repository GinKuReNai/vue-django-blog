CREATE DATABASE IF NOT EXISTS app_db CHARACER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER IF NOT EXISTS 'ginkurenai'@'%' IDENTIFIED BY 'KogaAkito1215@ginkurenai';
GRANT ALL PRIVILEGES ON app_db.* TO 'ginkurenai'@'%';
FLUSH PRIVILEGES;