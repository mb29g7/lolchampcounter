import webbrowser
import tkinter as tk
from tkinter import ttk

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

# Function to open the URLs
def open_urls():
    # Get the selected champion
    champion = champion_var.get()

    # Define the URLs
    urls = [
       ## f"https://www.counterstats.net/league-of-legends/{champion.lower()}",
        f"https://lolalytics.com/lol/{champion.lower()}/build/?patch=30",
        f"https://u.gg/lol/champions/{champion.lower()}/counter"
    ]

    # Open each URL in a new browser tab
    for url in urls:
        webbrowser.open_new_tab(url)

# Create the main window
root = tk.Tk()

# Create a StringVar for the champion
champion_var = tk.StringVar()

# Create a Combobox for selecting a champion
champion_cb = ttk.Combobox(root, textvariable=champion_var)
champion_cb['values'] = champions
champion_cb.grid(column=0, row=0)

# Create a Button for opening the URLs
open_btn = ttk.Button(root, text="Open URLs", command=open_urls)
open_btn.grid(column=1, row=0)

# Start the main loop
root.mainloop()
