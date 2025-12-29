SELECT
    o.track,
    CASE
        WHEN o.finished = true THEN 2
        WHEN o.cancelled = true THEN -1
        WHEN o."inDelivery" = true THEN 1
        ELSE 0
    END AS status
FROM "Orders" o
ORDER BY o.track;
