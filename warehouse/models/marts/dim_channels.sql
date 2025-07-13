SELECT DISTINCT
  channel_username,
  MIN(posted_at) AS first_seen,
  COUNT(*) AS total_messages
FROM staging.stg_telegram_messages
GROUP BY 1
