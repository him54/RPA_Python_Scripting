import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.imdb.com/chart/top/")
html = r.text
soup = BeautifulSoup(html, 'html.parser')
t = soup.tbody
print(t.attrs) # attributes   #{'class': ['lister-list']}
tb = soup.find('tbody', {'class':'lister-list'}) 
t2 = tb.findAll('tr')
for t1 in t2:
  movie_name = t1.find('td', {'class':'titleColumn'})
  print(movie_name.a.string, movie_name.span.string)
  
      # (altr)
#<span id = 'alr' class = 'xyz
  #element/tag
#OUTPUT

The Shawshank Redemption (1994)
The Godfather (1972)
The Dark Knight (2008)
The Godfather: Part II (1974)
12 Angry Men (1957)
Schindler's List (1993)
The Lord of the Rings: The Return of the King (2003)
Pulp Fiction (1994)
The Lord of the Rings: The Fellowship of the Ring (2001)
The Good, the Bad and the Ugly (1966)
Forrest Gump (1994)
Fight Club (1999)
The Lord of the Rings: The Two Towers (2002)
Inception (2010)
Star Wars: Episode V - The Empire Strikes Back (1980)
The Matrix (1999)
GoodFellas (1990)
One Flew Over the Cuckoo's Nest (1975)
Se7en (1995)
Seven Samurai (1954)
It's a Wonderful Life (1946)
The Silence of the Lambs (1991)
City of God (2002)
Saving Private Ryan (1998)
Life Is Beautiful (1997)
Interstellar (2014)
The Green Mile (1999)
Star Wars (1977)
Terminator 2: Judgment Day (1991)
Back to the Future (1985)
Spirited Away (2001)
The Pianist (2002)
Psycho (1960)
Parasite (2019)
Léon: The Professional (1994)
The Lion King (1994)
Gladiator (2000)
American History X (1998)
The Departed (2006)
The Usual Suspects (1995)
The Prestige (2006)
Whiplash (2014)
Casablanca (1942)
Harakiri (1962)
Grave of the Fireflies (1988)
The Intouchables (2011)
Modern Times (1936)
Once Upon a Time in the West (1968)
Rear Window (1954)
Cinema Paradiso (1988)
Alien (1979)
City Lights (1931)
Apocalypse Now (1979)
Memento (2000)
Django Unchained (2012)
Raiders of the Lost Ark (1981)
WALL·E (2008)
The Lives of Others (2006)
Sunset Blvd. (1950)
Paths of Glory (1957)
The Shining (1980)
The Great Dictator (1940)
Avengers: Infinity War (2018)
Witness for the Prosecution (1957)
Aliens (1986)
Spider-Man: Into the Spider-Verse (2018)
American Beauty (1999)
Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964)
The Dark Knight Rises (2012)
Oldboy (2003)
Inglourious Basterds (2009)
Amadeus (1984)
Coco (2017)
Joker (2019)
Toy Story (1995)
Braveheart (1995)
The Boat (1981)
Avengers: Endgame (2019)
Princess Mononoke (1997)
Once Upon a Time in America (1984)
Good Will Hunting (1997)
Your Name. (2016)
Requiem for a Dream (2000)
Singin' in the Rain (1952)
3 Idiots (2009)
Toy Story 3 (2010)
High and Low (1963)
Capernaum (2018)
Star Wars: Episode VI - Return of the Jedi (1983)
Eternal Sunshine of the Spotless Mind (2004)
2001: A Space Odyssey (1968)
Reservoir Dogs (1992)
The Hunt (2012)
Come and See (1985)
Top Gun: Maverick (2022)
Citizen Kane (1941)
Lawrence of Arabia (1962)
M (1931)
North by Northwest (1959)
Vertigo (1958)
Amélie (2001)
The Apartment (1960)
Ikiru (1952)
A Clockwork Orange (1971)
Double Indemnity (1944)
Full Metal Jacket (1987)
Hamilton (2020)
Scarface (1983)
To Kill a Mockingbird (1962)
Incendies (2010)
The Sting (1973)
Heat (1995)
Up (2009)
A Separation (2011)
Taxi Driver (1976)
Metropolis (1927)
L.A. Confidential (1997)
Die Hard (1988)
Snatch (2000)
Indiana Jones and the Last Crusade (1989)
Bicycle Thieves (1948)
Like Stars on Earth (2007)
1917 (2019)
Downfall (2004)
For a Few Dollars More (1965)
Dangal (2016)
Batman Begins (2005)
The Kid (1921)
Some Like It Hot (1959)
The Father (2020)
All About Eve (1950)
Green Book (2018)
The Wolf of Wall Street (2013)
Judgment at Nuremberg (1961)
Casino (1995)
Ran (1985)
Pan's Labyrinth (2006)
Unforgiven (1992)
The Truman Show (1998)
There Will Be Blood (2007)
The Sixth Sense (1999)
A Beautiful Mind (2001)
Shutter Island (2010)
Yojimbo (1961)
The Treasure of the Sierra Madre (1948)
Jurassic Park (1993)
Monty Python and the Holy Grail (1975)
Spider-Man: No Way Home (2021)
The Great Escape (1963)
Rashomon (1950)
No Country for Old Men (2007)
Kill Bill: Vol. 1 (2003)
The Thing (1982)
Finding Nemo (2003)
The Elephant Man (1980)
Chinatown (1974)
Raging Bull (1980)
V for Vendetta (2005)
Gone with the Wind (1939)
Lock, Stock and Two Smoking Barrels (1998)
Inside Out (2015)
Dial M for Murder (1954)
The Secret in Their Eyes (2009)
Howl's Moving Castle (2004)
Three Billboards Outside Ebbing, Missouri (2017)
The Bridge on the River Kwai (1957)
Trainspotting (1996)
Prisoners (2013)
Warrior (2011)
Fargo (1996)
Gran Torino (2008)
My Neighbor Totoro (1988)
Catch Me If You Can (2002)
Million Dollar Baby (2004)
Children of Heaven (1997)
Blade Runner (1982)
The Gold Rush (1925)
Before Sunrise (1995)
On the Waterfront (1954)
12 Years a Slave (2013)
Harry Potter and the Deathly Hallows: Part 2 (2011)
Klaus (2019)
Ben-Hur (1959)
Gone Girl (2014)
Wild Strawberries (1957)
The General (1926)
The Grand Budapest Hotel (2014)
The Third Man (1949)
In the Name of the Father (1993)
The Deer Hunter (1978)
Barry Lyndon (1975)
The Wages of Fear (1953)
Hacksaw Ridge (2016)
Mr. Smith Goes to Washington (1939)
Memories of Murder (2003)
Sherlock Jr. (1924)
Wild Tales (2014)
Mad Max: Fury Road (2015)
The Seventh Seal (1957)
Mary and Max (2009)
Room (2015)
How to Train Your Dragon (2010)
Monsters, Inc. (2001)
Jaws (1975)
The Big Lebowski (1998)
Dead Poets Society (1989)
Tokyo Story (1953)
The Passion of Joan of Arc (1928)
Hotel Rwanda (2004)
Ford v Ferrari (2019)
Rocky (1976)
Platoon (1986)
Spotlight (2015)
The Terminator (1984)
Ratatouille (2007)
Stand by Me (1986)
Logan (2017)
Rush (2013)
Network (1976)
Pather Panchali (1955)
Into the Wild (2007)
The Wizard of Oz (1939)
Before Sunset (2004)
Groundhog Day (1993)
The Best Years of Our Lives (1946)
The Exorcist (1973)
To Be or Not to Be (1942)
The Incredibles (2004)
La haine (1995)
The Battle of Algiers (1966)
Hachi: A Dog's Tale (2009)
Jai Bhim (2021)
Pirates of the Caribbean: The Curse of the Black Pearl (2003)
My Father and My Son (2005)
The Grapes of Wrath (1940)
Amores Perros (2000)
Rebecca (1940)
Cool Hand Luke (1967)
The Handmaiden (2016)
The 400 Blows (1959)
The Sound of Music (1965)
It Happened One Night (1934)
Persona (1966)
Life of Brian (1979)
Dersu Uzala (1975)
The Iron Giant (1999)
The Help (2011)
Aladdin (1992)
Gandhi (1982)
Dances with Wolves (1990)
