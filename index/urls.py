from django.urls import path,re_path

from . import views

import login.views as login
import register.views as register
import cate.views as cate
import book.views as book
import article.views as article
import weibo.views as weibo
import sitemap.views as sitemap
import search.views as search



urlpatterns = [
    path("", views.index , name='index'),
    path("about.html", views.info , kwargs={"tag": "about"} , name = 'about'),
    path("contact.html", views.info , kwargs={"tag": "contact"}, name = 'contact'),
    path("terms.html", views.info , kwargs={"tag": "terms"}, name = 'terms'),
    path("publish.html", views.info , kwargs={"tag": "publish"}, name = 'publish'),
    path("disclaimer.html", views.info , kwargs={"tag": "disclaimer"}, name = 'disclaimer'),

    path("login.html", login.login ,  name = 'login'),
    path("logindoweb.html", login.logindoweb ,  name = 'logindoweb'),
    path("loginreturn/<str:type>.html", login.loginreturn ,  name = 'loginreturn'),
    path("logindo/<str:type>.html", login.logindo ,  name = 'logindo'),
    path("logout.html", login.logout ,  name = 'logout'),

    path("register.html", register.register ,  name = 'register'),
    path("registerdo/<int:type>.html", register.registerdo ,  name = 'registerdo'),

    
    path("book.html", book.index , name = 'book'),
    path("book/list_<int:page>.html", book.index ,name = 'book_list'),

    path("meiwen.html", article.index ,kwargs={"type": 2}, name = 'meiwen'),
    path("meiwen/list_<int:page>.html", article.index ,kwargs={"type": 2}, name = 'meiwen_list'),

    path("gushi.html", article.index ,kwargs={"type": 3}, name = 'gushi'),
    path("gushi/list_<int:page>.html", article.index ,kwargs={"type": 3}, name = 'gushi_list'),

    path("zuowen.html", article.index ,kwargs={"type": 4}, name = 'zuowen'),
    path("zuowen/list_<int:page>.html", article.index ,kwargs={"type": 4}, name = 'zuowen_list'),

    path("weibo.html", weibo.index , name = 'weibo'),
    path("weibo/list_<int:page>.html", weibo.index , name = 'weibo_list'),
    path("weibo/<int:weibo_id>.html", weibo.detail , name = 'weibo_detail'),
    path("weibo/<int:weibo_id>_<int:page>.html", weibo.detail , name = 'weibo_detail_list'),
    path("weibo/createdo.html", weibo.createdo , name = 'weibo_createdo'),
    path("weibo/replydo.html", weibo.replydo , name = 'weibo_replydo'),
    path("weibo/del.html", weibo.delete , name = 'weibo_del'),


    path("sitemap.html", sitemap.index , name = 'sitemap'),

    path("search.html", search.index , name = 'search'),
    path("search/list_<int:page>.html", search.index , name = 'search_list'),
    path("search/<str:tag>.html", search.index , name = 'search_tag'),
    path("search/<str:tag>/list_<int:page>.html", search.index , name = 'search_tag_list'),

    re_path("(?P<route_name>[a-z\/]+).html", cate.list , name = 'list'),                                  #列表
    re_path("(?P<route_name>[a-z\/]+)/list_(?P<page>[0-9]+).html", cate.list , name = 'list_list'),       #列表

    re_path("(?P<route_name>[a-z\/]+)/(?P<third_id>[0-9]+).html", cate.detail , name = 'detail'),                              #文章详情
    re_path("(?P<route_name>[a-z\/]+)/(?P<third_id>[0-9]+)_(?P<page>[0-9]+).html", cate.detail , name = 'detail_list'),        #文章详情
]