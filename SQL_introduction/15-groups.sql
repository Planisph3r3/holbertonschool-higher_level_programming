-- Qualifing values based on the number of recounts.
SELECT DISTINCT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC, score;