import praw
import pickle

reddit = praw.Reddit(client_id='gl4t8_yiP3E-Cg',
                     client_secret='8SYfS0zwBn6XccqZCVvyPWwEkDTomQ',
                     username='AdditionalQuit5294',
                     password='J12W09yg',
                     user_agent='test_script')

# Choose subreddit
subs = ['KotakuInAction', 'MensRights', 'Incels', 
        'FemaleDatingStrategy', 'politics', 'TumblrInAction',
       'TrollXChromosomes'] 

subR = 'KotakuInAction'

reddit = praw.Reddit(client_id='gl4t8_yiP3E-Cg',
                     client_secret='8SYfS0zwBn6XccqZCVvyPWwEkDTomQ',
                     username='AdditionalQuit5294',
                     password='J12W09yg',
                     user_agent='test_script')

# Choose tab in subreddit (hot, rising, controversial, top, etc.)
subreddit = reddit.subreddit(subR).top(limit=300)

all_comments = []

# Go through data and get comments
for submission in subreddit:
    if not submission.stickied:
        all_comments.append(submission.title)

        comments = submission.comments.list()
        for comment in comments:

            try:
                all_comments.append(comment.body)
            except AttributeError:
                pass

# View number of comments scraped
print(len(all_comments))

# Pickle data, filename = subreddit + # of comments scraped
with open(f'{subR}_{len(all_comments)}.pkl', 'wb') as f:
    pickle.dump(all_comments, f)