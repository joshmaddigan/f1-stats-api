import requests

response = requests.get("https://api.jolpi.ca/ergast/f1/2026/driverstandings/")

data = response.json()


# print(data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["points"])

print(f"{'Pos':<5} {'Driver':^31} {'Team':<15} {'Points'} {'Wins'}")
for driver in data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]:
    print(f"{driver['position']:<5} {driver["Driver"]["givenName"]:<15} {driver['Driver']['familyName']:<15} {driver['Constructors'][0]['name']:<18} {driver['points']:<4} {driver['wins']:<2}")