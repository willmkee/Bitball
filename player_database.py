import sqlite3
conn = sqlite3.connect('player.sqlite')
c = conn.cursor()
# Creates a table for AAVE GHOSTS
# c.execute("""CREATE TABLE aave_ghosts (
#   name text,
#   str integer,
#   str_mod integer,
#   dex integer,
#   dex_mod integer,
#   wis integer,
#   wis_mod integer,
#   cha integer,
#   cha_mod integer,
#   mag integer,
#   mag_mod integer,
#   dmag integer,
#   dmag_mod integer,
#   gk integer,
#   gk_mod integer,
#   )""")

# Creates a table for alchemix_conjurers
# c.execute("""CREATE TABLE alchemix_conjurers (
#   name text,
#   str integer,
#   str_mod integer,
#   dex integer,
#   dex_mod integer,
#   wis integer,
#   wis_mod integer,
#   cha integer,
#   cha_mod integer,
#   mag integer,
#   mag_mod integer,
#   dmag integer,
#   dmag_mod integer,
#   gk integer,
#   gk_mod integer,
#   )""")


# creates a table for Abracadabra Wizards
# c.execute("""CREATE TABLE abracadabra_wizards (
#   name text,
#   str integer,
#   str_mod integer,
#   dex integer,
#   dex_mod integer,
#   wis integer,
#   wis_mod integer,
#   cha integer,
#   cha_mod integer,
#   mag integer,
#   mag_mod integer,
#   dmag integer,
#   dmag_mod integer,
#   gk integer,
#   gk_mod integer,
#   )""")

# Creates a table for Olympus_Omegas
# c.execute("""CREATE TABLE olympus_omegas (
#   name text,
#   str integer,
#   str_mod integer,
#   dex integer,
#   dex_mod integer,
#   wis integer,
#   wis_mod integer,
#   cha integer,
#   cha_mod integer,
#   mag integer,
#   mag_mod integer,
#   dmag integer,
#   dmag_mod integer,
#   gk integer,
#   gk_mod integer
#   )""")

# c.execute("INSERT INTO aave_ghosts VALUES ('Gobro Gons',	14,	2,	14,	2,	16,	3,	15,	2,	15,	2,	15,	2,	13,	1)")

# c.execute("INSERT INTO aave_ghosts VALUES ('Basiliano Milano',	11,	0,	10,	0,	12,	1,	13,	1,	14,	2,	14,	2, 0, 0)")

# c.execute(
#     "INSERT INTO aave_ghosts VALUES ('Cora Twill',	10,	0,	13,	1,	12,	1,	13,	1,	10,	0,	16,	3, 0, 0)")

# c.execute(
#     "INSERT INTO aave_ghosts VALUES ('Nadezda York',	8,	-1,	8,	-1,	16,	3,	10,	0,	15,	2,	12,	1, 0, 0)")

# c.execute(
#     "INSERT INTO aave_ghosts VALUES ('Vasanti Cruz',	16,	3,	14,	2,	12,	1,	15,	2,	14,	2,	16,	3, 0, 0)")

# c.execute("INSERT INTO alchemix_conjurers VALUES ('Hashad Kuhn',	10,	0,	11,	0,	16,	3,	9,	-1,	14,	2,	11,	0,	17,	3)")

# c.execute("INSERT INTO alchemix_conjurers VALUES ('BJon-Paul Jericho',	14,	2,	12,	1,	13,	1,	15,	2,	13,	1,	17,	3, 0, 0)")

# c.execute(
#     "INSERT INTO alchemix_conjurers VALUES ('Djimi Koundé',	10,	0,	14,	2,	10,	0,	15,	2,	10,	0,	16,	3, 0, 0)")

# c.execute(
#     "INSERT INTO alchemix_conjurers VALUES ('Mandy Malakar',	9,	-1,	11,	0,	10,	0,	13,	1,	8,	-1,	13,	1, 0, 0)")

# c.execute(
#     "INSERT INTO alchemix_conjurers VALUES ('Tel''blort',	8,	-1,	8,	-1,	14,	2,	16,	3,	14,	2,	15,	2, 0, 0)")

# c.execute("INSERT INTO abracadabra_wizards VALUES ('Shalva Pallesen',	12,	1,	8,	-1,	9,	-1,	13,	1,	13,	1,	9,	-1,	15,	2)")

# c.execute("INSERT INTO alchemix_conjurers VALUES ('Garel''blort',	13,	1,	11,	0,	11,	0,	13,	1,	15,	2,	16,	3, 0, 0)")

# c.execute(
#     "INSERT INTO alchemix_conjurers VALUES ('DKarl-Armando Pugh',	9,	-1,	16,	3,	10,	0,	8,	-1,	8,	-1,	13,	1, 0, 0)")

# c.execute(
#     "INSERT INTO alchemix_conjurers VALUES ('Holland O’Dafferty',	14,	2,	9,	-1,	11,	0,	10,	0,	10,	0,	13,	1, 0, 0)")

# c.execute(
#     "INSERT INTO alchemix_conjurers VALUES ('Mogan Squip',	14,	2,	9,	-1,	16,	3,	16,	3,	12,	1,	13,	1, 0, 0)")

# c.execute("INSERT INTO olympus_omegas VALUES ('Helias King',	12,	1,	8,	-1,	12,	1,	18,	4,	11,	0,	8,	-1,	18,	4)")

# c.execute("INSERT INTO olympus_omegas VALUES ('Lyman Hollencrantz',	13,	1,	11,	0,	15,	2,	6,	-2,	13,	1,	13,	1,	0, 0)")

# c.execute("INSERT INTO olympus_omegas VALUES ('Pradip Santana',	15,	2,	16,	3,	14,	2,	13,	1,	13,	1,	10,	0,	0, 0)")

# c.execute("INSERT INTO olympus_omegas VALUES ('Amelia Lacroix',	16,	3,	14,	2,	9,	-1,	11,	0,	7,	-2,	13,	1,	0, 0)")

# c.execute("INSERT INTO olympus_omegas VALUES ('Khil Metarot',	10,	0,	15,	2,	12,	1,	10,	0,	17,	3,	14,	2,	0, 0)")


conn.commit()

conn.close()
