from django.shortcuts import render, get_object_or_404

from .models import Post, Author, Tag


# Create your views here.
def starting_page(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    """Sort by date to return latest 3 posts."""
    # sorted_post = sorted(all_posts, key=get_date)
    # latest_post = sorted_post[-3:]

    return render(request, "blog/index.html", {"posts": latest_post})


def posts(request):
    """Provides all posts within post list"""
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    """Uses slug to filter and render that posts details using next()
    return post within all posts if post['slug'] == param
    """
    # identified_post = next(post for post in all_posts if post["slug"] == slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        "blog/post-detail.html",
        {"post": identified_post, "post_tags": identified_post.tags.all()},
    )
