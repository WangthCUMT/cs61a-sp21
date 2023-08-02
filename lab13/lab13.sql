.read data.sql


CREATE TABLE bluedog AS
  SELECT color ,pet FROM students WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color ,pet, song FROM students WHERE color = 'blue' AND pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b WHERE a.time < b.time AND a.pet = b.pet AND a.song = b.song;


CREATE TABLE sevens AS
  SELECT s.seven FROM students as s, number AS c WHERE s.number = 7 AND c.'7' = 'True' AND s.time = c.time;


CREATE TABLE average_prices AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE lowest_prices AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE shopping_list AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE total_bandwidth AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

