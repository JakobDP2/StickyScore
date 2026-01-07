import json
import urllib.request

# De URL van je Firebase database
url = "https://stickysituations-4bb14-default-rtdb.europe-west1.firebasedatabase.app/scores.json"

def count_players():
    try:
        # 1. Verbinding maken met de database en de ruwe JSON data ophalen
        with urllib.request.urlopen(url) as response:
            if response.getcode() == 200:
                # Data inlezen en decoderen
                raw_data = response.read().decode()
                data = json.loads(raw_data)
                
                # Check of er data is (database kan leeg zijn of 'null' teruggeven)
                if not data:
                    print("De database is leeg of onbereikbaar.")
                    return

                # 2. Deelnemers tellen
                # Firebase geeft data terug als een dictionary: { "id1": {...}, "id2": {...} }
                # We maken een lijst van alle spelers die NIET "TestPlayer" heten.
                real_players = [
                    entry for entry in data.values() 
                    if entry.get('name') != "TestPlayer"
                ]
                
                count = len(real_players)
                
                print("-" * 30)
                print(f"Totaal aantal database entries: {len(data)}")
                print(f"Aantal 'TestPlayer' entries:   {len(data) - count}")
                print("-" * 30)
                print(f"EINDTOTAAL ECHTE DEELNEMERS:  {count}")
                print("-" * 30)
                
            else:
                print(f"Fout bij ophalen data. HTTP Status code: {response.getcode()}")
                
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

if __name__ == "__main__":
    count_players()