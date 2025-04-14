create database world;
use world;

CREATE TABLE exchange_rate (
code2 VARCHAR(10) NOT NULL PRIMARY KEY UNIQUE,
country_name VARCHAR(50),
Currency_name VARCHAR(20),
Exchange_rate VARCHAR(20),
Cash_Buying VARCHAR(20),
Cash_Selling VARCHAR(20),
Remit_Sending VARCHAR(20),
Remit_Receiving VARCHAR(20),
USD_Conv_Rate FLOAT,
dat DATETIME NOT NULL
);

  INSERT INTO exchange_rate VALUES (
  'USA', '미국', 'USD', '1,377.00', '1,401.09', '1,352.91', '1,390.40', '1,363.60', 1, '2024-07-13');
  
  INSERT INTO exchange_rate VALUES (
  'EU', '유럽연합', 'EUR', '1,501.55', '1,531.43', '1,471.67', '1,516.56', '1,486.54', 1.091, '2024-07-13');
  INSERT INTO exchange_rate VALUES (
  'JPN', '일본', 'JPY(100엔)', '872.07', '887.33', '856.81', '880.61', '863.53', 0.633, '2024-07-13');
  
  INSERT INTO exchange_rate VALUES (
  'CHN', '중국', 'CNY', '189.37', '198.83', '179.91', '191.26', '187.48', 0.138, '2024-07-13') ;

INSERT INTO exchange_rate VALUES (
  'GBR', '영국', 'GBP', '1,788.10', '1,823.32', '1,752.88', '1,770.22', '1,740.00', 1.299, '2024-07-13'
);

select * from exchange_rate ORDER BY cocuntry_name;