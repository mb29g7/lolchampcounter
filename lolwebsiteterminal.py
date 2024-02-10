import webbrowser

# List of champions
champions = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Azir",
"Bard", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Briar", 
"Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki",
"Darius", "Diana", "Dr. Mundo", "Draven", 
"Ekko", "Elise", "Evelynn", "Ezreal",          
"Fiddlesticks", "Fiora", "Fizz", 
"Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", 
"Hecarim", "Heimerdinger", "Hwei", "Illaoi", "Irelia", "Ivern", 
"Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx",
"Kai'Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw","K'Sante",            
"LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi","Milio", "Miss Fortune", "Mordekaiser", "Morgana",
"Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nocturne", "Nunu & Willump","Nilah",            
"Olaf", "Orianna", "Ornn",
"Pantheon", "Poppy", "Pyke", 
"Qiyana", "Quinn",          
"Rakan", "Rammus", "Rek'Sai", "Rell","Renata", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", 
"Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra",
"Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch",
"Udyr", "Urgot", 
"Varus", "Vayne", "Veigar", "Vel'Koz","Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", 
"Warwick", "Wukong", 
"Xayah", "Xerath", "Xin Zhao", 
"Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed","Zerri", "Ziggs", "Zilean", "Zoe", "Zyra"]


# Ask the user to select a champion

champion = input("Please select a champion from the list: ")

# Convert the user's input to title case
champion = champion.title()

# Check if the selected champion is in the list
if champion in champions:
    # Define the URLs
    urls = [
        f"https://www.counterstats.net/league-of-legends/{champion.lower()}",
        f"https://lolalytics.com/lol/{champion.lower()}/build/?patch=30",
        f"https://u.gg/lol/champions/{champion.lower()}/counter"
    ]

    # Open each URL in a new browser tab
    for url in urls:
        webbrowser.open_new_tab(url)
else:
    print("The selected champion is not in the list.")
