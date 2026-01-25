"""
Imagine you have a dataset with information about your favorite sports team. 🏀🎾⚽ The goal is to use Python's data structures to organize and analyze this data.

If you can't think of any, feel free to use the Super Bowl 2024 champions, the Kansas City Chiefs. 🏈

As a data analyst for the Kansas City Chiefs you have been given a dataset containing information about the players, their positions, and some game statistics.

Let's start analyzing!

    Create a list of dictionaries where each dictionary represents a player. Include attributes such as 'name,' 'position,' and 'jersey number.'
    Print out a list of all player positions in the dataset.
    Choose a player and update their game statistics in the dataset.
    Calculate the average statistics (e.g., yards gained, touchdowns) for all players and print the results.

"""

players = [
    {
        "name" : "Ronaldo"  ,
        "position" : "CF" ,
        "jersey_number" : 7
    },
    {
        "name" : "Messi"  ,
        "position" : "RW" ,
        "jersey_number" : 10
    } ,
    {
        "name" : "Kohli"  ,
        "position" : "Batsman" ,
        "jersey_number" : 18
    } ,
    {
        "name" : "Dhoni"  ,
        "position" : "WK" ,
        "jersey_number" : 7
    }
]
positions = []
for player in players :
    positions.append(player["position"])

unique_positions = set(positions)
print(unique_positions)