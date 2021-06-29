#! python3
# test inserting new usernames into database

import utils.CreateNickname as CreateNickname
import sql.sql_funcs as sql_funcs

TEST_USERNAMES = ['gusterfell',
 'NedRyersonsHat',
 'GeoDuuuude',
 'joeyblove',
 'johnnyflashytits',
 'h2oape',
 'unoriginal1187',
 'captncoop88',
 'TattooJerry',
 'kestrel1000c',
 'TheAssassin777',
 'DerAmeisenbaer',
 'afkush',
 'bikeidaho',
 'fasda',
 'UndeadMarine55',
 'zombieslayer9389',
 'AeonFluxIncapacitaor',
 'progamercabrera',
 'Notafuzzycat',
 'Gorditotimebabyyyy']

for username in TEST_USERNAMES:
    sql_funcs.insert_username(username)

need_nicknames = sql_funcs.need_nicknames()
print(len(need_nicknames)) # output should be 20

for user in need_nicknames:
    nickname = CreateNickname.create_nickname()
    sql_funcs.insert_nickname(user,nickname)