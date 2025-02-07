import os

def define_env(env):
    """This function is automatically called by mkdocs-macros"""
    
    blog_path = "docs/blog"
    if not os.path.exists(blog_path):
        return
    
    # Get all blog posts and sort by latest modified date
    posts = [
        f for f in os.listdir(blog_path) if f.endswith(".md")
    ]
    posts.sort(key=lambda f: os.path.getmtime(os.path.join(blog_path, f)), reverse=True)

    # Generate links for the latest 5 blog posts
    latest_posts = [
        f"- [{post.replace('.md', '').replace('-', ' ').title()}](blog/{post})"
        for post in posts[:5]
    ]

    # Save the latest posts list
    env.variables["latest_blog_posts"] = "\n".join(latest_posts)
