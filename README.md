# tournament
This is a small database application that tracks results from a Swiss-style tournament.

# prerequisites
<pre>
python 2.7
postgres 9.5.6
</pre>

# installation
```
vagrant@vagrant:/vagrant/tournament$ **psql**  
psql (9.5.6)  
Type "help" for help.  
vagrant=> **\i tournament.sql**  
```

# running unit tests
```
vagrant@vagrant:~$ cd /vagrant  
vagrant@vagrant:/vagrant$ cd tournament  
vagrant@vagrant:/vagrant/tournament$ python tournament_test.py  
```

# methods
**connect()** -- _connect to the tournament database_
**deleteMatches()** -- _delete all matches_
**deletePlayers()** -- _delete all players_
**countPlayers()** -- _count the players_
**registerPlayer(name)** -- _register a player_
**playerStandings()** -- _get a list of all players and their statistics sorted by who has won the most matches_
**reportMatch()** -- _record the results of a match_
**swissPairings** -- _get the pairings for the next round of the tournament_


# version
version 0.1

# authors
Kenneth Kehl

# acknowledgements
This project was a class project for the Udacity full stack nanodegree.

# license
This project is released under the <a href="https://opensource.org/licenses/MIT">MIT License</a>