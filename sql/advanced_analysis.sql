-- Total Revenue
SELECT SUM(fare_amount) AS total_revenue
FROM ola_rides
WHERE ride_status = 'Completed';

-- Cancellation Rate
SELECT COUNT(CASE WHEN ride_status='Cancelled' THEN 1 END)*100.0 / COUNT(*) 
AS cancellation_rate
FROM ola_rides;

-- Driver Ranking
WITH driver_revenue AS (
  SELECT driver_id,
         SUM(fare_amount) AS total_revenue
  FROM ola_rides
  WHERE ride_status='Completed'
  GROUP BY driver_id
)
SELECT *,
       RANK() OVER (ORDER BY total_revenue DESC) AS driver_rank
FROM driver_revenue;