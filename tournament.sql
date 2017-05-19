-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE players;
DROP TABLE player_standings;
DROP TABLE matches;

CREATE TABLE matches (
    winner_id int,
	loser_id int,
	id serial,
	PRIMARY KEY(id)
);

CREATE TABLE players (
    name text,
	id serial,
	PRIMARY KEY(id)
);

CREATE TABLE player_standings (
    player_id int,
	wins int,
	matches int,
	id serial,
	PRIMARY KEY(id)
);
