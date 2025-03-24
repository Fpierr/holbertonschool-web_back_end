-- Task 3
-- Glam rock
SELECT band_name, COALESCE(split, 2024) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
