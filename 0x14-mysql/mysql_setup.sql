--mysql setup for web-01 and web-02 servers--
CREATE USER holberton_user@localhost
IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.*
TO 'holberton_user'@'localhost';
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6(id INT, name VARCHAR(256));
INSERT INTO nexus6 (name) VALUES ('Leon');
GRANT SELECT ON tyrell_corp.nexus6
TO holberton_user@localhost;
CREATE USER 'replica_user'@'%'
IDENTIFIED BY 'replica;'
GRANT REPLICATION SLAVE ON *.*
TO 'replica_user'@'%';
GRANT SELECT ON mysql.user
TO holberton_user@localhost;
CREATE USER web-02@34.224.2.3
IDENTIFIED BY 'web-02';
GRANT REPLICATION SLAVE ON *.*
TO web-02@34.224.2.3;
