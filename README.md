# tournament
This is a small database application that tracks results from a Swiss-style tournament.

# prerequisites
python 2.7
<BR>
postgres 9.5.6

# installation
```
<pre> 
vagrant@vagrant:/vagrant/tournament$ **psql**  
psql (9.5.6)  
Type "help" for help.  
vagrant=> **\i tournament.sql**  
</pre>
```

# running unit tests
```
<pre>
vagrant@vagrant:~$ cd /vagrant  
vagrant@vagrant:/vagrant$ cd tournament  
vagrant@vagrant:/vagrant/tournament$ python tournament_test.py  
</pre>
```

# methods
<pre>
**connect()** -- _connect to the tournament database_
**deleteMatches()** -- _delete all matches_
**deletePlayers()** -- _delete all players_
**countPlayers()** -- _count the players_
**registerPlayer(name)** -- _register a player_
**playerStandings()** -- _get a list of all players and their statistics sorted by who has won the most matches_
**reportMatch()** -- _record the results of a match_
**swissPairings** -- _get the pairings for the next round of the tournament_
</pre>

# version
version 0.1

# authors
Kenneth Kehl

# acknowledgements
This project was a class project for the Udacity full stack nanodegree.

# license
This project is released under the <a href="https://opensource.org/licenses/MIT">MIT License</a>