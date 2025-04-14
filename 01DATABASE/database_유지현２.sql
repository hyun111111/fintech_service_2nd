create database world;
use world;

CREATE TABLE country_table (
code VARCHAR(10) NOT NULL PRIMARY KEY UNIQUE,
code2 VARCHAR(10) NOT NULL,
Name VARCHAR(50) NOT NULL,
Continent VARCHAR(50) NOT NULL,
SurfaceArea INT,
Population INT,
LifeExpectancy FLOAT,
GNP INT
);

INSERT INTO country_table VALUES ('USA', 'USA', '미국', 'North_America', 9363520, 278357000, 77.1, 8510700);
INSERT INTO country_table VALUES ('JPN', 'JPN', '일본', 'Asia', 377829, 126714000, 80.7, 3787042);
INSERT INTO country_table VALUES ('GBR', 'GBR', '영국', 'Europe', 242900, 59623400, 77.7, 1378330);
INSERT INTO country_table VALUES ('DEU', 'DEU', '독일', 'Europe', 357022, 82164700, 77.4, 2133367);
INSERT INTO country_table VALUES ('CHN', 'CHN', '중국', 'Asia', 9572900, 1277558000, 71.4, 982268);


select * from country_table;