"""Staff dashboard URL Configuration.

Included directly under /staff. Currently, the index view redirects
manually to the dashboard view.
"""


# Django imports
from django.urls import path, include

# Local imports
from . import views
from . import autocomplete


app_name = "staff"
# Custom URL patterns
story_urlpatterns = ([
    path("", views.StoryListView.as_view(), name="view"),
    path("create/", views.StoryCreateView.as_view(), name="create"),
    path("edit/<int:story_id>/", views.stories_edit, name="edit"),
], "stories")

autocomplete_urlpatterns = ([
    path("users/", autocomplete.UserAutoComplete.as_view(), name="users"),
], "autocomplete")

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("stories/", include(story_urlpatterns, "stories")),
    path("media/create/", views.dummy),
    path("media/create/image/", views.ImageCreateView.as_view(), name="create_image"),
    path("media/edit/<int:pk>/", views.ImageCreateView.as_view(), name="edit_media"),
    path("media/delete/<int:pk>/", views.ImageCreateView.as_view(), name="delete_media"),
    path("autocomplete/", include(autocomplete_urlpatterns, "autocomplete"))
]
