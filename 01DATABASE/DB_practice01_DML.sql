USE titanic;
show tables;
SELECT * FROM p_info;
DESC p_info;
SELECT * FROM p_info WHERE Sibsp=1 or Sibsp=2 or Sibsp=3;
SELECT * FROM p_info WHERE Age>20 and Age<50;
SElECT * FROM p_info WHERE SibSp>1 and Parch>1;
SELECT * FROM t_info WHERE Pclass=1;

