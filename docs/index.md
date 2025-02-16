---
title: "Welcome to My Blog"
description: "Explore my latest projects, write-ups, and tech blogs."
---

# 🏠 Welcome to My Blog!

Hello! I'm **superxz3r0**, and this is my blog where I write about **cybersecurity, DevOps, and tech projects**. Here, you'll find my latest **projects, write-ups, and general blogs**.

---

## 📝 Latest Posts  

{% for category in ["Blog", "Write-Up", "Project"] %}
### {{ category }}s

{% for post in categories[category][:3] %}  <!-- Show only the latest 3 posts -->
- **[{{ post.title }}]({{ post.filename }})**  
  📅 {{ post.date }} | 🏷️ {{ post.category }}

{% endfor %}
{% endfor %}

➡️ **[View All Posts](blog/index.md)**  
