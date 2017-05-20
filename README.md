# tournament
This is a small database application that tracks results from a Swiss-style tournament.

# getting started

1. Install Python and Postgres
2. run the command "psql" to start Postgres
3. run the command "\i tournament.sql" to run the sql script to create your tournament database
4. exit from Postgres by running "\q"
5. run unit tests by running the commmand "python tournament_test.py"
6. If everything is good, the unit test should finish by printing out "Success! All tests pass!"

# methods
connect -- connect to the tournament database
deleteMatches -- delete all matches
deletePlayers -- delete all players
countPlayers -- count the players
registerPlayer -- register a player
playerStandings -- get a list of all players and their statistics sorted by who has won the most matches
reportMatch -- record the results of a match
swissPairings -- get the pairings for the next round of the tournament

# prerequisites

python 2.7
postgres 9.5

# version

version 0.1

# authors

Kenneth Kehl

# acknowledgements

This project was a class project for the Udacity full stack nanodegree.
