CREATE TABLE User (
    user_id VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE Role (
    role_id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (role_id)
);

CREATE TABLE User_Role (
   user_id VARCHAR(50) NOT NULL,
   role_id BIGINT NOT NULL,
   PRIMARY KEY (user_id, role_id),
   FOREIGN KEY (user_id) REFERENCES User (user_id),
   FOREIGN KEY (role_id) REFERENCES Role (role_id)
);