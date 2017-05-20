#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database """
    db = connect()
    c = db.cursor()
    c.execute("delete from matches")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("delete from players")
    db.commit()
    db.close()
    


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("select count(*) from players as player_count")
    player_count = c.fetchone()
    db.close()
    return player_count[0];

def registerPlayer(name):
    """Adds a player to the tournament database.
	
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
	
    """ create player """
    c.execute("insert into players (name) values (%s)", [name])  
    db.commit()
    db.close()



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
	
    c.execute("select * from v_rankings")
    standings = c.fetchall()
    db.close()
    return standings;


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
    db = connect()
    c = db.cursor()
	
    """ update matches table with the new match """
    c.execute("insert into matches (winner_id, loser_id) values (%s, %s)", (winner, loser))  
		
    db.commit()
    db.close()

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the sepsqlcond player's name
    """
	
    players = playerStandings();
	
	
    names_and_ids = []
    is_second_pair = False
    p1_id = ""
    p1_name= ""
    p2_id = ""
    p2_name = ""
	
    if len(players) % 2 != 0:
        raise ValueError("swissPairings() requires an even number of players")
   
    """ results should be order from worst players to best and we are guaranteed an even number
        so take the first two, make a tuple, grab the next two, etc. """
    for p in players:
        if (is_second_pair):
            p2_id = p[0]
            p2_name = p[1]
            tup = (p1_id, p1_name, p2_id, p2_name)
            names_and_ids.append(tup)
            is_second_pair = False
        else:
            p1_id = p[0]
            p1_name = p[1]
            is_second_pair = True
    return names_and_ids