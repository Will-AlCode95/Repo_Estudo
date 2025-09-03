
--SELECT * 
--FROM employees 
--WHERE Title LIKE '%Sales%';

--SELECT DISTINCT CustomerId 
--FROM invoices 
--WHERE BillingCity = 'Brasília';

SELECT t.Name 
FROM tracks t
INNER JOIN genres g ON t.GenreId = g.GenreId
WHERE g.Name = 'Rock And Roll';
