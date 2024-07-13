# Write your MySQL query statement below
select r.contest_id, ROUND((count(r.user_id)/(select count(user_id) from Users))*100, 2) as percentage
from register r right join users u on r.user_id = u.user_id 
where r.user_id is not null 
group by r.contest_id
order by percentage desc, contest_id;