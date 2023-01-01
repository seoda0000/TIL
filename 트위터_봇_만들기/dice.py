# -*-coding:utf-8 -*-
import logging

logger = logging.Logger
import tweepy
import random
import time


def main():
    # ============================
    #          계정 설정
    # ============================

    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    bearer_token = ''

    client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token,
                           access_token_secret=access_token_secret, bearer_token=bearer_token)
    # print(client.get_me().data.id)
    id = ''

    last_mention = 0


    bonus = ['', ' ', '!', '.', '::', '!!', ]

    yesno = ['Y', 'N', 'y', 'n', '예', '아니오', 'yes', 'no', 'YES', 'NO', 'Yes', 'No', '요원님 뜻대로 하십시오.']
    # 오늘의 운세 리스트
    fortune = ['운세1',
               '운세2',
               '운세3',
               '운세4',
               '운세5',
               '운세6',
               '운세7',
               '운세8',
               '운세9',
               '운세10',
               ]

    while True:
        mentions = client.get_users_mentions(id=id, since_id=last_mention, user_auth=True, max_results=20).data
        if mentions:
            print(mentions)
            for mention in mentions[::-1]:
                tweet_id = mention.id
                tweet_txt = mention.text
                answer = 0
                answer_txt = ''
                if '오늘의 운세' in tweet_txt:
                    text = fortune[random.randrange(0, len(fortune))]
                    text += bonus[random.randrange(0, 6)]
                    # client.create_tweet(text=text, in_reply_to_tweet_id=tweet_id)
                    last_mention = tweet_id
                    continue

                if 'Y/N' in tweet_txt or 'y/n' in tweet_txt:
                    text = yesno[random.randrange(0, 13)]
                    text += bonus[random.randrange(0, 6)]
                    # client.create_tweet(text=text, in_reply_to_tweet_id=tweet_id)
                    last_mention = tweet_id
                    continue

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
                        if t + 4 < len(tweet_txt) and tweet_txt[t + 4] == '0':
                            num = random.randrange(1, 101)
                        else:
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
                if answer:
                    if answer_txt:
                        text = answer_txt + str(answer)
                    else:
                        text = str(answer) + bonus[random.randrange(0, 6)]
                    # client.create_tweet(text=text, in_reply_to_tweet_id=tweet_id)

                last_mention = tweet_id
                print(last_mention)
            time.sleep(5)
        else:
            time.sleep(10)
            print(time.localtime(time.time()))


if __name__ == "__main__":
    main()
