# tournament
This is a small database application that tracks results from a Swiss-style tournament.

# prerequisites
python 2.7
postgres 9.5.6

# installation
` 
vagrant@vagrant:/vagrant/tournament$ **psql**
psql (9.5.6)
Type "help" for help.
vagrant=> **\i tournament.sql**
`

# running unit tests
` 
vagrant@vagrant:~$ cd /vagrant
vagrant@vagrant:/vagrant$ cd tournament
vagrant@vagrant:/vagrant/tournament$ python tournament_test.py
`

# methods
**connect()** -- __connect to the tournament database__
**deleteMatches()** -- __delete all matches__
**deletePlayers()** -- __delete all players__
**countPlayers()** -- __count the players__
**registerPlayer(name)** -- __register a player__
**playerStandings()** -- __get a list of all players and their statistics sorted by who has won the most matches__
**reportMatch()** -- __record the results of a match__
**swissPairings** -- __get the pairings for the next round of the tournament__

# version
version 0.1

# authors
Kenneth Kehl

# acknowledgements
This project was a class project for the Udacity full stack nanodegree.

# license
This project is released under the <a href="https://opensource.org/licenses/MIT">MIT License</a>