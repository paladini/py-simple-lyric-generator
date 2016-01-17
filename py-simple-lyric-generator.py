#!/usr/bin/python3
import requests
import sys
import os
import hashlib
from pymarkovchain import MarkovChain

API_URI = "http://lyrics.wikia.com/api.php?action=lyrics&fmt=realjson"

if __name__ == '__main__':

	if len(sys.argv) != 3:
		raise "Usage: python3 py-simple-lyric-generator \"[artist_name]\" [number_of_phrases_to_generate]"

	artist_name = sys.argv[1]
	number_of_phrases = sys.argv[2]
	params = {
		'artist': artist_name
	}

	# Generating a Markov Chain Model
	db_name_hashed = "db/" + hashlib.md5(artist_name.lower().encode('utf-8')).hexdigest()
	mc = MarkovChain(db_name_hashed)

	# Checking if the database already exists, if so uses the cache instead another API call
	if not os.path.isfile(db_name_hashed):
		print("No data cached. Please be patient while we search the lyrics of %s." % artist_name)		
		
		# Adding lyrics to a single gigant string
		lyrics = ''

		# Parsing each lyric from this artist.
		# [http://api.wikia.com/wiki/LyricWiki_API]
		artist = requests.get(API_URI, params=params).json()
		for album in artist['albums']:
			for song in album['songs']:
				params = {
					'artist': artist_name,
					'song': song
				}
				print("Parsing \"{}\" from Wikia.".format(song))
				response = requests.get(API_URI, params=params).json()["lyrics"]
				lyrics += response.replace('[...]', '') + ' '

		# Generating the database
		mc.generateDatabase(lyrics)
		mc.dumpdb()

	# Printing a string
	for i in range(0, int(number_of_phrases)):
		print(mc.generateString())