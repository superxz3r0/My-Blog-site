# 📜 All Blog Posts

{% for category, posts in categories.items() %}
## {{ category }}s

{% for post in posts %}
### [{{ post.title }}]({{ post.filename }})
📅 {{ post.date }} | 🏷️ {{ post.category }}

{{ post.description }}

---
{% endfor %}

{% endfor %}
