# F1 Stats Tracker

A Python script that pulls live 2026 Formula 1 standings from the Jolpica API and displays them as a formatted table in the terminal.

## How to run

1. Install dependencies:
   ```
   pip install requests
   ```

2. Run the script:
   ```
   python f1_explorer.py
   ```

## What it shows

- Driver championship standings
- Position, name, team, points, wins

## What's next

- Add podiums column (calculating from race results endpoint)
- Add pole positions column
- Wrap in Flask as a web app
