DELIMITER //
DROP PROCEDURE IF EXISTS Ques4;
CREATE PROCEDURE Ques4()
BEGIN
	declare name VARCHAR(255);
	declare city VARCHAR(255);
	declare country VARCHAR(255);
	declare grade INT;
	declare fin INT default 0;
	declare cursooor cursor for SELECT CUST_NAME, CUST_CITY, CUST_COUNTRY, GRADE FROM customer WHERE AGENT_CODE LIKE 'A00%';
	declare continue handler for not found set fin=1;
	open cursooor;
	karan:loop
	fetch cursooor into name, city, country, grade;
	select name, city, country, grade;
	if fin=1 then
	leave karan;
	end if;
	end loop karan;
END //

DELIMITER ;

/*
CALL Ques4();
*/
