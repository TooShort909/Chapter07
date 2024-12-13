def world_series_champions():
    # Read the list of World Series winners from the file
    with open('WorldSeriesWinners.txt', 'r') as file:
        winners = [line.strip() for line in file.readlines()]

    # Ask the user for a team name
    team_name = input("Enter the name of a team to check how many times they won the World Series: ").strip()

    # Count how many times the team won
    count = winners.count(team_name)
    
    print(f"The team {team_name} has won the World Series {count} times.")

world_series_champions()