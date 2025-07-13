WITH raw AS (
  SELECT * FROM raw.telegram_messages
)

SELECT
  id::bigint AS message_id,
  channel_username,
  text,
  date::timestamp AS posted_at,
  has_media,
  media_type
FROM raw
