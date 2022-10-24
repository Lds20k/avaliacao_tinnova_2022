-- SQLite
PRAGMA foreign_keys = ON;

CREATE TABLE brand(
    id   INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(30) NOT NULL
);

CREATE TABLE vehicle(
    id          INTEGER PRIMARY KEY NOT NULL,
    name        VARCHAR(30) NOT NULL,
    brandid     INTEGER NOT NULL,
    color       VARCHAR(30) NOT NULL,
    year        INTEGER NOT NULL,
    description TEXT NOT NULL,
    sold        BOOLEAN NOT NULL,
    created     DATETIME NOT NULL,
    updated     DATETIME NOT NULL,
    FOREIGN KEY(brandid) REFERENCES brand(id)
);

INSERT INTO brand (name) VALUES ('toyota');
INSERT INTO brand (name) VALUES ('volkswagen');
INSERT INTO brand (name) VALUES ('ford');
INSERT INTO brand (name) VALUES ('honda');
INSERT INTO brand (name) VALUES ('hyundai');
INSERT INTO brand (name) VALUES ('nissan');
INSERT INTO brand (name) VALUES ('chevrolet');
INSERT INTO brand (name) VALUES ('kia');
INSERT INTO brand (name) VALUES ('mercedes-benz');
INSERT INTO brand (name) VALUES ('bmw');