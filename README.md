URL Endpoints
-------------------
auth/login/   Login
auth/logout/   Logout
auth/register/   Register and login

user/follow/   follow people
user/profile/<usernmae>/   see profile
user/profile/<usernmae>/update/   update profile

post/create_post/     create a post
post/<pk>/     get the post with pk
post/story/<pk>/   get story with pk
post/feed/  get the user feed

activity/like/<post_id>/   like a post
activity/comment/create/  send comment, The comment will add mention automate with signals
activity/comment/delete/pk/ get the comment detail

direct/send_message/  send direct message
direct/get_message/<pk>/   get message detail
