DELIMITER //
DROP PROCEDURE CustomerName;
CREATE PROCEDURE CustomerName(
	IN city VARCHAR(255)
)
BEGIN
	SELECT CUST_NAME 
 	FROM customer
	WHERE WORKING_AREA = city;
END //

DELIMITER ;

/*
CALL CustomerName('Bangalore');
*/
