
--SELECT * 
--FROM employees 
--WHERE Title LIKE '%Sales%';

--SELECT DISTINCT CustomerId 
--FROM invoices 
--WHERE BillingCity = 'Brasília';

--SELECT t.Name 
--FROM tracks t
--INNER JOIN genres g ON t.GenreId = g.GenreId
--WHERE g.Name = 'Rock And Roll';

.mode column

.once saida.txt
--SELECT artists.Name AS Artista
--FROM albums 
--INNER JOIN artists ON albums.ArtistId = artists.ArtistId
--WHERE albums.Title = 'Dark Side Of The Moon';

SELECT albums.Title AS Album, artists.Name AS Artista
FROM albums 
INNER JOIN artists ON albums.ArtistId = artists.ArtistId
WHERE albums.Title LIKE '%black%' OR artists.Name LIKE '%black%';

