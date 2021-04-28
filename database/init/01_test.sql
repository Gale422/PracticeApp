use practice_db;
create table todo_list(
  id INT NOT NULL AUTO_INCREMENT,
  title TEXT NOT NULL,
  start_time DATETIME DEFAULT NULL,
  end_time DATETIME DEFAULT NULL,
  location TEXT DEFAULT NULL,
  detail LONGTEXT DEFAULT NULL,
  inserted_at DATETIME DEFAULT NOW(),
  updated_at DATETIME DEFAULT NOW(),
  PRIMARY KEY (id)
);

create table tags(
  id INT NOT NULL AUTO_INCREMENT,
  todo_id INT NOT NULL,
  tag_id INT NOT NULL,
  order_index INT NOT NULL DEFAULT 0,
  PRIMARY KEY (id),
  UNIQUE tag_uni_index (todo_id, tag_id),
  UNIQUE order_uni_index (todo_id, order_index)
);

create table tag(
  id INT NOT NULL AUTO_INCREMENT,
  name TEXT NOT NULL,
  PRIMARY KEY (id)
);

insert into todo_list
  (title, start_time, end_time, location, detail)
values 
  ('TODO 1', DATE_FORMAT(DATE_ADD(NOW(), interval 1 day), '%Y-%m-%d 12:00:00'), DATE_FORMAT(DATE_ADD(NOW(), interval 1 day), '%Y-%m-%d 13:00:00'), null, 'TODO 1 の詳細データです。'),
  ('TODO 2', DATE_ADD(NOW(), interval 5 hour), DATE_ADD(NOW(), interval 8 hour), null, 'TODO 2 の詳細データです。'),
  ('TODO 3', null, DATE_FORMAT(LAST_DAY(NOW()), '%Y-%m-%d 23:59:59'), null, 'TODO 3 の詳細データです。'),
  ('TODO 4', NOW(), null, null, 'TODO 4 の詳細データです。'),
  ('TODO 5', null, null, null, 'TODO 5 の詳細データです。');

insert into tag
  (name)
values
  ('動作確認用'),
  ('練習用'),
  ('TODO');

insert into tags
  (todo_id, tag_id, order_index)
values
  (0, 1, 1),
  (1, 2, 1),
  (2, 3, 1),
  (3, 1, 2),
  (3, 2, 1);