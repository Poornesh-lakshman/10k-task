
CREATE TABLE employee (
    emp_name CHAR(20),
    location VARCHAR(30)
);

ALTER TABLE employee
ADD address VARCHAR(50);

ALTER TABLE employee
ADD emp_id INT FIRST;

ALTER TABLE employee
ADD email VARCHAR(25) AFTER emp_name;

ALTER TABLE employee
MODIFY emp_name VARCHAR(20);

ALTER TABLE employee
ADD sid INT,
ADD department VARCHAR(30);

ALTER TABLE employee
RENAME COLUMN emp_name TO employeeName;

ALTER TABLE employee
CHANGE emp_name employeeName VARCHAR(20);

ALTER TABLE employee
DROP COLUMN sid;