-- Table: books

-- DROP TABLE bookclub.books;

CREATE TABLE bookclub.books
(
  book_id integer NOT NULL,
  book_title varchar(500),
  book_desc varchar(5000) ,
  num_pages integer,
  CONSTRAINT book_id PRIMARY KEY (book_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE bookclub.books
  OWNER TO chadleonard;

-- drop table bookclub.review

  
CREATE TABLE bookclub.reviews
(
  review_id integer NOT NULL,
  book_id integer NOT NULL,
  rating decimal(5,2),
  votes integer,
  started_at varchar(35),
  read_at varchar(35),
  CONSTRAINT review_id PRIMARY KEY (review_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE bookclub.reviews
  OWNER TO chadleonard;



CREATE TABLE bookclub.authors
(
  author_id integer NOT NULL,
  author_name varchar(100),
  image_url varchar(200),
  small_image_url varchar(200),
  link varchar(100),
  average_rating decimal(5,2),
  ratings_count integer,
  text_reviews_count integer,
  CONSTRAINT author_id PRIMARY KEY (author_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE bookclub.authors
  OWNER TO chadleonard;


CREATE TABLE bookclub.books_authors_rltn
(
  book_id integer NOT NULL,
  author_id integer NOT NULL,
  published  integer,
  CONSTRAINT books_authors_id PRIMARY KEY (book_id, author_id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE bookclub.books_authors_rltn
  OWNER TO chadleonard;


















  