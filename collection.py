import os
from cd import CD


class Collection:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, artist, title, year):
        self.items.append(CD(artist, title, year))

    def remove(self, item):
        for i in self.items:
            if i == item:
                self.items.remove(i)
                return True
        return False

    def find(self, artist, title):
        for item in self.items:
            if item.artist == artist and item.title == title:
                return item
        return None

    def edit(self, item, artist, title, year):
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i].artist = artist
                self.items[i].title = title
                self.items[i].year = year
                return True
        return False
    
    def general_search(self, search_term):
        results = []
        for item in self.items:
            if search_term in item.artist or search_term in item.title or search_term in item.year:
                results.append(item)
        return results

    def change_name(self, name):
        self.name = name

    def print_all(self):
        if len(self.items) == 0:
            print("No items in the collection")
        else:
            index = 1
            for item in self.items:
                print(f"{index}.", item)
                index += 1

    def save(self):
        with open(f"{self.name}.txt", "w") as f:
            for item in self.items:
                f.write(f"{item.artist}\t{item.title}\t{item.year}\n")

    def load(self):
        if (os.path.exists(f"{self.name}.txt")):
            with open(f"{self.name}.txt", "r") as f:
                for line in f:
                    artist, title, year = line.strip().split("\t")
                    self.items.append(CD(artist, title, year))

    def __str__(self):
        return f"{self.name} ({len(self.items)} items)"
    
    def __repr__(self):
        return f"{self.name} ({len(self.items)} items)"

