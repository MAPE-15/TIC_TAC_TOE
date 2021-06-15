# TIC-TAC-TOE
# FINISHED !!!

('''
ADD SOMETHING TO A MULTIPLE LIST

a = [[], [], []]
a[0].append(1)
print(a)

''')

('''
HOW IT IS SUPPOSED TO WORK !!!

tic_tac_toe_list = [
                    ['1'], ['2'], ['3'],
                    ['4', 'X'], ['5'], ['6'],
                    ['7'], ['8'], ['9', 'O']
                    ]

print(len(tic_tac_toe_list[0]))
print(tic_tac_toe_list[3][1])


PRINT THE TIC TAC TOE BOARD !!!
print('     |     |')
print('  ' + tic_tac_toe_list[0][len(tic_tac_toe_list[0]) - 1] + '  |  ' + tic_tac_toe_list[1][len(tic_tac_toe_list[1]) - 1] + '  |  '
      + tic_tac_toe_list[2][len(tic_tac_toe_list[2]) - 1])
print('_____|_____|_____')
print('     |     |   ')
print('  ' + tic_tac_toe_list[3][len(tic_tac_toe_list[3]) - 1] + '  |  ' + tic_tac_toe_list[4][len(tic_tac_toe_list[4]) - 1] + '  |  ' +
        tic_tac_toe_list[5][len(tic_tac_toe_list[5]) - 1])
print('_____|_____|_____')
print('     |     |')
print('  ' + tic_tac_toe_list[6][len(tic_tac_toe_list[6]) - 1] + '  |  ' + tic_tac_toe_list[7][len(tic_tac_toe_list[7]) - 1] + '  |  ' +
      tic_tac_toe_list[8][len(tic_tac_toe_list[8]) - 1])
print('     |     |')

''')

# ---------------------------------------------------------------------------------------------


print('''
HOW TIC TAC TOE LOOKS LIKE:
    
     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     
    
positions = 1, 2, 3, 4, 5, 6, 7, 8, 9
    
    ''')



def tic_tac_toe_game():

    # kolkaty hrac je na tahu z player_name listu (69)
    kolkaty_hrac = 0

    # kolkaty tah je zatial, zatial je 0
    kolkaty_turn = 0

    print('')
    # type 2 players who are gonna play this game, not less or more than 2 players
    player_names = input('Type 2 player names, who are going to play this game: ').split(', ')

    # a dictionary where player names are gonna be added and their mark X or O.
    x_o_dict = {}

    # if you type less or more than 2 names raise an error
    if len(player_names) != 2:
        print('')
        print('!!! There must be two players who want to play, not more, not less, try again !!!')
        tic_tac_toe_game()


    def who_x_o():
        print('')
        # ask the first play name in the list player_names what he wants to be an X or O
        x_o = input(player_names[kolkaty_hrac] + ', do you want to be an X or O? X/O: ').upper()

        # if he/she chooses X
        if x_o == 'X':
            print('')
            # set X to the first player and set O to the second player
            # name is key and his/her mark is X or O in x_o_dict dictionary
            print(player_names[kolkaty_hrac] + ', you are an X, \n' + player_names[kolkaty_hrac + 1] + ', is an O.')

            # add mark X to the first player
            x_o_dict[player_names[kolkaty_hrac]] = 'X'
            # add automatically O to the second player
            x_o_dict[player_names[kolkaty_hrac + 1]] = 'O'

        # if he/she chooses O
        elif x_o == 'O':
            print('')
            # set O to the first player and set X to the second player
            # name is key and his/her mark is X or O in x_o_dict dictionary
            print(player_names[kolkaty_hrac] + ', you are an O, \n' + player_names[kolkaty_hrac + 1] + ', is an X.')

            # add mark O to the first player
            x_o_dict[player_names[kolkaty_hrac]] = 'O'
            # add automatically X to the second player
            x_o_dict[player_names[kolkaty_hrac + 1]] = 'X'

        # if he/she writes wrong X/O
        else:
            print('')
            print(player_names[kolkaty_hrac] + ', you have type wrong X/O, try again !!!')
            who_x_o()

    who_x_o()

    # this is our tic-tac-toe list which has values/positions from 1 to 9
    tic_tac_toe_list = [
        ['1'], ['2'], ['3'],
        ['4'], ['5'], ['6'],
        ['7'], ['8'], ['9']
    ]

    # decide who is a winner
    def winner():
        global kolkaty_hrac

        def play_again():
            # type who has won, and ask if they want to start a new game
            yes_no = input('!!! Vyhral ' + player_names[kolkaty_hrac] + ', wanna play again? yes/no: ').upper()

            if yes_no == 'YES':
                print('You have decided to play again.')
                tic_tac_toe_game()

            elif yes_no == 'NO':
                print('You have decided not to play again, closing the program...')
                exit()

            else:
                print('')
                print('!!! You have typed wrong yes/no, try again !!!')
                play_again()

        # first row, 1st 2nd 3rd positions
        if tic_tac_toe_list[0][len(tic_tac_toe_list[0]) - 1] == tic_tac_toe_list[1][len(tic_tac_toe_list[1]) - 1] and tic_tac_toe_list[0][len(tic_tac_toe_list[0]) - 1] == tic_tac_toe_list[2][len(tic_tac_toe_list[2]) - 1]:

            # if that name is equal to his/hers mark, then type that he/she is the winner
            if x_o_dict[player_names[kolkaty_hrac]] == tic_tac_toe_list[0][len(tic_tac_toe_list[0]) - 1]:
                play_again()


        # second row, 4th 5th 6th positions
        elif tic_tac_toe_list[3][len(tic_tac_toe_list[3]) - 1] == tic_tac_toe_list[4][len(tic_tac_toe_list[4]) - 1] and tic_tac_toe_list[3][len(tic_tac_toe_list[3]) - 1] == tic_tac_toe_list[5][len(tic_tac_toe_list[5]) - 1]:

            # if that name is equal to his/hers mark, then type that he/she is the winner
            if x_o_dict[player_names[kolkaty_hrac]] == tic_tac_toe_list[3][len(tic_tac_toe_list[3]) - 1]:
                play_again()


        # third row, 7th 8th 9th positions
        elif tic_tac_toe_list[6][len(tic_tac_toe_list[6]) - 1] == tic_tac_toe_list[7][len(tic_tac_toe_list[7]) - 1] and tic_tac_toe_list[6][len(tic_tac_toe_list[6]) - 1] == tic_tac_toe_list[8][len(tic_tac_toe_list[8]) - 1]:

            # if that name is equal to his/hers mark, then type that he/she is the winner
            if x_o_dict[player_names[kolkaty_hrac]] == tic_tac_toe_list[6][len(tic_tac_toe_list[6]) - 1]:
                play_again()


        # first column, 1st 4th 7th positions
        elif tic_tac_toe_list[0][len(tic_tac_toe_list[0]) - 1] == tic_tac_toe_list[3][len(tic_tac_toe_list[3]) - 1] and tic_tac_toe_list[0][len(tic_tac_toe_list[0]) - 1] == tic_tac_toe_list[6][len(tic_tac_toe_list[6]) - 1]:

            # if that name is equal to his/hers mark, then type that he/she is the winner
            if x_o_dict[player_names[kolkaty_hrac]] == tic_tac_toe_list[0][len(tic_tac_toe_list[0]) - 1]:
                play_again()


        # second column, 2nd 5th 8th positions
        elif tic_tac_toe_list[1][len(tic_tac_toe_list[1]) - 1] == tic_tac_toe_list[4][len(tic_tac_toe_list[4]) - 1] and tic_tac_toe_list[1][len(tic_tac_toe_list[1]) - 1] == tic_tac_toe_list[7][len(tic_tac_toe_list[7]) - 1]:

            # if that name is equal to his/hers mark, then type that he/she is the winner
            if x_o_dict[player_names[kolkaty_hrac]] == tic_tac_toe_list[1][len(tic_tac_toe_list[1]) - 1]:
                play_again()


        # third column, 3rd 6th 9th positions
        elif tic_tac_toe_list[2][len(tic_tac_toe_list[2]) - 1] == tic_tac_toe_list[5][len(tic_tac_toe_list[5]) - 1] and tic_tac_toe_list[2][len(tic_tac_toe_list[2]) - 1] == tic_tac_toe_list[8][len(tic_tac_toe_list[8]) - 1]:

            # if that name is equal to his/hers mark, then type that he/she is the winner
            if x_o_dict[player_names[kolkaty_hrac]] == tic_tac_toe_list[2][len(tic_tac_toe_list[2]) - 1]:
                play_again()


        # first diagonal, 1st 5th 9th positions
        elif tic_tac_toe_list[0][len(tic_tac_toe_list[0]) - 1] == tic_tac_toe_list[4][len(tic_tac_toe_list[4]) - 1] and tic_tac_toe_list[0][len(tic_tac_toe_list[0]) - 1] == tic_tac_toe_list[8][len(tic_tac_toe_list[8]) - 1]:

            # type who has won, and ask if they want to start a new game
            if x_o_dict[player_names[kolkaty_hrac]] == tic_tac_toe_list[0][len(tic_tac_toe_list[0]) - 1]:
                play_again()


        # second diagonal, 3rd 5th 7th positions
        elif tic_tac_toe_list[2][len(tic_tac_toe_list[2]) - 1] == tic_tac_toe_list[4][len(tic_tac_toe_list[4]) - 1] and tic_tac_toe_list[2][len(tic_tac_toe_list[2]) - 1] == tic_tac_toe_list[6][len(tic_tac_toe_list[6]) - 1]:

            # type who has won, and ask if they want to start a new game
            if x_o_dict[player_names[kolkaty_hrac]] == tic_tac_toe_list[2][len(tic_tac_toe_list[2]) - 1]:
                play_again()

        else:
            pass


    def game_positions():
        global kolkaty_hrac, kolkaty_turn

        # kolkaty hrac je na tahu z player_name listu
        kolkaty_hrac = 0

        # kolkaty tah je zatial, zatial je 0
        kolkaty_turn = 0

        # if the first player is O, then set kolkaty_hrac to -1, 'cause we want him/her to start first
        if x_o_dict[player_names[kolkaty_hrac]] == 'O':
            kolkaty_hrac = -1

        # if the first player is X, then set kolkaty_hrac to 0, 'cause we want the second player to start the first
        elif x_o_dict[player_names[kolkaty_hrac]] == 'X':
            kolkaty_hrac = 0


        print(x_o_dict)
        print('')
        print('First who gets to choose is O.')
        print('')

        print('''
HOW TIC TAC TOE LOOKS LIKE:

     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     

positions = 1, 2, 3, 4, 5, 6, 7, 8, 9
        ''')

        # while number of turns is less or equal to 9, then keep asking and adding
        while kolkaty_turn <= 9:
            # always add one to the number of turns
            kolkaty_turn += 1

            # if number of turns is more than 9, that means that all positions have been filled and execute this code
            if kolkaty_turn > 9:
                def play_again():
                    print('')
                    print("!!! It's a TIE !!!")
                    yes_no = input('You have filled all positions, wanna try a new game? yes/no: ').upper()

                    if yes_no == 'YES':
                        print('')
                        print('You have decided to play again.')
                        tic_tac_toe_game()

                    elif yes_no == 'NO':
                        print('')
                        print('You have decided not to play again, closing the program...')
                        exit()

                    else:
                        print('')
                        print('!!! You have typed wrong yes/no, try again !!!')
                        play_again()

                play_again()

            else:
                pass

            def turns_9():
                global kolkaty_hrac, kolkaty_turn

                def tic_tac_toe_board():
                    # print the whole tic-tac-toe board and the marks where to players have chosen them the place to be placed
                    # [len(tic_tac_toe_list[0]) - 1] == get the amount of elements in the specific list and print out the last one -->
                    # if amount is 2 then 2 - 1 == 1 and that means it's going to -->
                    # print the last element from that list which is the players mark X/O
                    # if amount is 1 then 1 - 1 == 0 and that means it's going to -->
                    # print the the first/last (only one element in that list) element which is the number of position 1/2/3/4/5/6/7/8/9

                    print('     |     |')
                    print('  ' + tic_tac_toe_list[0][len(tic_tac_toe_list[0]) - 1] + '  |  ' + tic_tac_toe_list[1][
                        len(tic_tac_toe_list[1]) - 1] + '  |  '
                          + tic_tac_toe_list[2][len(tic_tac_toe_list[2]) - 1])
                    print('_____|_____|_____')
                    print('     |     |   ')
                    print('  ' + tic_tac_toe_list[3][len(tic_tac_toe_list[3]) - 1] + '  |  ' + tic_tac_toe_list[4][
                        len(tic_tac_toe_list[4]) - 1] + '  |  ' +
                          tic_tac_toe_list[5][len(tic_tac_toe_list[5]) - 1])
                    print('_____|_____|_____')
                    print('     |     |')
                    print('  ' + tic_tac_toe_list[6][len(tic_tac_toe_list[6]) - 1] + '  |  ' + tic_tac_toe_list[7][
                        len(tic_tac_toe_list[7]) - 1] + '  |  ' +
                          tic_tac_toe_list[8][len(tic_tac_toe_list[8]) - 1])
                    print('     |     |')

                # kolkaty_hrac plus one 'cause we want to move to another player, chceme aby sa striedali
                kolkaty_hrac += 1
                # if kolkaty_hrac is gonna be more than 1, we want him to start from the beginning, then kolkaty_hrac = 0
                if kolkaty_hrac > 1:
                    kolkaty_hrac = 0

                print('')
                print(player_names[kolkaty_hrac] + ' == ' + x_o_dict[player_names[kolkaty_hrac]] + "'s turn, turn: " + str(kolkaty_turn) + '.')
                what_position = input(player_names[kolkaty_hrac] + ', in which position you want to go? 1/2/3/4/5/6/7/8/9: ')

                if what_position == '1':

                    def position_1():
                        global kolkaty_hrac

                        # if number of characters is more than 1, then this means that that (1st) position has already been taken
                        if len(tic_tac_toe_list[0]) > 1:
                            print('')
                            print('!!! This position is already taken, try another one !!!')

                            # 'cause kolkaty_hrac is still being added value plus one -->
                            # and now we hit an 'error', and nothing is being added in tic-tac-toe -->
                            # then if kolkaty_hrac is at the last (1) position, then subtract one to equalize it -->
                            # in order to start from the last (1) position; kolkaty_hrac += 1 == kolkaty_hrac -= 1
                            if kolkaty_hrac == 1:
                                kolkaty_hrac -= 1

                            # but when we are at the first (0) position, then just set the kolkaty_hrac to -1 -->
                            # in order to start it from the first (0) position again, when that 'error' occurs
                            elif kolkaty_hrac == 0:
                                kolkaty_hrac = -1

                            turns_9()

                        else:
                            # add that players mark to the tic-tac-toe list in the 1st position
                            tic_tac_toe_list[0].append(x_o_dict[player_names[kolkaty_hrac]])
                            print('')
                            print(x_o_dict)
                            print('')

                            tic_tac_toe_board()

                            # call the winner() function is order to decide if there is a winner or not
                            winner()

                    position_1()


                elif what_position == '2':

                    def position_2():
                        global kolkaty_hrac

                        # if number of characters is more than 1, then this means that that (2nd) position has already been taken
                        if len(tic_tac_toe_list[1]) > 1:
                            print('')
                            print('!!! This position is already taken, try another one !!!')

                            # 'cause kolkaty_hrac is still being added value plus one -->
                            # and now we hit an 'error', and nothing is being added in tic-tac-toe -->
                            # then if kolkaty_hrac is at the last (1) position, then subtract one to equalize it -->
                            # in order to start from the last (1) position; kolkaty_hrac += 1 == kolkaty_hrac -= 1
                            if kolkaty_hrac == 1:
                                kolkaty_hrac -= 1

                            # but when we are at the first (0) position, then just set the kolkaty_hrac to -1 -->
                            # in order to start it from the first (0) position again, when that 'error' occurs
                            elif kolkaty_hrac == 0:
                                kolkaty_hrac = -1

                            turns_9()

                        else:
                            # add that players mark to the tic-tac-toe list in the 2nd position
                            tic_tac_toe_list[1].append(x_o_dict[player_names[kolkaty_hrac]])
                            print('')
                            print(x_o_dict)
                            print('')

                            tic_tac_toe_board()

                            # call the winner() function is order to decide if there is a winner or not
                            winner()

                    position_2()

                elif what_position == '3':

                    def position_3():
                        global kolkaty_hrac

                        # if number of characters is more than 1, then this means that that (3rd) position has already been taken
                        if len(tic_tac_toe_list[2]) > 1:
                            print('')
                            print('!!! This position is already taken, try another one !!!')

                            # 'cause kolkaty_hrac is still being added value plus one -->
                            # and now we hit an 'error', and nothing is being added in tic-tac-toe -->
                            # then if kolkaty_hrac is at the last (1) position, then subtract one to equalize it -->
                            # in order to start from the last (1) position; kolkaty_hrac += 1 == kolkaty_hrac -= 1
                            if kolkaty_hrac == 1:
                                kolkaty_hrac -= 1

                            # but when we are at the first (0) position, then just set the kolkaty_hrac to -1 -->
                            # in order to start it from the first (0) position again, when that 'error' occurs
                            elif kolkaty_hrac == 0:
                                kolkaty_hrac = -1

                            turns_9()

                        else:
                            # add that players mark to the tic-tac-toe list in the 3rd position
                            tic_tac_toe_list[2].append(x_o_dict[player_names[kolkaty_hrac]])
                            print('')
                            print(x_o_dict)
                            print('')

                            tic_tac_toe_board()

                            # call the winner() function is order to decide if there is a winner or not
                            winner()

                    position_3()


                elif what_position == '4':

                    def position_4():
                        global kolkaty_hrac

                        # if number of characters is more than 1, then this means that that (4th) position has already been taken
                        if len(tic_tac_toe_list[3]) > 1:
                            print('')
                            print('!!! This position is already taken, try another one !!!')

                            # 'cause kolkaty_hrac is still being added value plus one -->
                            # and now we hit an 'error', and nothing is being added in tic-tac-toe -->
                            # then if kolkaty_hrac is at the last (1) position, then subtract one to equalize it -->
                            # in order to start from the last (1) position; kolkaty_hrac += 1 == kolkaty_hrac -= 1
                            if kolkaty_hrac == 1:
                                kolkaty_hrac -= 1

                            # but when we are at the first (0) position, then just set the kolkaty_hrac to -1 -->
                            # in order to start it from the first (0) position again, when that 'error' occurs
                            elif kolkaty_hrac == 0:
                                kolkaty_hrac = -1

                            turns_9()

                        else:
                            # add that players mark to the tic-tac-toe list in the 4th position
                            tic_tac_toe_list[3].append(x_o_dict[player_names[kolkaty_hrac]])
                            print('')
                            print(x_o_dict)
                            print('')

                            tic_tac_toe_board()

                            # call the winner() function is order to decide if there is a winner or not
                            winner()

                    position_4()


                elif what_position == '5':

                    def position_5():
                        global kolkaty_hrac

                        # if number of characters is more than 1, then this means that that (5th) position has already been taken
                        if len(tic_tac_toe_list[4]) > 1:
                            print('')
                            print('!!! This position is already taken, try another one !!!')

                            # 'cause kolkaty_hrac is still being added value plus one -->
                            # and now we hit an 'error', and nothing is being added in tic-tac-toe -->
                            # then if kolkaty_hrac is at the last (1) position, then subtract one to equalize it -->
                            # in order to start from the last (1) position; kolkaty_hrac += 1 == kolkaty_hrac -= 1
                            if kolkaty_hrac == 1:
                                kolkaty_hrac -= 1

                            # but when we are at the first (0) position, then just set the kolkaty_hrac to -1 -->
                            # in order to start it from the first (0) position again, when that 'error' occurs
                            elif kolkaty_hrac == 0:
                                kolkaty_hrac = -1

                            turns_9()

                        else:
                            # add that players mark to the tic-tac-toe list in the 5th position
                            tic_tac_toe_list[4].append(x_o_dict[player_names[kolkaty_hrac]])
                            print('')
                            print(x_o_dict)
                            print('')

                            tic_tac_toe_board()

                            # call the winner() function is order to decide if there is a winner or not
                            winner()

                    position_5()


                elif what_position == '6':

                    def position_6():
                        global kolkaty_hrac

                        # if number of characters is more than 1, then this means that that (6th) position has already been taken
                        if len(tic_tac_toe_list[5]) > 1:
                            print('')
                            print('!!! This position is already taken, try another one !!!')

                            # 'cause kolkaty_hrac is still being added value plus one -->
                            # and now we hit an 'error', and nothing is being added in tic-tac-toe -->
                            # then if kolkaty_hrac is at the last (1) position, then subtract one to equalize it -->
                            # in order to start from the last (1) position; kolkaty_hrac += 1 == kolkaty_hrac -= 1
                            if kolkaty_hrac == 1:
                                kolkaty_hrac -= 1

                            # but when we are at the first (0) position, then just set the kolkaty_hrac to -1 -->
                            # in order to start it from the first (0) position again, when that 'error' occurs
                            elif kolkaty_hrac == 0:
                                kolkaty_hrac = -1

                            turns_9()

                        else:
                            # add that players mark to the tic-tac-toe list in the 6th position
                            tic_tac_toe_list[5].append(x_o_dict[player_names[kolkaty_hrac]])
                            print('')
                            print(x_o_dict)
                            print('')

                            tic_tac_toe_board()

                            # call the winner() function is order to decide if there is a winner or not
                            winner()

                    position_6()


                elif what_position == '7':

                    def position_7():
                        global kolkaty_hrac

                        # if number of characters is more than 1, then this means that that (7th) position has already been taken
                        if len(tic_tac_toe_list[6]) > 1:
                            print('')
                            print('!!! This position is already taken, try another one !!!')

                            # 'cause kolkaty_hrac is still being added value plus one -->
                            # and now we hit an 'error', and nothing is being added in tic-tac-toe -->
                            # then if kolkaty_hrac is at the last (1) position, then subtract one to equalize it -->
                            # in order to start from the last (1) position; kolkaty_hrac += 1 == kolkaty_hrac -= 1
                            if kolkaty_hrac == 1:
                                kolkaty_hrac -= 1

                            # but when we are at the first (0) position, then just set the kolkaty_hrac to -1 -->
                            # in order to start it from the first (0) position again, when that 'error' occurs
                            elif kolkaty_hrac == 0:
                                kolkaty_hrac = -1

                            turns_9()

                        else:
                            # add that players mark to the tic-tac-toe list in the 7th position
                            tic_tac_toe_list[6].append(x_o_dict[player_names[kolkaty_hrac]])
                            print('')
                            print(x_o_dict)
                            print('')

                            tic_tac_toe_board()

                            # call the winner() function is order to decide if there is a winner or not
                            winner()

                    position_7()


                elif what_position == '8':

                    def position_8():
                        global kolkaty_hrac

                        # if number of characters is more than 1, then this means that that (8th) position has already been taken
                        if len(tic_tac_toe_list[7]) > 1:
                            print('')
                            print('!!! This position is already taken, try another one !!!')

                            # 'cause kolkaty_hrac is still being added value plus one -->
                            # and now we hit an 'error', and nothing is being added in tic-tac-toe -->
                            # then if kolkaty_hrac is at the last (1) position, then subtract one to equalize it -->
                            # in order to start from the last (1) position; kolkaty_hrac += 1 == kolkaty_hrac -= 1
                            if kolkaty_hrac == 1:
                                kolkaty_hrac -= 1

                            # but when we are at the first (0) position, then just set the kolkaty_hrac to -1 -->
                            # in order to start it from the first (0) position again, when that 'error' occurs
                            elif kolkaty_hrac == 0:
                                kolkaty_hrac = -1

                            turns_9()

                        else:
                            # add that players mark to the tic-tac-toe list in the 8th position
                            tic_tac_toe_list[7].append(x_o_dict[player_names[kolkaty_hrac]])
                            print('')
                            print(x_o_dict)
                            print('')

                            tic_tac_toe_board()

                            # call the winner() function is order to decide if there is a winner or not
                            winner()

                    position_8()


                elif what_position == '9':

                    def position_9():
                        global kolkaty_hrac

                        # if number of characters is more than 1, then this means that that (9th) position has already been taken
                        if len(tic_tac_toe_list[8]) > 1:
                            print('')
                            print('!!! This position is already taken, try another one !!!')

                            # 'cause kolkaty_hrac is still being added value plus one -->
                            # and now we hit an 'error', and nothing is being added in tic-tac-toe -->
                            # then if kolkaty_hrac is at the last (1) position, then subtract one to equalize it -->
                            # in order to start from the last (1) position; kolkaty_hrac += 1 == kolkaty_hrac -= 1
                            if kolkaty_hrac == 1:
                                kolkaty_hrac -= 1

                            # but when we are at the first (0) position, then just set the kolkaty_hrac to -1 -->
                            # in order to start it from the first (0) position again, when that 'error' occurs
                            elif kolkaty_hrac == 0:
                                kolkaty_hrac = -1

                            turns_9()

                        else:
                            # add that players mark to the tic-tac-toe list in the 9th position
                            tic_tac_toe_list[8].append(x_o_dict[player_names[kolkaty_hrac]])
                            print('')
                            print(x_o_dict)
                            print('')

                            tic_tac_toe_board()

                            # call the winner() function is order to decide if there is a winner or not
                            winner()

                    position_9()

                # if the player haven't chosen any of the positions 1/2/3/4/5/6/7/8/9, and typed obvious bullshit
                else:
                    print('')
                    # type the player's name and remind him/her a mistake he/she made and ask him/her to try again
                    print(player_names[kolkaty_hrac] + ''', you have chosen the wrong position; 
positions == 1/2/3/4/5/6/7/8/9, try again!!! ''')

                    # 'cause kolkaty_hrac is still being added value plus one -->
                    # and now we hit an 'error', and nothing is being added in tic-tac-toe -->
                    # then if kolkaty_hrac is at the last (1) position, then subtract one to equalize it -->
                    # in order to start from the last (1) position; kolkaty_hrac += 1 == kolkaty_hrac -= 1
                    if kolkaty_hrac == 1:
                        kolkaty_hrac -= 1

                    # but when we are at the first (0) position, then just set the kolkaty_hrac to -1 -->
                    # in order to start it from the first (0) position again, when that 'error' occurs
                    elif kolkaty_hrac == 0:
                        kolkaty_hrac = -1

                    turns_9()

            turns_9()


    game_positions()


tic_tac_toe_game()

