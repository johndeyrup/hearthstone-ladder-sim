'''
Created on January 11, 2015
Models the Hearthstone Ladder System
allowing you to determine how long it
will take to reach the top of the ladder
@author: John Deyrup
'''
import random
import matplotlib.pyplot as plt

#Simulates playing a game in Hearthstone
def play_a_game(win_chance):
    game_result = random.randint(1,100)
    if win_chance >= game_result:
        return True

'''
Keep playing games until player receives
96 stars. Every time a player wins a game
he receives 1 star unless he has won the 
last 2 games in a row. In this case he will
two stars as long he has less than 60 stars.
A player loses a star every time he loses a
game as long as he has more than 10 stars.
'''
def play_a_series(current_stars, win_chance):    
    stars = current_stars
    game_win_streak = 0
    stars_won = []
    while stars < 96:
        if play_a_game(win_chance):
            game_win_streak += 1
            if game_win_streak > 2 and stars < 60:
                stars += 2
            else:
                stars += 1
        else:
            game_win_streak = 0
            if stars > 10:
                stars -= 1
        stars_won.append(stars)
    return stars_won

#Plot series with a given win chance and print how long it 
#will take to reach the maximum rank
def plot_series(number_series, win_chance, current_stars, game_time):
    total_game_length = []
    for i in range(number_series):
        series_played = play_a_series(current_stars, win_chance)
        plt.plot(series_played)
        total_game_length.append(len(series_played))
    average_game = sum(total_game_length)/len(total_game_length)
    print("It will take an average of %d hours %d minutes and %d games to reach legendary" % 
          (int(game_time*average_game/60), game_time*average_game%60, average_game))
    plt.ylabel("Stars Won")
    plt.xlabel("Games Played")
    plt.show()

#Creates a dictionary with the total amount of stars for each rank    
def create_rank_dic():
    rank_dic = {}
    stars = 0
    for i in range(25,0,-1):
        rank_dic[str(i)] = stars
        if i > 20:
            stars += 2
        elif i > 15:
            stars += 3
        elif i > 10:
            stars += 4
        else:
            stars += 5 
    return rank_dic

rank = input("Enter your current rank ")
stars = int(input("Enter your current stars "))
player_win_rate = int(input("Enter your win rate as integer "))
player_game_time = float(input("Enter your average game time "))
current_stars = create_rank_dic()[rank] + stars    
plot_series(1000,player_win_rate,current_stars,player_game_time)
