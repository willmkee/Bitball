import sqlite3
conn = sqlite3.connect('player_database.db')
c = conn.cursor()
# Creates a table for AAVE GHOSTS
c.execute("""CREATE TABLE players (
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


c.execute("INSERT INTO players VALUES ('Gobro Gons',	14,	2,	14,	2,	16,	3,	15,	2,	15,	2,	15,	2,	13,	1)")

c.execute("INSERT INTO players VALUES ('Basiliano Milano',	11,	0,	10,	0,	12,	1,	13,	1,	14,	2,	14,	2, 0, 0)")

c.execute("INSERT INTO players VALUES ('Cora Twill',	10,	0,	13,	1,	12,	1,	13,	1,	10,	0,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES ('Nadezda York',	8,	-1,	8,	-1,	16,	3,	10,	0,	15,	2,	12,	1, 0, 0)")

c.execute("INSERT INTO players VALUES ('Vasanti Cruz',	16,	3,	14,	2,	12,	1,	15,	2,	14,	2,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES ('Hashad Kuhn',	10,	0,	11,	0,	16,	3,	9,	-1,	14,	2,	11,	0,	17,	3)")

c.execute("INSERT INTO players VALUES ('Jon-Paul Jericho',	14,	2,	12,	1,	13,	1,	15,	2,	13,	1,	17,	3, 0, 0)")

c.execute("INSERT INTO players VALUES ('Djimi Koundé',	10,	0,	14,	2,	10,	0,	15,	2,	10,	0,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES ('Mandy Malakar',	9,	-1,	11,	0,	10,	0,	13,	1,	8,	-1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES ('Tel''blort',	8,	-1,	8,	-1,	14,	2,	16,	3,	14,	2,	15,	2, 0, 0)")

c.execute("INSERT INTO players VALUES ('Shalva Pallesen',	12,	1,	8,	-1,	9,	-1,	13,	1,	13,	1,	9,	-1,	15,	2)")

c.execute("INSERT INTO players VALUES ('Garel''blort',	13,	1,	11,	0,	11,	0,	13,	1,	15,	2,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES ('Karl-Armando Pugh',	9,	-1,	16,	3,	10,	0,	8,	-1,	8,	-1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES ('Holland O’Dafferty',	14,	2,	9,	-1,	11,	0,	10,	0,	10,	0,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES ('Mogan Squip',	14,	2,	9,	-1,	16,	3,	16,	3,	12,	1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES ('Helias King',	12,	1,	8,	-1,	12,	1,	18,	4,	11,	0,	8,	-1,	18,	4)")

c.execute("INSERT INTO players VALUES ('Lyman Hollencrantz',	13,	1,	11,	0,	15,	2,	6,	-2,	13,	1,	13,	1,	0, 0)")

c.execute("INSERT INTO players VALUES ('Pradip Santana',	15,	2,	16,	3,	14,	2,	13,	1,	13,	1,	10,	0,	0, 0)")

c.execute("INSERT INTO players VALUES ('Amelia Lacroix',	16,	3,	14,	2,	9,	-1,	11,	0,	7,	-2,	13,	1,	0, 0)")

c.execute("INSERT INTO players VALUES ('Khil Metarot',	10,	0,	15,	2,	12,	1,	10,	0,	17,	3,	14,	2,	0, 0)")

c.execute("INSERT INTO players VALUES ('Neuvo Urriciani',  15, 2,  13, 1,  9, -1,  14, 2,  14, 2,  16, 3,  14, 2)")

c.execute("INSERT INTO players VALUES ('Igor Rendón',  10, 0,  11, 0,  11, 0,  14, 2,  10, 0,  14, 2,  0, 0)")

c.execute("INSERT INTO players VALUES ('Jonatan Towner',  13, 1, 15, 2,  16, 3,  12, 1,  16, 3,  16, 3,  0, 0)")

c.execute("INSERT INTO players VALUES ('Sofia Mertens',  12, 1,  10, 0,  13, 1,  10, 0,  11, 0,  10, 0,  0, 0)")

c.execute("INSERT INTO players VALUES ('Diamond Cabbagestalk',  8, -1,  11, 0,  14, 2,  8, -1,  12, 1,  9, -1,  0, 0)")

c.execute("INSERT INTO players VALUES ('Gwong Klopso',  12, 1,  11, 0,  13, 1,  11, 0,  12, 1,  15, 2,  14, 2)")

c.execute("INSERT INTO players VALUES ('Khil Metarot',  10, 0,  15, 2,  12, 1,  10, 0,  17, 3,  14, 2,  0, 0)")

c.execute("INSERT INTO players VALUES ('Goma Glib',  14, 2,  9, -1,  13, 1,  9, -1,  11, 0,  15, 2,  0, 0)")

c.execute("INSERT INTO players VALUES ('Tekkel''blort',  5, -3,  13, 1,  13, 1,  14, 2,  17, 3,  12, 1,  0, 0)")

c.execute("INSERT INTO players VALUES ('Ralston Crux',  16, 3,  12, 1,  8, -1,  7, -2,  7, -2,  15, 2,  0, 0)")

c.execute("INSERT INTO players VALUES ('Bandy Moscato',  17, 3,  11, 0,  13, 1,  15, 2,  6, -2,  9, -1,  0, 0)")

c.execute("INSERT INTO players VALUES ('Daisuke Sato',  7, -2,  13, 1,  8, -1,  13, 1,  13, 1,  14, 2,  13, 1)")

c.execute("INSERT INTO players VALUES ('Paro''blort',  10, 0,  16, 3,  13, 1,  6, -2,  14, 2,  7, -2,  0, 0)")

c.execute("INSERT INTO players VALUES ('Tad Garbaj',  12, 1,  10, 0,  12, 1,  13, 1,  12, 1,  8, -1,  0, 0)")

c.execute("INSERT INTO players VALUES ('Thankful Tenniford',  16, 3,  15, 2,  14, 2,  10, 0,  17, 3,  7, -2,  0, 0)")

c.execute("INSERT INTO players VALUES ('Horus Shelp',  9, -1,  8, -1,  11, 0,  15, 2,  13, 1,  4, -3,  0, 0)")



conn.commit()
conn.close()
