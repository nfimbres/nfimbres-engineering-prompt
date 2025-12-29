# Head-to-Head Records Matrix


This solution reads a JSON file containing each team's win-loss records versus opponents and builds both a matrix and a pandas DataFrame displaying only the number of wins (W) for each matchup. The code prints both formats with clear titles for easy comparison. It is written in Python for clarity and ease of use.

## How It Works


1. **Input**: The program expects a JSON file (e.g., `prompt.json`) with a structure like:

```
{
  "TeamA": {"TeamB": {"W": 2, "L": 1}, "TeamC": {"W": 1, "L": 2}},
  "TeamB": {"TeamA": {"W": 1, "L": 2}, "TeamC": {"W": 3, "L": 0}},
  "TeamC": {"TeamA": {"W": 2, "L": 1}, "TeamB": {"W": 0, "L": 3}}
}
```

2. **Processing**:
   - Reads the JSON data.
   - Extracts all team names.
   - Builds a matrix where each cell `[i][j]` shows the number of wins for team `i` vs team `j`.

3. **Output**:
   - Prints a formatted matrix table to the console, showing only the number of wins (W) for each matchup, with the title "Head-to-Head Wins Matrix:".
   - Prints a pandas DataFrame of the same data, with the title "Head-to-Head Wins DataFrame:".

## Usage

1. Place your JSON data in a file named `prompt.json` in the same directory as the script.
2. Run the script:

```
python solution.py
```

3. Both the head-to-head matrix and the pandas DataFrame will be printed in the terminal, each with a title.

## Example Output

```
Head-to-Head Wins Matrix:

       | TeamA | TeamB | TeamC
-------+-------+-------+-------
TeamA  | -     | 2     | 1    
TeamB  | 1     | -     | 3    
TeamC  | 2     | 0     | -    

Head-to-Head Wins DataFrame:

      TeamA TeamB TeamC
TeamA     -     2     1
TeamB     1     -     3
TeamC     2     0     -
```

## Notes
- The code requires the `pandas` library. Install it with `pip install pandas` if not already installed.
- You can easily adapt the script to read from a different file or output to a CSV if needed.
