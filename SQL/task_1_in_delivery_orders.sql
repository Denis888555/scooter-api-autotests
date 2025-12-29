SELECT
    c.login AS courier_login,
    COUNT(o.id) AS number_of_orders
FROM "Orders" o
JOIN "Couriers" c ON o."courierId" = c.id
WHERE o."inDelivery" = true
GROUP BY c.login;
