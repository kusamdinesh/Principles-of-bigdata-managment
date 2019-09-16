import codecs
import json
import sys


def parse_tweet(line):
    tweet = json.loads(line)
    urls = [url['expanded_url'] for url in tweet['entities']['urls']]
    return [urls]


if __name__ == "__main__":
    file_timeordered_json_tweets = codecs.open("twiterdata.csv", 'r')
    fout = codecs.open("twiturls.txt", 'w')

for line in file_timeordered_json_tweets:
    try:

        [urls] = parse_tweet(line)
        if len(urls) > 0:
            fout.write(str([urls]) + "\n")
        print("extracting urls")
    except:
        pass
file_timeordered_json_tweets.close()
fout.close()