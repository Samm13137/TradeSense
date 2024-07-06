from pyfacebook import GraphAPI

api = GraphAPI(access_token=settings.FACEBOOK_API_KEY)

group_id = 'GROUP_ID'  # Replace with the ID of the stock group you want to scrape

# Get the posts from the stock group
posts = api.get_all_connections(group_id, 'feed')

for post in posts:
    # Extract relevant information from each post
    post_id = post['id']
    message = post.get('message', '')
    created_time = post['created_time']
    
    # Perform any necessary data processing or analysis here
    
    # Print the extracted information
    print(f"Post ID: {post_id}")
    print(f"Message: {message}")
    print(f"Created Time: {created_time}")
    print("-----")
