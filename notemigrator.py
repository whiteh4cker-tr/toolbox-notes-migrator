import praw
import csv
import time

# Reddit API credentials
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="YOUR_USER_AGENT",
    username="YOUR_REDDIT_USERNAME",
    password="YOUR_REDDIT_PASSWORD"
)

# Subreddit name
subreddit_name = "subredditname"

# Function to add mod notes
def add_mod_note(username, text):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.mod.notes.create(label="ABUSE_WARNING", note=text, redditor=username)
        print(f"Mod note added for {username}")
    except Exception as e:
        print(f"Error adding mod note for {username}: {str(e)}")
        # If an error occurs, move on to the next username
        return

# Path to your CSV file
csv_file_path = "notes.csv"

# Initialize variables for rate limiting
requests_count = 0
start_time = time.time()

# Read CSV file and add mod notes
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Check if the rate limit has been reached
        if requests_count >= 1000:
            # Calculate time remaining until the 10-minute window resets
            elapsed_time = time.time() - start_time
            if elapsed_time < 600:
                remaining_time = 600 - elapsed_time
                print(f"Waiting for {remaining_time} seconds to respect rate limit...")
                time.sleep(remaining_time)
                # Reset variables after waiting
                requests_count = 0
                start_time = time.time()
        
        username = row[0]  # Assuming the username is in the first column
        text = ','.join(row[1:])  # Joining all elements after the first one with commas
        add_mod_note(username, text)
        
        # Increment the request count
        requests_count += 1
        time.sleep(2)
