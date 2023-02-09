# mancala-py
A mancala game that you can play in your command line

mancala-py allows two people to play a text-based version of the game Mancala (check the attached PDF file for the detailed rules).

For this board game, two players can play. As the figure shows, the player who choose the bottom red position will be player 1 and the player choose the top blue position will be player 2.  Each player could only choose the pit on his side in each round: player 1 can only choose pits in red and player 2 can only choose pits in blue. The index for each pit is marked in the figure as well.

mancala-py does not have a GUI -- it was made simply as an exercise in object oriented programming (classes, composition), control flow, and data structures. 

* As a simple example, here is how the game can be played:

      game = Mancala()
      player1 = game.create_player("Lily")
      player2 = game.create_player("Lucy")
      print(game.play_game(1, 3))
      game.play_game(1, 1)
      game.play_game(2, 3)
      game.play_game(2, 4)
      game.play_game(1, 2)
      game.play_game(2, 2)
      game.play_game(1, 1)
      game.print_board()
      print(game.return_winner())

* And the output will be:

      player 1 take another turn
      [4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0]
      player 2 take another turn
      player1:
      store: 10
      [0, 0, 2, 7, 7, 6]
      player2:
      store: 2
      [5, 0, 1, 1, 0, 7]
      Game has not ended


* Another test example could be:

      game = Mancala()
      player1 = game.create_player("Lily")
      player2 = game.create_player("Lucy")
      game.play_game(1, 1)
      game.play_game(1, 2)
      game.play_game(1, 3)
      game.play_game(1, 4)
      game.play_game(1, 5)
      game.play_game(1, 6)
      game.print_board()
      print(game.return_winner())

* And the output will be:

      player 1 take another turn
      player1:
      store: 12
      [0, 0, 0, 0, 0, 0]
      player2:
      store: 36
      [0, 0, 0, 0, 0, 0]
      Winner is player 2: Lucy
