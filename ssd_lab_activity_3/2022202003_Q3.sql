SELECT Essn, COUNT(Pno) FROM WORKS_ON GROUP BY Essn HAVING Essn IN (SELECT Mgr_ssn FROM DEPARTMENT WHERE Dnumber = (SELECT Dnum FROM PROJECT WHERE Pname='ProductY'));
