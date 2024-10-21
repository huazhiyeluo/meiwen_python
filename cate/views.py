from django.shortcuts import render

# Create your views here.
import model.book
import model.user
import qiu.utils
import qiu.common
import book.views
import article.views


'''
列表页
'''
def list(request , route_name = '' , page = 1 ):
    category = {}
    for type in [1,2,3,4]:
        tempAllCategorys = qiu.utils.get_categorys_by_type(type)
        tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 0, 0)
        for key,item in tempCategorys.items():
            if item['route_name'] == route_name:
                category = item
                break

    if category['pcid'] == 0:
        cid1 = category['cid']
        cid2 = 0
    else:
        cid1 = category['pcid']
        cid2 = category['cid']
    
    if category['type'] == 1:
        return book.views.index(request , int(page) , cid1 , cid2 , 'list' , route_name)
    else:
        return article.views.index(request , int(page) , cid1 , cid2 , 'list' , route_name , category['type'] )
    


'''
详情页
'''
def detail(request, route_name = '' , third_id = 0, page = ''):
    category = {}
    for type in [1,2,3,4]:
        tempAllCategorys = qiu.utils.get_categorys_by_type(type)
        tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 0, 0)
        for key,item in tempCategorys.items():
            if item['route_name'] == route_name:
                category = item
                break

    if category['pcid'] == 0:
        cid1 = category['cid']
        cid2 = 0
    else:
        cid1 = category['pcid']
        cid2 = category['cid']
    
    if category['type'] == 1:
        if page == '':
            return book.views.chapter(request , third_id , 'detail' , route_name)
        else:
            return book.views.detail(request , third_id , int(page) , 'detail' , route_name)
    else:
        if page == '':
            page = 1
        return article.views.detail(request , third_id , int(page) , 'detail' , route_name, category['type'] )
