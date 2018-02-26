# Tournament

Receives a JSON with what type of tournament (seeded or blind draw), a list of categories and a list of players. 
It then sorts the players in different poules and gives back a file with the brackets.
Sorting can happen in two ways:
  - Blind draw: this is a random shuffle
  - Seeded: the best player goes against the worst, the second best against the second worst etc until no players are left. If there's an uneven number, the best player receives a bye.
  
  Bracket information: https://www.printyourbrackets.com/seededbrackets.html
