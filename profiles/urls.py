from core.generic_views import http_404_not_found
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path("post-signup", signup_view),
    path("edit-my-profile", edit_my_profile),
    path("get-my-profile", get_my_profile),
    path("get-profile/<str:slug>", get_profile),
    path("get-profile-projects/<str:slug>", get_profile_projects),
    path("get-filtered-profiles/<str:query>", get_filtered_profiles),
    path("get-profile-list", get_profile_list),
    path("get-skills-name-list", get_skills_name_list),
    path("get-notifications", get_notifications),
    path("get-notifications-number", get_notifications_number),
    path("visualize-notifications", visualize_notifications),
    path("create-link", create_link),
    path("delete-link/<int:link_id>", delete_link),
    re_path(r".*", http_404_not_found),
]
