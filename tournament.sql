-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS player_standings;
DROP TABLE IF EXISTS matches;


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
