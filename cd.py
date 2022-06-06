class CD:
    def __init__(self, artist, title, year):
        self.artist = artist
        self.title = title
        self.year = year
    
    def __str__(self):
        return f"{self.artist} - {self.title} - {self.year}"
    
    def __repr__(self):
        return f"{self.artist} - {self.title} - {self.year}"
    
    def __eq__(self, other):
        return self.artist == other.artist and self.title == other.title and self.year == other.year

    