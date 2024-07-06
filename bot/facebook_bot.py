from pyfacebook import GraphAPI
import bot.settings as settings

#start of facebook bot

api = GraphAPI(access_token=settings.FACEBOOK_API_KEY)

# Need to pick out which group to scrape
group_id = 322661495555943  # Replace with the ID of the stock group you want to scrape

# Get the posts from the stock group, might limit this to not over saturate?
posts = api.get_all_connections(group_id, 'feed')

for post in posts:
    # Extract relevant information from each post
    post_id = post['id']
    message = post.get('message', '')
    created_time = post['created_time']
    
    # Perform any necessary data processing or analysis here, maybe something determining what's postivive and negative?
    
    # Print the extracted information for now, but need to replace this with actual analysis
    print(f"Post ID: {post_id}")
    print(f"Message: {message}")
    print(f"Created Time: {created_time}")
    print("-----")
