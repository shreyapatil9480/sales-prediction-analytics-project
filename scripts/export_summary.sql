-- Stakeholder summary metrics for D07
SELECT
  COUNT(*) AS total_records,
  AVG(CAST(meets_sla AS FLOAT)) AS meets_sla_rate
FROM warehouse_throughput;

SELECT *
FROM warehouse_throughput
ORDER BY 1
LIMIT 10;
