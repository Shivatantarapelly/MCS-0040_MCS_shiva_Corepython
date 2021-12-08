CREATE TABLE emp_details(
name varchar(25),
eid integer,
designation varchar(25),
salary integer);
select * from emp_details;

INSERT INTO emp_details values('surya', 11250, 'manager',15000);

INSERT INTO emp_details VALUES('varma',11251, 'manager',15500);
INSERT INTO emp_details VALUES('kalyan',11252,'manager',15500);
INSERT INTO emp_details VALUES('sharma',11253,'manager',15560);
INSERT INTO emp_details VALUES('vihan',10256,'engineer',12000);
INSERT INTO emp_details VALUES('vikram',10258,'engineer',12500);
INSERT INTO emp_details VALUES('vishali',10259,'hr',10000);

SELECT*FROM emp_details;


INSERT INTO emp_details VALUES('sreekanth',10267,'hr',10200);

INSERT INTO emp_details VALUES('ishaan',10268,'supervisor',8500);
INSERT INTO emp_details VALUES('kiran',10269,'supervisor',8000);

SELECT * FROM emp_details;

DELETE FROM emp_details WHERE eid = 10268;
DELETE FROM emp_details WHERE name = 'kiran';

SELECT*FROM emp_details;

ALTER TABLE emp_details ADD COLUMN place varchar(15);
ALTER TABLE emp_details ADD COLUMN email varchar(25);
ALTER TABLE emp_details ADD COLUMN benefits integer;
ALTER TABLE emp_details ADD COLUMN bonus integer;

SELECT * FROM emp_details;

ALTER TABLE emp_details DROP COLUMN bonus;
ALTER TABLE emp_details DROP COLUMN benefits;

SELECT name,eid,designation,salary from emp_details WHERE designation = 'hr';
SELECT name,eid,designation from emp_details where salary < 12000;

SELECT sum(salary) total_sal from emp_details;

SELECT sum(salary) hr_sal from emp_details where designation = 'hr';
SELECT sum(salary) manager_sal from emp_details where designation = 'manager';
SELECT SUM(salary) supervisor_sal from emp_details where designation = 'supervisor';

SELECT name,eid,salary from emp_details where name LIKE '__l%';

SELECT name,eid,salary from emp_details where name LIKE '%a%';


SELECT
CASE
WHEN salary = 15000 THEN
salary + 5000
WHEN salary <15000 THEN
salary +10000
WHEN salary = 12000 THEN
salary - 5000
WHEN salary < 10000 THEN
salary - 8000
ELSE
salary + 30000
END salaryinc,name,designation
FROM
emp_details;

