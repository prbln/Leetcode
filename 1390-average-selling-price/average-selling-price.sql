# Write your MySQL query statement below
select p.product_id, COALESCE(ROUND(SUM(p.price*s.units)/SUM(s.units),2), 0 ) as "average_price"
from prices p LEFT join  unitssold s on p.product_id = s.product_id and s.purchase_date Between p.start_date and p.end_date 
group by p.product_id;