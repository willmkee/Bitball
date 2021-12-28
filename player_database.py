import sqlite3
conn = sqlite3.connect('player_database.db')
c = conn.cursor()
# Creates a table for AAVE GHOSTS
c.execute("""CREATE TABLE players (
  refnum integer,
  team text,
  name text,
  str integer,
  str_mod integer,
  dex integer,
  dex_mod integer,
  wis integer,
  wis_mod integer,
  cha integer,
  cha_mod integer,
  mag integer,
  mag_mod integer,
  dmag integer,
  dmag_mod integer,
  gk integer,
  gk_mod integer
  )""")


c.execute("INSERT INTO players VALUES (1,'Aave Ghosts', 'Gobro Gons',	14,	2,	14,	2,	16,	3,	15,	2,	15,	2,	15,	2,	13,	1)")

c.execute("INSERT INTO players VALUES (2,'Aave Ghosts','Basiliano Milano',	11,	0,	10,	0,	12,	1,	13,	1,	14,	2,	14,	2, 0, 0)")

c.execute("INSERT INTO players VALUES (3,'Aave Ghosts','Cora Twill',	10,	0,	13,	1,	12,	1,	13,	1,	10,	0,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (4,'Aave Ghosts','Nadezda York',	8,	-1,	8,	-1,	16,	3,	10,	0,	15,	2,	12,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (5,'Aave Ghosts','Vasanti Cruz',	16,	3,	14,	2,	12,	1,	15,	2,	14,	2,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (1,'Alchemix Conjurers','Hashad Kahn',	10,	0,	11,	0,	16,	3,	9,	-1,	14,	2,	11,	0,	17,	3)")

c.execute("INSERT INTO players VALUES (2,'Alchemix Conjurers','Jon-Paul Jericho',	14,	2,	12,	1,	13,	1,	15,	2,	13,	1,	17,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (3,'Alchemix Conjurers','Djimi Koundé',	10,	0,	14,	2,	10,	0,	15,	2,	10,	0,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (4,'Alchemix Conjurers','Mandy Malakar',	9,	-1,	11,	0,	10,	0,	13,	1,	8,	-1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (5,'Alchemix Conjurers','Tel''blort',	8,	-1,	8,	-1,	14,	2,	16,	3,	14,	2,	15,	2, 0, 0)")

c.execute("INSERT INTO players VALUES (1,'Abracadabra Wizards','Shalva Pallesen',	12,	1,	8,	-1,	9,	-1,	13,	1,	13,	1,	9,	-1,	15,	2)")

c.execute("INSERT INTO players VALUES (2,'Abracadabra Wizards','Garel''blort',	13,	1,	11,	0,	11,	0,	13,	1,	15,	2,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (3,'Abracadabra Wizards','Karl-Armando Pugh',	9,	-1,	16,	3,	10,	0,	8,	-1,	8,	-1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (4,'Abracadabra Wizards','Holland O’Dafferty',	14,	2,	9,	-1,	11,	0,	10,	0,	10,	0,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (5,'Abracadabra Wizards','Mogan Squip',	14,	2,	9,	-1,	16,	3,	16,	3,	12,	1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (1,'Olympus Omegas','Helias King',	12,	1,	8,	-1,	12,	1,	18,	4,	11,	0,	8,	-1,	18,	4)")

c.execute("INSERT INTO players VALUES (2,'Olympus Omegas','Lyman Hollencrantz',	13,	1,	11,	0,	15,	2,	6,	-2,	13,	1,	13,	1,	0, 0)")

c.execute("INSERT INTO players VALUES (3,'Olympus Omegas','Pradip Santana',	15,	2,	16,	3,	14,	2,	13,	1,	13,	1,	10,	0,	0, 0)")

c.execute("INSERT INTO players VALUES (4,'Olympus Omegas','Amelia Lacroix',	16,	3,	14,	2,	9,	-1,	11,	0,	7,	-2,	13,	1,	0, 0)")

c.execute("INSERT INTO players VALUES (5,'Olympus Omegas','Khil Metarot',	10,	0,	15,	2,	12,	1,	10,	0,	17,	3,	14,	2,	0, 0)")

c.execute("INSERT INTO players VALUES (1,'Uniswap Unicorns','Neuvo Urriciani',  15, 2,  13, 1,  9, -1,  14, 2,  14, 2,  16, 3,  14, 2)")

c.execute("INSERT INTO players VALUES (2,'Uniswap Unicorns','Igor Rendón',  10, 0,  11, 0,  11, 0,  14, 2,  10, 0,  14, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Uniswap Unicorns','Jonatan Towner',  13, 1, 15, 2,  16, 3,  12, 1,  16, 3,  16, 3,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Uniswap Unicorns','Sofia Mertens',  12, 1,  10, 0,  13, 1,  10, 0,  11, 0,  10, 0,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Uniswap Unicorns','Diamond Cabbagestalk',  8, -1,  11, 0,  14, 2,  8, -1,  12, 1,  9, -1,  0, 0)")

c.execute("INSERT INTO players VALUES (1,'Convex Curves','Gwong Klopso',  12, 1,  11, 0,  13, 1,  11, 0,  12, 1,  15, 2,  14, 2)")

c.execute("INSERT INTO players VALUES (2,'Convex Curves','Goma Glib',  14, 2,  9, -1,  13, 1,  9, -1,  11, 0,  15, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Convex Curves','Tekkel''blort',  5, -3,  13, 1,  13, 1,  14, 2,  17, 3,  12, 1,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Convex Curves','Ralston Crux',  16, 3,  12, 1,  8, -1,  7, -2,  7, -2,  15, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Convex Curves','Bandy Moscato',  17, 3,  11, 0,  13, 1,  15, 2,  6, -2,  9, -1,  0, 0)")

c.execute("INSERT INTO players VALUES (1,'Compound Dragons','Daisuke Sato',  7, -2,  13, 1,  8, -1,  13, 1,  13, 1,  14, 2,  13, 1)")

c.execute("INSERT INTO players VALUES (2,'Compound Dragons','Paro''blort',  10, 0,  16, 3,  13, 1,  6, -2,  14, 2,  7, -2,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Compound Dragons','Tad Garbaj',  12, 1,  10, 0,  12, 1,  13, 1,  12, 1,  8, -1,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Compound Dragons','Thankful Tenniford',  16, 3,  15, 2,  14, 2,  10, 0,  17, 3,  7, -2,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Compound Dragons','Horus Shelp',  9, -1,  8, -1,  11, 0,  15, 2,  13, 1,  4, -3,  0, 0)")

c.execute("INSERT INTO players VALUES (1,'Chainlink Frogs','Tamara Edison',  13, 1,  10, 0,  15, 2,  10, 0,  13, 1,  16, 3,  13, 1)")

c.execute("INSERT INTO players VALUES (2,'Chainlink Frogs','Borjo Blozok',  10, 0,  14, 2,  12, 1,  15, 2,  15, 2,  11, 0,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Chainlink Frogs','Gauchinho',  11, 0,  12, 1,  14, 2,  14, 2,  15, 2,  15, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Chainlink Frogs','Sylvia Trask',  10, 0,  17, 3,  13, 1,  15, 2,  13, 1,  12, 1,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Chainlink Frogs','Talia Jeffers',  13, 1,  11, 0,  14, 2,  13, 1,  13, 1,  14, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (1,'Rari Whales','Sharn''blort',  9, -1,  10, 0,  14, 2,  8, -1,  11, 0,  16, 3,  12, 1)")

c.execute("INSERT INTO players VALUES (2,'Rari Whales','Ptolemy Crass',  10, 0,  15, 2,  12, 1,  15, 2,  15, 2,  14, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Rari Whales','Cristiana',  17, 3,  15, 2,  10, 0,  15, 2,  12, 1,  16, 3,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Rari Whales','Martin Murray',  17, 3,  14, 2,  16, 3,  12, 2,  14, 1,  6, -2,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Rari Whales','Tanner Dulce',  11, 0,  15, 2,  13, 1,  10, 0,  12, 1,  9, -1,  0, 0)")

c.execute("INSERT INTO players VALUES (1,'Fractional NFT','Secundus Senior',  8, -1,  16, 3,  8, -1,  12, 1,  13, 1, 11, 0,  18, 4)")

c.execute("INSERT INTO players VALUES (2,'Fractional NFT','Shiva Moss',  15, 2,  13, 1,  12, 1, 17, 3,  13, 1,  13, 1,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Fractional NFT','Dooley Tarver',  14, 2,  16, 3,  13, 1,  14, 2,  13, 1,  14, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Fractional NFT','Roger',  13, 1,  10, 0,  14, 2, 9, -1, 15, 2,  15, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Fractional NFT','Gando''blort',  15, 2,  13, 1,  15, 2,  16, 3,  11, 0,  15, 2,  0, 0)")

conn.commit()
conn.close()
