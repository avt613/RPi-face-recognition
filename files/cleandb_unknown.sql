delete from faces where person_id in (SELECT people.id FROM people WHERE name LIKE 'unknown%');
delete from log where person_id in (SELECT people.id FROM people WHERE name LIKE 'unknown%');
delete from people where id in (SELECT people.id FROM people WHERE name LIKE 'unknown%');