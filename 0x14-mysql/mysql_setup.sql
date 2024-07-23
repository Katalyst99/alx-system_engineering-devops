--mysql setup for web-01 and web-02 servers--
CREATE USER holberton_user@localhost
IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.*
TO 'holberton_user'@'localhost';
