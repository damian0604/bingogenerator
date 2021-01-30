#!/usr/bin/env python3
import argparse
from random import sample

class Bingo():
    def __init__(self, inputfile):
        with open(inputfile) as f:
            self.values = set([e.strip() for e in f.readlines()])
    

    def generate(self, templatefile, afmeting):
        selection = sample(self.values, afmeting**2)
        with open(templatefile) as f:
            return f.read().format(*selection)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Maak bingokaarten op basis van een lijst met mogelijke opties. Vooral nuttig voor corona-perco's!")
    parser.add_argument('spelers', type=int, default=1,help="Hoe veel kaarten heb je nodig?")
    parser.add_argument('afmeting', type=int, default=4, help="Hoe groot moet je bingokaart zijn? Voor een 4x4 kaart geef je 4 aan.")
    parser.add_argument('inputbestand', help = "Hoe heet het bestand waarmee je de bingokaarten wilt vullen?")
    args = parser.parse_args()

    if args.afmeting != 4:
        raise NotImplementedError("Op dit moment ondersteunen we alleen 4x4 kaarten")
    
    mybingo = Bingo(args.inputbestand)
    for i in range(args.spelers):
        with open(f"{i}.html", mode = 'w') as fo:
            fo.write(mybingo.generate('template.html', args.afmeting))
        print(f"Bingokaart nummer {i} opgeslagen als {i}.html")
        
