# py-simple-lyric-generator
A simple Markov chains lyric generator written in Python.

This small project generate new lyrics based on the lyrics of a given artist. For example, you can ask the script to generate Pink Floyd-like lyrics, so it will read all the lyrics from Pink Floyd and generate a new one with the same style. 

I've made a small "database" too, so whenever you load all lyrics from a given artist it will be saved on your computer under the *db* folder. This way we can avoid a lot of API calls (that are quite expensive).

### Dependencies
- [PyMarkovChain](https://github.com/TehMillhouse/PyMarkovChain) (install it using `pip3 install PyMarkovChain`)
- [requests](http://www.python-requests.org/en/latest/) (install it using `pip3 install requests`)
- [Wikya Lyrics API](http://api.wikia.com/wiki/LyricWiki_API) (you don't need to install/configure it)
- Python 3

### Usage
The program expects the following arguments:
```bash
python3 py-simple-lyric-generator.py "<name of the artist>" <number_of_phrases_to_generate>
```

For example, if you want to generate 10 sentences based on Pink Floyd lyrics you should run:
```bash
python3 py-simple-lyric-generator.py "Pink Floyd" 10
```

Then you'll get somewhat like that:
```
I'd be gone
Cause I'm the man on the outside looking in
Playing to rules
Lotuses lean on each other in yearning
The Schoolmaster
And all that you see
And if you don't mind
It's awfully considerate of you to leave, Lucy
Wheeling, soaring, gliding b Instrumental He made his way to the see-saw It's awfully considerate of you to think of me here
Don't accept that what's hap One sound, one single kiss
```

If you want to reset cached artists from the database, just run the following:
```sh
chmod +x clean_db.sh
./clean_db.sh
```

### How it works?
This's my first experiment within lyrics generation with Markov chains, but I've read some texts and a lot of examples. In order to understand how can I generate lyrics, please check the following links:

- [Lyricize: A Flask App to Create Lyrics Using Markov Chains](https://realpython.com/blog/python/lyricize-a-flask-app-to-create-lyrics-using-markov-chains/) [very useful]
- [Text generation with Markov chains](https://lauris.github.io/text-generation-markov-chain)
- [Generating pseudo random text with Markov chains using Python](http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/)

And here you can check some projects on Github that helped me:
- [Lyrics Can Be Easy](https://github.com/zeyus/lyrics-can-be-easy)
- [taytay](https://github.com/caktus/taytay) [Taylor-Swift-like lyric generator, I really want to read their code, they have awesome results]
- [PyMarkovChain](https://github.com/TehMillhouse/PyMarkovChain)

### About
The `py-simple-lyric-generator` was created by Fernando Paladini on 01-17-2016, but it was heavily based on another open-source projects you can find at the web. If you have any issue, doubt, problem or suggestion, please feel free to create a [new Issue](https://github.com/paladini/py-simple-lyric-generator/issues) or even contact me at fnpaladini at gmail dot com. 

