DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS `addNums`(
	IN `num1` INT,
	IN `num2` INT,
	OUT `total` INT
)
BEGIN
	Set total = num1 + num2;
END$$
DELIMITER ;

/*
Call addNums(5,10,@sum);
SELECT @sum;
*/
