-- Task 3: List all Glam rock bands ranked by their longevity
-- This script selects all bands with "Glam rock" as their main style
-- and ranks them by their longevity (calculated using the "formed" and "split" attributes)

SELECT band_name, TIMESTAMPDIFF(YEAR, formed, IFNULL(split, CURDATE())) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
