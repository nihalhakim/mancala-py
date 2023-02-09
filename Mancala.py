# Author: Nihal Hakim
# GitHub username: nihalhakim
# A Mancala game simulator for two players


class Mancala:
    """
    This is the Mancala class, it contains information and logic to represent a Mancala game
    """

    def __init__(self):
        """
        The init method will create some other private data members to keep track of during the game
        _player1, _player2 will be assigned by the create_player method, _winner will be assigned by the check_winner method
        The _pits_and_stores variable is a dict representing key-values of the pits and stores in the order of the game direction.
        """
        self._player1 = None
        self._player2 = None
        self._winner = None
        self._pits_and_stores = {
            0: 4,
            1: 4,
            2: 4,
            3: 4,
            4: 4,
            5: 4,

            6: 0,

            7: 4,
            8: 4,
            9: 4,
            10: 4,
            11: 4,
            12: 4,

            13: 0
        }  # key 6 is player 1's store, and key 13 is player 2's store

    def create_player(self, name):
        """
        A method to be called when creating a player for a mancala game
        Checks if player 1 and/or player 2 is assigned and assigns a Player object to the first available
        If player 1 is None then create a new Player with the given name and assign it to self._player1
        Else if player 2 is None then create a new Player with the given name and assign it to self._player2
        Else print a message to user if player 1 and player 2 are assigned
        """
        if self._player1 is None:
            self._player1 = Player(name)
            return self._player1
        elif self._player2 is None:
            self._player2 = Player(name)
            return self._player2
        else:
            print("player 1 and player 2 are already assigned")

    def get_player(self, x):
        """
        getter method to return a player object by its number
        """
        if x == 1:
            return self._player1
        if x == 2:
            return self._player2

    def print_board(self):
        """
        print player1's store by accessing self._pits_and_stores[6] and printing value
        print player1's seed numbers by accessing self._pits_and_stores and iterating over keys 0-5 and printing values in a list (using list comprehension)
        print player2's store by accessing self._pits_and_stores[13] and printing value
        print player2's seed numbers by accessing self._pits_and_stores and iterating over keys 7-12 and printing values in a list (using list comprehension)
        """
        print("player1:")
        print("store: " + str(self._pits_and_stores[6]))
        print(str([self._pits_and_stores[x] for x in self._pits_and_stores if 0 <= x <= 5]))
        print("player2:")
        print("store: " + str(self._pits_and_stores[13]))
        print(str([self._pits_and_stores[x] for x in self._pits_and_stores if 7 <= x <= 12]))

    def return_winner(self):
        """
        this method will use a private data member of Mancala, _winner, to print the appropriate value
        the _winner  variable will be updated and/or assigned by the check_winner method, which will be called in the play_game method
        If self._winner is None then the game has not ended so print a message saying so
        Else if self._winner has the value of "tie" then print that it is a tie
        If none of the above, then check if self._winner is player 1 then print the winner message, or if self._winner is player 2 then print the winner message
        We are returning the values instead of printing them in this function because the examples in the README print this function
        """
        if self._winner is None:
            return "Game has not ended"
        elif self._winner == "tie":
            return "It's a tie"
        else:
            if self._winner == self._player1:
                return "Winner is player 1: " + str(self._player1.get_name())
            if self._winner == self._player2:
                return "Winner is player 2: " + str(self._player2.get_name())

    def check_winner(self, player_index):
        """
        This method is called  in the play_game method after a turn is "played"
        Checks if there is a winner and updates self._winner if so
        takes as a parameter the player_index of the play_game method so it only checks the rules for the player that last played
        If the player index passed is 1:
        Iterate over keys 0-5 of self._pits_and_stores and if all values are empty then take the seeds from player 2's pits and put it into player 2's store. That is take the sum of the values of self._pits_and_stores from keys 7 to 12 and add it to self._pits_and_stores[13]
        Then if self._pits_and_stores[6] is greater than self._pits_and_stores[13] then player 1 to self._winner, if self._pits_and_stores[6] is less than self._pits_and_stores[13] then player 2 to self._winner, if equal its a tie
        If the player index passed is 2:
        Iterate over keys 7-12 of self._pits_and_stores and if all values are empty then take the seeds from player 1's pits and put it into player 1's store. That is take the sum of the values of self._pits_and_stores from keys 0 to 5 and add it to self._pits_and_stores[6]
        Then if self._pits_and_stores[6] is greater than self._pits_and_stores[13] then player 1 to self._winner, if self._pits_and_stores[6] is less than self._pits_and_stores[13] then player 2 to self._winner, if equal its a tie
        returns True if a winner was assigned at all (including a tie), return False otherwise
        """
        row_sum = 0  # we will check if the sum of the player's row is equal to 0
        if player_index == 1:
            for i in range(0, 5 + 1):
                row_sum += self._pits_and_stores[i]
            if row_sum == 0:
                for j in range(7, 12 + 1):
                    self._pits_and_stores[13] += self._pits_and_stores[j]
                    self._pits_and_stores[j] = 0
        if player_index == 2:
            for k in range(7, 12 + 1):
                row_sum += self._pits_and_stores[k] != 0
            if row_sum == 0:
                for l in range(0, 5 + 1):
                    self._pits_and_stores[6] += self._pits_and_stores[l]
                    self._pits_and_stores[l] = 0

        if row_sum == 0:  # this is the win condition
            if self._pits_and_stores[6] > self._pits_and_stores[13]:
                self._winner = self._player1
                return True
            elif self._pits_and_stores[13] > self._pits_and_stores[6]:
                self._winner = self._player2
                return True
            elif self._pits_and_stores[6] == self._pits_and_stores[13]:
                self._winner = "tie"
                return True
        else:
            return False

    def play_game(self, player_index, pit_index):
        """
        If the player_index is 2 then take the pit_index and add 7 so we start from the correct pit
        execute moves by setting a temp var X to the pit value, setting pit value to 0, then iterating over the next X keys and adding 1 to their value. Go to the beginning of the keys if the end of the dict is reached.
        On the last iteration if the key is the player's store (either 6 or 13) then print a message that they should play another turn.
        If the new value at the key on the last iteration becomes 1, then set that value back to 0, get the opposite pit (opp_key = -curr_key + 12) and take the pits from the opponents side and set it to 0, and add the sum to the players store
        pass player_index to the check_winner method to see if the last move resulted in a winner, if check_winner returns True then return nothing to stop the game play
        returns a list of the current seed number in the specified format by iterating over the values of self._pits_and_stores and printing them in a list
        """
        if not (1 <= pit_index <= 6 or not isinstance(pit_index, int)):
            return "Invalid number for pit index"

        if self._winner:  # if there is a winner don't play
            return "Game is ended"

        pit_index -= 1  # the user passes a pit number, as in "1" for the first pit, but we subtract 1 from that because the first is "0" in our dict
        if player_index == 2:  # if we're playing for player 2 then offset the given pit index by 7
            pit_index += 7

        X = self._pits_and_stores[pit_index]  # grab the value at the given key i.e. assign the number of variables to a temp variable

        self._pits_and_stores[pit_index] = 0  # the number of seeds in the pit is now 0

        i = 0  # we use "i" to keep track of how many pits forward we are dropping, we use "_" as the iterating variable below to keep track of how many drops we make
        last_played_pit_index = None  # we initialize a variable for the last_played_pit_index here because later on we need to catch a special case (mentioned below)
        for _ in range(1, X + 1):  # start dropping the seeds into pits
            i += 1
            if pit_index + i > 13:  # if the targeted pit is past the range of the dict start over from the beginning
                pit_index = 0
                i = 0

            if player_index == 1:
                if pit_index + i != 13:  # player 1 should not drop seeds into player 2's pit
                    self._pits_and_stores[pit_index + i] += 1
                elif pit_index + i == 13:  # if player 1 is about to drop a seed into player 2's pit then...
                    if _ == X:  # if we are at the last seed just drop the seed player 1's first pit. The loop will end after this
                        self._pits_and_stores[0] += 1
                        last_played_pit_index = 0  # this is the special case where we needed to define last_played_pit_index ahead of when it is calculated below. the special case is the player has to skip the opposite player's store in their last move
                    else:  # if we are not at the last seed then increment i by 1 to skip forward a pit, but decrement _ by 1 to account for the extra seed
                        i += 1
                        _ -= 1
                        continue
            elif player_index == 2:
                if pit_index + i != 6:  # player 2 should not drop seeds into player 1's pit
                    self._pits_and_stores[pit_index + i] += 1
                elif pit_index + i == 6:  # if player 2 is about to drop a seed into player 1's pit then...
                    if _ == X:  # if we are at the last seed just drop the seed player 2's first pit. The loop will end after this
                        self._pits_and_stores[7] += 1
                        last_played_pit_index = 7  # this is the special case where we needed to define last_played_pit_index ahead of when it is calculated below. the special case is the player has to skip the opposite player's store in their last move
                    else:  # if we are not at the last seed then increment i by 1 to skip forward a pit, but decrement _ by 1 to account for the extra seed
                        i += 1
                        _ -= 1
                        continue

            if _ == X:  # checking for special rules here. This line catches the last iteration of the loop by checking if the iterator is equal to the number of seeds that were to be dropped
                if last_played_pit_index is None:  # last_played_pit_index is calculated in the next line, but it may have been assigned before in the special case above where the player has to skip the opposite player's store in their last move
                    last_played_pit_index = pit_index + i
                if player_index == 1 and last_played_pit_index == 6:  # checks if player 1 just landed their last seed into their store
                    print("player 1 take another turn")
                elif player_index == 2 and last_played_pit_index == 13:  # checks if player 2 just landed their last seed into their store
                    print("player 2 take another turn")
                elif self._pits_and_stores[last_played_pit_index] == 1 and ((player_index == 1 and 0 <= last_played_pit_index <= 5) or (player_index == 2 and 7 <= last_played_pit_index <= 12)):  # checks if the last played seed went into a pit that was previously empty and on players side
                    self._pits_and_stores[last_played_pit_index] = 0
                    opp_key = -last_played_pit_index + 12
                    stolen_seeds = self._pits_and_stores[opp_key] + 1
                    self._pits_and_stores[opp_key] = 0
                    if player_index == 1:
                        self._pits_and_stores[6] += stolen_seeds
                    if player_index == 2:
                        self._pits_and_stores[13] += stolen_seeds

        self.check_winner(player_index)
        return [self._pits_and_stores[x] for x in self._pits_and_stores if 0 <= x <= 13]  # this function will always return the pits and stores as a list


class Player:
    """
    This class represents a game player. It stores the name as a private data variable and has a get_name() function to get the name
    """

    def __init__(self, name):
        self._name = name

    def get_name(self):
        """
        getter method for the name of a player
        """
        return self._name


def test_1():
    """
    a function wrapping the first test example provided in the README
    """
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


def test_2():
    """
    a function wrapping the second test example provided in the README
    """
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


def main():
    """
    This main function calls both test examples
    """
    print("------TEST EXAMPLE 1------")
    test_1()

    print()

    print("------TEST EXAMPLE 2------")
    test_2()

# if __name__ == "__main__":
#     main()
