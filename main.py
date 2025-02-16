import os
import yaml

BLOG_DIR = "docs/blog"

def get_blog_posts():
    categories = {"Blog": [], "Write-Up": [], "Project": []}
    posts = []

    for filename in os.listdir(BLOG_DIR):
        if filename.endswith(".md") and filename != "index.md":
            filepath = os.path.join(BLOG_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if lines and lines[0].strip() == "---":
                    front_matter = []
                    i = 1
                    while i < len(lines) and lines[i].strip() != "---":
                        front_matter.append(lines[i])
                        i += 1
                    metadata = yaml.safe_load("\n".join(front_matter))
                    post_data = {
                        "title": metadata.get("title", filename.replace(".md", "")),
                        "date": metadata.get("date", "Unknown Date"),
                        "category": metadata.get("category", "Blog"),
                        "filename": f"blog/{filename}",
                        "description": metadata.get("description", "No description available."),
                    }
                    posts.append(post_data)
                    categories[post_data["category"]].append(post_data)

    return categories, posts

def define_env(env):
    categories, posts = get_blog_posts()
    env.variables["categories"] = categories
    env.variables["blog_posts"] = posts
