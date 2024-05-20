from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "test.jpg",
        "author": "Me",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "there is nothing like the views you get when hiking in the mountains. I was enjoying the View",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, nulla possimus. Soluta corporis mollitia,
          fugit maxime quod beatae. Doloremque amet omnis sunt sed, asperiores aspernatur iusto perspiciatis blanditiis quos. Repellat.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, nulla possimus. Soluta corporis mollitia,
          fugit maxime quod beatae. Doloremque amet omnis sunt sed, asperiores aspernatur iusto perspiciatis blanditiis quos. Repellat.
      """,
    },
    {
        "slug": "Swim",
        "image": "test.jpg",
        "author": "Me",
        "date": date(2021, 8, 22),
        "title": "Swim ",
        "excerpt": "there is nothing like the views you get when hiking in the mountains. I was enjoying the View",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, nulla possimus. Soluta corporis mollitia,
          fugit maxime quod beatae. Doloremque amet omnis sunt sed, asperiores aspernatur iusto perspiciatis blanditiis quos. Repellat.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, nulla possimus. Soluta corporis mollitia,
          fugit maxime quod beatae. Doloremque amet omnis sunt sed, asperiores aspernatur iusto perspiciatis blanditiis quos. Repellat.
      """,
    },
    {
        "slug": "Run",
        "image": "test.jpg",
        "author": "Me",
        "date": date(2021, 6, 26),
        "title": "Run ",
        "excerpt": "there is nothing like the views you get when hiking in the mountains. I was enjoying the View",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, nulla possimus. Soluta corporis mollitia,
          fugit maxime quod beatae. Doloremque amet omnis sunt sed, asperiores aspernatur iusto perspiciatis blanditiis quos. Repellat.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo, nulla possimus. Soluta corporis mollitia,
          fugit maxime quod beatae. Doloremque amet omnis sunt sed, asperiores aspernatur iusto perspiciatis blanditiis quos. Repellat.
      """,
    },
]


def get_date(post):
    """Function printing python version."""
    return post["date"]


# Create your views here.
def starting_page(request):
    """Sort by date to return latest 3 posts."""
    sorted_post = sorted(all_posts, key=get_date)
    latest_post = sorted_post[-3:]

    return render(request, "blog/index.html", {"posts": latest_post})


def posts(request):
    """Provides all posts within post list"""
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    """Uses slug to filter and render that posts details using next()
    return post within all posts if post['slug'] == param
    """
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
