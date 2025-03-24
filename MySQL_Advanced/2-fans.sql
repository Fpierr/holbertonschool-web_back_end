-- Task 2
-- cat 2-fans.sql | mysql -uroot -p holberton > tmp_res ; head tmp
SELECT DISTINCT `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
