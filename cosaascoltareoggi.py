import tkinter as tk
import random
import webbrowser
import os

class MusicApp:
    def __init__(self, master):
        self.master = master
        master.title("Cosa ascoltare oggi?")

        # Configurazione della finestra
        master.configure(bg='#222')
        master.geometry("400x350")

        # Impostazione dell'icona
        if os.path.exists("el.ico"):
            master.iconbitmap("el.ico")
        else:
            print("Attenzione: Il file 'el.ico' non è stato trovato nella directory corrente.")

        # Titolo
        self.label = tk.Label(master, text="Cosa ascoltare oggi?", fg="white", bg="#222", font=("Arial", 24))
        self.label.pack(pady=20)

        # Descrizione
        self.description = tk.Label(master, text="Clicca sul pulsante 'Ci pensa EL' per ottenere un album da ascoltare.", 
                                    fg="white", bg="#222", font=("Arial", 12), wraplength=350)
        self.description.pack(pady=10)

        # Pulsante
        self.button = tk.Button(master, text="Ci pensa EL", command=self.generate_youtube_link,
                                bg="white", fg="blue", font=("Arial", 16))
        self.button.pack(pady=20)

        # Scritta in basso
        self.credits = tk.Label(master, text="Realizzato da ELPythonEMI", fg="white", bg="#222", font=("Arial", 10))
        self.credits.pack(side=tk.BOTTOM, pady=10)

        self.albums = [
            "Pink Floyd - The Dark Side of the Moon",
            "Led Zeppelin - IV",
            "The Rolling Stones - Exile on Main St.",
            "The Who - Who's Next ",
            "Queen - A Night at the Opera",
            "The Eagles - Hotel California",
            "The Doors - L.A. Woman",
            "David Bowie - The Rise and Fall of Ziggy Stardust and the Spiders from Mars ",
            "Neil Young - Harvest",
            "Fleetwood Mac - Rumours ",
            "Aerosmith - Toys in the Attic",
            "Pink Floyd - Wish You Were Here",
            "Bob Dylan - Blood on the Tracks",
            "Deep Purple - Machine Head",
            "Queen - Sheer Heart Attack",
            "The Allman Brothers Band - At Fillmore East",
            "AC/DC - High Voltage",
            "Black Sabbath - Paranoid",
            "Elton John - Goodbye Yellow Brick Road",
            "Bruce Springsteen - Born to Run",
            "Genesis - The Lamb Lies Down on Broadway",
            "Jimi Hendrix - Axis: Bold as Love",
            "Jethro Tull - Aqualung",
            "Van Morrison - Moondance",
            "Yes - Fragile",
            "The Clash - London Calling",
            "Emerson, Lake & Palmer - Brain Salad Surgery",
            "Supertramp - Breakfast in America",
            "The Ramones - Ramones",
            "Judas Priest - British Steel",
            "Blind Guardian - Battalions of Fear",
            "Rush - 2112",
            "MOTÖRHEAD - ACE OF SPADES",
            "SAXON - DENIM AND LEATHER",
            "DEF LEPPARD - PYROMANIA",
            "SLAYER - SOUTH OF HEAVEN",
            "KISS - LOVE GUN",
            "RAINBOW - LONG LIVE ROCK 'N' ROLL",
            "MEGADETH - KILLING IS MY BUSINESS... AND BUSINESS IS GOOD",
            "THIN LIZZY - BAD REPUTATION",
            "VENOM - BLACK METAL VENOM",
            "QUEENSRŸCHE - THE WARNING ",
            "BLUE ÖYSTER CULT - AGENTS OF FORTUNE",
            "URIAH HEEP - DEMONS AND WIZARDS",
            "QUIET RIOT - METAL HEALTH",
            "SUICIDAL TENDENCIES - LIGHTS CAMERA REVOLUTION",
            "YNGWIE MALMSTEEN - TRILOGY ",
            "SLAYER - SEASONS IN THE ABYSS",
            "HELLOWEEN - WALLS OF JERICHO",
            "MOTÖRHEAD - 1916",
            "L.A. GUNS - L.A. GUNS",
            "JUDAS PRIEST - DEFENDERS OF THE FAITH",
            "MEGADETH - RUST IN PEACE",
            "ANTHRAX STATE OF EUPHORIA",
            "RAINBOW - RISING",
            "Vasco Rossi - Bollicine",
            "Ligabue - Buon Compleanno Elvis",
            "Pino Daniele - Nero a Metà ",
            "Afterhours - Hai Paura del Buio?",
            "Subsonica - Microchip Emozionale",
            "Verdena - Solo un Grande Sasso",
            "CCCP - Fedeli Alla Linea",
            "Litfiba - El Diablo",
            "Litfiba - Mondi Sommersi",
            "Franco Battiato - La Voce del Padrone",
            "Bluvertigo - Zero",
            "Il Rovescio della Medaglia - Contaminazione",
            "Negrita - Mama Maè ",
            "Marlene Kuntz - Il Vile",
        ]

    def get_random_index(self):
        return random.randint(0, len(self.albums) - 1)

    def generate_youtube_link(self):
        random_index = self.get_random_index()
        album = self.albums[random_index]
        search_query = album + " full album"
        youtube_link = "https://www.youtube.com/results?search_query=" + "+".join(search_query.split())
        webbrowser.open_new_tab(youtube_link)

root = tk.Tk()
app = MusicApp(root)
root.mainloop()