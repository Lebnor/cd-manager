# cd-manager
Create and manage collections of CD's with this interactive python program

# How to run this program
`cd` to the project's root (where main.py is located)
and run `python3 main.py`

# Project Structure

## cd.py
Defines the class and basic methods for a single CD entry that is kept inside the collection.
A cd has the following fields:
* artist: string
* title: string
* year: integer

## collection.py
Stores an array of CD objects. Contains methods to operate on the collection and to represent the collection as text.
Collections get saved in a .txt file in the *collections* folder.

collection fields:
* items: array of CD objects
* name: string

collection methods:
* *remove* - takes a CD object as parameter and removes it from the collection
* *find* - takes artist and title as parameters and returns the CD in the collection that has those artist and title.
Returns None if there is no such CD.
* *edit* - takes a CD object and artist, title, year as parameters. If given CD object is in the collection, sets it's artist, title, year to the given artist, title and year.
* *general_search* - takes a single string as parameter and returns an array of all CD's that have either title, artist or year contain the given string.
* *change_name* - changes the collection's name to the given name.
* *print_all* - prints the contents of the collection in a table-like format.
* *save* - saves the contents of the collection to a .txt file
* *load* - loads the content of a saved collection from a .txt file

## main.py
Entry point of the program. Run this file to execute the program.
To run the file, `cd` to the project's root (where main.py is located)
and run `python3 main.py`
