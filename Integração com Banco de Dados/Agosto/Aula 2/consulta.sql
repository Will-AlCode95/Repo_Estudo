.mode table

SELECT FirstName || ' ' || LastName AS Nome, address as Endereço, Country as País
FROM customers
WHERE Endereço LIKE 'B%'
ORDER BY Nome, País;
