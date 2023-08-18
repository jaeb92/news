create table news (
    news_id varchar primary key,
    title varchar not null,
    content text not null,
    author varchar,
    date timestamp,
    source varchar
)