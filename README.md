# Oh Baby Games League Generator

Oh Baby Games League Generator is a Python-based project designed to facilitate the organization and management of gaming leagues. The project includes functionality for generating game schedules, ensuring balanced player participation across regions, and avoiding repeated player assignments.

## Features

- **Game Generation**: Automatically generates game schedules with balanced player participation.
- **Region Management**: Supports players from both EU and NA regions.
- **Player Participation Tracking**: Tracks the number of games each player participates in to ensure fair distribution.
- **Repeat Avoidance**: Checks for and minimizes repeated player assignments in the same game.

## Files

- `final.py`: Script to read player names from `names.txt`, generate game schedules, and write the results to `games.txt`.
- `finalfor36.py`: Similar to `final.py`, but designed for a different set of player names stored in `names36.txt`.
- `test.py`: Script to parse the generated games, check for repeated players, and count player participation across games.
- `games.txt`: Example output file containing the generated game schedules.
- `names.txt`: List of 24 player names for generating game schedules with `final.py`.
- `names36.txt`: List of 36 player names for generating game schedules with `finalfor36.py`.

## Differences Between 24-Player and 36-Player Versions

The project supports two versions for generating game schedules, catering to leagues with different numbers of players:

- **24-Player Version (`final.py`)**:
  - Uses the `names.txt` file containing 24 player names.
  - Generates game schedules where each game has balanced participation from EU and NA regions.
  - Ensures that no player exceeds a maximum number of games per region.

- **36-Player Version (`finalfor36.py`)**:
  - Uses the `names36.txt` file containing 36 player names.
  - Generates game schedules with an additional consideration for repeated players in a specific region.
  - Alternates between regions for repeated players to maintain balance and fairness.
  - Ensures that no player exceeds a maximum number of games per region, with slightly different balancing logic compared to the 24-player version.

## Usage

1. **Generate Game Schedules**:
    - Ensure `names.txt` or `names36.txt` is populated with player names.
    - Run `final.py` to generate game schedules using `names.txt`:
      ```sh
      python final.py
      ```
    - Run `finalfor36.py` to generate game schedules using `names36.txt`:
      ```sh
      python finalfor36.py
      ```

2. **Check Game Schedules**:
    - Use `test.py` to parse and check the generated games for repeated players and participation counts:
      ```sh
      python test.py
      ```

## Example Output

The generated game schedules will be written to `games.txt`. Below is a sample format:

```
Game 1:
EU Region: Player1, Player2, Player3, ...
NA Region: Player4, Player5, Player6, ...
Repeated NA Region: Player7, Player8, Player9, ...

Game 2:
EU Region: Player10, Player11, Player12, ...
NA Region: Player13, Player14, Player15, ...
Repeated EU Region: Player16, Player17, Player18, ...
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact the Oh Baby Games team at [ohbabygames.com.](https://ohbabygames.com/support) or you can contact me at my email danielyankovich03@gmail.com or through the Oh Baby Games discord @dantheopman
