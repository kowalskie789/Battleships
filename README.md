 

<h1>Battleship</h1>
One of the first projects for Codecool: a classic Battleship game created in Python as a console app.

<h2>About</h2>
This project does not vary from classic rules of Battleship game. Players in their turns try to guess fields filled by ships and sink them. The game of course consists of two phases: a placement phase and a shooting phase
<h2>Phase one: placement</h2>
Each player has to place 6 ships of three kinds: big (3 fields), medium (2 fields) and small (1 field). 3 of them are small, 2 medium and 1 is big on a board with size 5x5. Player can't place a ship on the place where there are ships already, at the area surrounding tham, or outside the board. He has to enter coordinates (letter for row and number for column, like for example A1, wich means the upper row and the left column) of the upper-left end of the ship, then program checks whether this input is valid and meets all described citeria. If yes, ship is succesfully placed, otherwise player is asked to place a ship again. When one player places all the ships, the second player does the same thing.
<h2>Phase two: shooting</h2>
This phase consists of guessing the positions and shooting. After one shot, second player gets his. All fields of oponent's board are covered with "X". When you shoot, it changes:
<ul>
  <li>When you miss, it changes to "M"</li>
  <li>When you hit, changes to "H"</li>
  <li>When you sink a ship, all fields covered by it change to "S"</li>
</ul>
Game ends, when one player sinks all the oponent's ships.
