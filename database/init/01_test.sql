use practice_db;
create table todoList(
  id INT NOT NULL AUTO_INCREMENT,
  name TEXT NOT NULL,
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

insert into todoList
  (name)
values 
  ('TODO 1'),
  ('TODO 2'),
  ('TODO 3'),
  ('TODO 4'),
  ('TODO 5');

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