from mastodon import Mastodon
import config
import naughty

import textplayer.textPlayer as tp
import time
import arrow

from collections import Counter
from bs4 import BeautifulSoup as bs

# Function definitions - you shouldn't have to modify these.
def Most_Common(lst):
    data = Counter(lst)
    return (data.most_common(1)[0][0], (str(int(100 * data.most_common(1)[0][1]/sum(data.values()))) + "%")) # (actual command, percentage of votes this command received)

def sendToot(message, api):
    if len(message) > 500:
        messages = [ message[i:i+475] for i in range(0, len(message), 475) ] # Message too long - split it into 475 (arbitrary) character chunks.
        for i in range(len(messages)):
            info = api.status_post(("(%s/%s) "%(i+1, len(messages)) + messages[i]), visibility='unlisted')
            print('sent message %s with id %s'%(i+1, info['id']))
    else:
        info = api.status_post(message, visibility='unlisted')
        print('sent toot with id %s'%info['id'])

    return info



if __name__ == '__main__':
    client = Mastodon(config.client_id, config.client_secret, config.access_token, api_base_url=config.base_url)
    t = tp.TextPlayer(config.game)
    latest = sendToot(t.run(), client)
    tootTime = arrow.get(latest['created_at'])
    toWait = config.time_gap
    while True:
        time.sleep(15)
        replies = filter((lambda x: x['type'] == 'mention' and (arrow.get(x['created_at']) - tootTime).seconds <= toWait), client.notifications()) # Find mentions sent in the last `toWait` seconds
        options = [naughty.replace(bs(i['status']['content'], 'html.parser').p.text.split('@' + config.name + ' ')[1]) for i in replies] # I'm sorry.
        if len(options) != 0:
            command = Most_Common(options)
            response = t.execute_command(str(command[0]))
            if t.get_score() != None:
                score = t.get_score()[0]

            newToot = '> ' + str(command[0]) + ' (' + command[1] + ')' + '\n' + response + '\n' + 'Score: %s'%score
            latest = sendToot(newToot, client)
            tootTime = arrow.get(latest['created_at'])
            toWait = 15
        else:
            print('No commands received. Waiting...')
            toWait += 15
