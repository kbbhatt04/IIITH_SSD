DELIMITER //
DROP PROCEDURE IF EXISTS Ques3;
CREATE PROCEDURE Ques3()
BEGIN
	SELECT CUST_NAME, GRADE 
 	FROM customer
	WHERE OPENING_AMT + RECEIVE_AMT > 10000;
END //

DELIMITER ;

/*
CALL Ques3();
*/
