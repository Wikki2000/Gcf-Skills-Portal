-- Create database if not exists
CREATE DATABASE IF NOT EXISTS gcf_db;

-- Create user if not exists
CREATE USER IF NOT EXISTS "gcf_user"@"localhost" IDENTIFIED BY "gcf_test_pwd";

-- Grant priviledges
GRANT ALL ON gcf_db.* TO "gcf_user"@"localhost";
