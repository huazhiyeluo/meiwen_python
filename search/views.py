from django.shortcuts import render
import qiu.utils
import qiu.common

from qiu.mypage import MyPaper

import model.search
import model.book
from django.urls import reverse

# Create your views here.

def index(request , tag = '' ,page = 1):

    size = 15

    data          = {}
    data['controller'] = 'index'
    data['tag'] = tag
    route_field = ''
    url = ''
    params = []
    if (tag == ''):
        route_field = 'search'
        url = reverse("search", args = [])
    else:
        route_field = 'search_tag'
        url = reverse("search_tag", args = [tag])
        params = [tag]
    data['url'] = url

    keyword = request.POST.get("keyword","")
    if keyword == '':
        keyword = request.GET.get("keyword","")

    data['keyword'] = keyword

    if keyword == '':
        data['list']  = []
        data['total']  = 0
        data['page']  = ''
    else:
        if tag == '':
            searchs = model.search.get_search_all(keyword, page , 15)
        elif tag == 'book':
            searchs = model.search.get_search_book(keyword, page , 15)
        elif tag == 'meiwen':
            searchs = model.search.get_search_meiwen(keyword, page , 15)
        elif tag == 'gushi':
            searchs = model.search.get_search_gushi(keyword, page , 15)
        elif tag == 'zuowen':
            searchs = model.search.get_search_zuowen(keyword, page , 15)
            book_ids = list(set([item['b_id'] for item in searchs['list']]))
            books = model.book.get_books( {'where_in':{'book_id':book_ids}},['book_id', 'title', 'cid1', 'cid2', 'author', 'cover', 'desc'],1,len(book_ids) )
            books = qiu.utils.array_object(books,'book_id')
            for item in searchs['list']:
                item['catename'] = qiu.utils.get_first_name(item['oid'])
                if item['oid'] == 5:
                    item['cid1'] = books[item['b_id']]['cid1']
                    item['cid2'] = books[item['b_id']]['cid2']
                    item['book_title'] = books[item['b_id']]['title']

        for item in searchs['list']:
            item['catename'] = qiu.utils.get_first_name(item['oid'])
        

        tempAllCategorys = qiu.utils.get_categorys_by_type(0)
        searchs['list'] = qiu.utils.get_init_list(searchs['list'], tempAllCategorys ,1)
        data['list']  = searchs['list']
        data['total']  = searchs['total']

        paginator = MyPaper(page, size, searchs['total'])  # 10表示每页显示的项数
        data['page'] = paginator.create_links(route_field,params , '_' , '?keyword='+keyword)

        
    initData = qiu.common.get_init_data(request)

    data = {**data,**initData}

    return render(request, 'search/index.html', data)