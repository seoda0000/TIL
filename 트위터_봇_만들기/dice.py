
import logging
logger = logging.Logger
import tweepy
import random


def main():

    # ============================
    #          계정 설정
    # ============================

    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    bearer_token = ""

    client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token,
                           access_token_secret=access_token_secret, bearer_token=bearer_token)
    # response = client.create_tweet(text='hello world')
    # print(client.get_me().data.id)
    id = ''

    last_mention = 0


    while True:
        mentions = client.get_users_mentions(id=id, since_id = last_mention).data
        print(mentions)
        if mentions:
            for mention in mentions:
                tweet_id = mention.id
                tweet_txt = mention.text
                answer = 0
                answer_txt = ''

                for t in range(len(tweet_txt)):
                    if tweet_txt[t:t + 3] == '1d6' or tweet_txt[t:t + 3] == '1D6':
                        num = random.randrange(1, 7)
                        answer += num
                        if answer_txt:
                            answer_txt += '+' + str(num)
                        else:
                            answer_txt += str(num)
                    elif tweet_txt[t:t + 3] == '1d8' or tweet_txt[t:t + 3] == '1D8':
                        num = random.randrange(1, 9)
                        answer += num
                        if answer_txt:
                            answer_txt += '+' + str(num)
                        else:
                            answer_txt += str(num)
                    elif tweet_txt[t:t + 3] == '1d1' or tweet_txt[t:t + 3] == '1D1':
                        num = random.randrange(1, 11)
                        answer += num
                        if answer_txt:
                            answer_txt += '+' + str(num)
                        else:
                            answer_txt += str(num)
                if '+' in answer_txt:
                    answer_txt += '='
                else:
                    answer_txt = ''

                last_mention = tweet_id
        else:
            pass



if __name__ == "__main__":
    main()
