# ADVENTURE BOT
Source code for [@adventure](https://botsin.space/@adventure) on Mastodon.

## How to use it
You need to install a few things first. (sorry, no requirements.txt yet)
1. Follow all instructions to install [textplayer](https://github.com/danielricks/textplayer) (make sure textplayer is installed under the adventure folder
2. Install [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/), `arrow`, and `Mastodon.py`
3. Generate credentials for Mastodon.py (see https://gist.github.com/aparrish/661fca5ce7b4882a8c6823db12d42d26)
4. Copy the client ID, client secret, and access token into `config.py`
5. Set the other options in `config.py`
6. (optional) Add words you'd rather not see to `naughty.py` and have them replaced with "toot". :P

After you've done all those steps, just run `bot.py` in something like tmux or screen, and have fun!
