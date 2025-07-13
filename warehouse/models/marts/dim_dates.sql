WITH dates AS (
  SELECT
    generate_series('2023-01-01'::date, CURRENT_DATE, INTERVAL '1 day') AS date
)
SELECT
  date,
  EXTRACT(DAY FROM date) AS day,
  EXTRACT(MONTH FROM date) AS month,
  EXTRACT(YEAR FROM date) AS year,
  EXTRACT(DOW FROM date) AS weekday
FROM dates
