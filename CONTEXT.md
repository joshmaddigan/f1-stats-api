# Project Context for Claude

Read this at the start of a new session to get up to speed.

## Who I am

Beginner-to-intermediate Python learner. Comfortable with loops, functions, lists, dictionaries, and basic OOP. Working toward a backend dev job using Python. Main learning project is a Tamagotchi-style game called Pixel Pal.

## Teaching preferences

- One concept at a time — don't pile on
- Nudge before solution — give hints first, not answers
- No code dumps unless explicitly asked
- Point out the most important mistake only
- I work well with checklists for multi-step plans

## This project

An F1 2026 season stats tracker. Pulls live data from the Jolpica API and displays it as a formatted terminal table.

**GitHub:** https://github.com/joshmaddigan/f1-stats-api

## Current state

`f1_explorer.py` does the following:
- Hits `https://api.jolpi.ca/ergast/f1/2026/driverstandings/` 
- Navigates the nested JSON: `MRData > StandingsTable > StandingsLists[0] > DriverStandings`
- Loops through drivers and prints a formatted table with: position, first name, last name, team, points, wins

## Why Jolpica (not OpenF1 or FastF1)

- FastF1 was tried before and was too complex — hides the request/response cycle
- OpenF1 splits driver names and standings across multiple endpoints, requires merging
- Jolpica returns everything in one clean response — keeps it simple

## What's done

- [x] Basic API call with `requests`
- [x] JSON navigation
- [x] Formatted table output with header row
- [x] Pushed to GitHub

## What's next

- [ ] Podiums column — endpoint is `https://api.jolpi.ca/ergast/f1/2026/results/` — need to count finishing positions <= 3 per driver across all races
- [ ] Poles column — not yet investigated, likely from qualifying results endpoint
- [ ] Flask web app wrapper (end goal)

## Key concepts covered so far

- `requests.get()` and `response.json()`
- Navigating nested JSON like Python dictionaries
- f-string formatting with alignment (`<`, `>`, `^`) and fixed widths
