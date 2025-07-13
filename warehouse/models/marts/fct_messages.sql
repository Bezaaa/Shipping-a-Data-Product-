SELECT
  message_id,
  channel_username,
  posted_at,
  has_media,
  media_type,
  LENGTH(text) AS message_length
FROM staging.stg_telegram_messages
