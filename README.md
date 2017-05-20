# tournament
This is a small database application that tracks results from a Swiss-style tournament.

# prerequisites
python 2.7
<BR>
postgres 9.5.6

# installation
` 
vagrant@vagrant:/vagrant/tournament$ **psql**  
psql (9.5.6)  
Type "help" for help.  
vagrant=> **\i tournament.sql**  
`

# running unit tests
<pre>
` 
vagrant@vagrant:~$ cd /vagrant  
vagrant@vagrant:/vagrant$ cd tournament  
vagrant@vagrant:/vagrant/tournament$ python tournament_test.py  
`
</pre>

# methods
**connect()** -- __connect to the tournament database__
<BR>
**deleteMatches()** -- __delete all matches__
<BR>
**deletePlayers()** -- __delete all players__
<BR>
**countPlayers()** -- __count the players__
<BR>
**registerPlayer(name)** -- __register a player__
<BR>
**playerStandings()** -- __get a list of all players and their statistics sorted by who has won the most matches__
<BR>
**reportMatch()** -- __record the results of a match__
<BR>
**swissPairings** -- __get the pairings for the next round of the tournament__
<BR>

# version
version 0.1

# authors
Kenneth Kehl

# acknowledgements
This project was a class project for the Udacity full stack nanodegree.

# license
This project is released under the <a href="https://opensource.org/licenses/MIT">MIT License</a>