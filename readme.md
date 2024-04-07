# Getting Started

## Creating the Reddit app

In your browser, when you are logged in with the Reddit account you want to use, go to this URL: https://www.reddit.com/prefs/apps

Once there, click the “are you a developer? create an app...” button at the bottom. Name the app anything you want. Then **CLICK THE SCRIPT OPTION**, this is important.

You can leave the description and about URL empty, but you need to put a value for the redirect URI. This can be anything as long as it is a valid URL. I recommend putting `http://127.0.0.1`.

Then click Create App.

You will find your client id and secret. Now we are ready to get the bot up and running!

Open `notemigrator.py` using a text editor and input these credentials. You can input `AI Modbot 0.1` for `user_agent`. Input your reddit bot account's username and password. Finally, edit the subreddit name.

## Creating notes.csv

Change `subreddit` in `https://www.reddit.com/r/subreddit/about/wiki/edit/usernotes/` and go to that page. Select the wiki content with `CTRL + A` and copy it. Create a file called `notes.txt` and paste the content that you copied from your subreddit's wiki. Then run `noteextractor.py`.

## Migrating the notes from notes.csv to new mod notes

Run `notemigrator.py`. Each note will take 2 seconds to migrate.

### Limitations

All new notes will have the `Abuse Warning` label.
