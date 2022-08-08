-- 4. MySQL setup test
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'hbnb_test_pwd'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
