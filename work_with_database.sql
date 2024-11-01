Список логинов курьеров с количеством их заказов в статусе «В доставке»

SELECT c.login AS "Логин", COUNT(o.id) AS "Количество принятых заказов"
FROM "Couriers" AS c
JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;

SELECT o.track AS "Трек заказа",
CASE 
WHEN o.finished = true THEN 2
WHEN o.cancelled = true THEN -1
WHEN o."inDelivery" = true THEN 1
ELSE 0 END AS "Статус"
FROM "Orders" AS o;