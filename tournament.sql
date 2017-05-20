-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players (
    name text,
	id serial,
	PRIMARY KEY(id)
);

CREATE TABLE matches (
    winner_id int references players(id),
	loser_id int references players(id),
	id serial,
	PRIMARY KEY(id)
);




CREATE VIEW v_wins as
select players.id, count(matches.id) as wins
from players left outer join matches
    on players.id = matches.winner_id
group by players.id;

CREATE VIEW v_matches as
select players.id, players.name, count(matches.id) as played
from players left outer join matches
    on players.id = matches.winner_id or players.id = matches.loser_id
group by players.id;



CREATE VIEW v_rankings as
    select v_wins.id, v_matches.name, wins, played
    from v_wins join v_matches
        on v_wins.id = v_matches.id
    group by v_wins.id, v_matches.name, v_wins.wins, played
	order by wins desc;


