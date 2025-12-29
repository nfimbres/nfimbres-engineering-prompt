
"""
head-to-head records matrix generator

reads a json file (e.g., prompt.json) containing each team's win-loss records versus opponents and prints a matrix table.
"""
import json
import os
import pandas as pd  # add pandas import

def load_data(filename):
    # open and read the json file
    with open(filename, 'r') as f:
        return json.load(f)

def build_matrix(data):
    # get all team names and sort them
    teams = sorted(data.keys())
    matrix = []
    for team in teams:
        row = []
        for opponent in teams:
            if team == opponent:
                # dash for same team
                row.append('-')
            else:
                # get the record for team vs opponent
                record = data.get(team, {}).get(opponent, '')
                if isinstance(record, dict):
                    # only show wins
                    w = record.get('W', '')
                    row.append(str(w))
                else:
                    row.append(str(record))
        matrix.append(row)
    return teams, matrix

def print_matrix(teams, matrix):
    # print the matrix title
    print("Head-to-Head Wins Matrix:\n")
    # print the table header
    header = [''] + teams
    # calculate column widths
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(header, *matrix)]
    # create format string for each row
    fmt = ' | '.join('{{:{}}}'.format(w) for w in col_widths)
    print(fmt.format(*header))
    # print separator line
    print('-+-'.join('-' * w for w in col_widths))
    # print each row
    for team, row in zip(teams, matrix):
        print(fmt.format(team, *row))

def main():
    # set the input file name
    filename = 'prompt.json'
    # check if file exists
    if not os.path.exists(filename):
        print(f"file '{filename}' not found.")
        return
    # load data from file
    data = load_data(filename)
    # build the matrix
    teams, matrix = build_matrix(data)
    # print the matrix with a title
    print_matrix(teams, matrix)
    # create and print pandas dataframe with a title
    matrix_for_df = [[cell if cell == '-' else cell for cell in row] for row in matrix]
    df = pd.DataFrame(matrix_for_df, index=teams, columns=teams)
    print("\nHead-to-Head Wins DataFrame:\n")
    print(df)

if __name__ == '__main__':
    # run the main function
    main()
