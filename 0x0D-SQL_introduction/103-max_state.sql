-- Displays the max temperature of each state (ordered by State name)
SELECT state, MAX(value) as max_temp
FROM temparatures
GROUP BY state
ORDER BY state;
