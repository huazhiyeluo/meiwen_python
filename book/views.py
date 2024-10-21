from django.shortcuts import render

import model.book
import model.user
import qiu.utils
import qiu.common
from django.urls import reverse

from qiu.mypage import MyPaper

# Create your views here.

def index(request , page = 1 , cid1 =0 , cid2 =0 , route_field = 'book' , route_name = 'book'):
    type = 1
    size = 28

    data          = {}
    data['controller'] = 'book'
    data['route_name'] = route_name
    data['route_field'] = route_field

    paginatorParams = []
    if route_field != route_name:
        paginatorParams = [route_name]


    #1、分类下导航
    tempAllCategorys = qiu.utils.get_categorys_by_type(type)
    tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 0, 0)

    #2、关联菜单
    relationCategorys = {key: tempCategorys[key] for key in list(tempCategorys)[0:8]}
    nav = qiu.utils.get_first_nav(type)
    relationCategorys = {**{0:nav},**relationCategorys}
    data['relationCategorys'] = relationCategorys

    #3、书籍列表
    where = []
    if cid2 != 0:
        where.append(['cid2','=',cid2])
    elif cid1 != 0:
        where.append(['cid1','=',cid1])

    books = model.book.get_books_list( {'where':where,'order':{'book_id':'desc'}},['book_id', 'title', 'cid1', 'cid2', 'author', 'cover', 'desc'],page,size )
    books['list'] = qiu.utils.get_init_list(books['list'], tempAllCategorys ,1)

    paginator = MyPaper(page, size, books['total'])  # 10表示每页显示的项数
    data['list'] = books['list']
    data['page'] = paginator.create_links(route_field,paginatorParams)

    #4、热门书籍
    hotBooks = model.book.get_books( {'where':where,'order':{'count_view':'desc'}},['book_id', 'title', 'cid1', 'cid2', 'author', 'cover', 'desc'],1,8 )
    data['hotBooks'] = qiu.utils.get_init_list(hotBooks, tempAllCategorys ,1)

    #5、最新书籍
    newBooks = model.book.get_books( {'where':where,'order':{'book_id':'desc'}},['book_id', 'title', 'cid1', 'cid2', 'author', 'cover', 'desc'],1,8 )
    data['newBooks'] = qiu.utils.get_init_list(newBooks, tempAllCategorys ,1)

    #6、热门菜单
    tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 2, cid1)
    hotCategorys = {key: tempCategorys[key] for key in list(tempCategorys)[0:6]}
    data['hotCategorys'] = hotCategorys

    breadcrumbs = []
    if cid2 != 0:
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['pCategorys'][cid1]['route_name']]) , 'title':tempAllCategorys['pCategorys'][cid1]['title'] })
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['cCategorys'][cid2]['route_name']]) , 'title':tempAllCategorys['cCategorys'][cid2]['title'] })
    elif cid1 !=0:
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['pCategorys'][cid1]['route_name']]) , 'title':tempAllCategorys['pCategorys'][cid1]['title'] })

    firstBreadcrumb = qiu.utils.get_first_breadcrumb(type)
    breadcrumbs.insert(0,firstBreadcrumb)
    breadcrumbs.insert(0,{'url':reverse('index'),'title':'首页'})
    data['breadcrumbs'] = breadcrumbs


    initData = qiu.common.get_init_data(request)
    initData['seo'] = qiu.common.get_nav_seo(initData['seo'],tempCategorys , type , cid1)

    data = {**data,**initData}

    return render(request, 'book/index.html', data)


def chapter(request , book_id = 0,  route_field = 'book' , route_name = ''):
    data          = {}
    data['controller'] = 'book'
    data['route_name'] = route_name
    data['route_field'] = route_field

    #1、分类下导航
    type = 1
    tempAllCategorys = qiu.utils.get_categorys_by_type(type)
    tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 0, 0)

    #2、关联菜单
    relationCategorys = {key: tempCategorys[key] for key in list(tempCategorys)[0:8]}
    nav = qiu.utils.get_first_nav(type)
    relationCategorys = {**{0:nav},**relationCategorys}
    data['relationCategorys'] = relationCategorys

    #3、书籍信息
    book = model.book.get_book({'where':[['book_id','=',book_id]]},[])
    book.route_name = route_name
    data['book'] = book

    #4、阅读量
    model.book.edit_book({'count_view': book.count_view + 1},{'book_id':book_id})

    #5、章节信息
    chapters = model.book.get_book_chapters({'where':[['book_id','=',book_id]] ,'order':{'chapter_id':'asc'}},['chapter_id','title'],1,5000)
    data['chapters'] = chapters

    
    cid1 = book.cid1
    cid2 = book.cid2
    where = {}
    if cid2 != 0:
        where['cid2'] = cid2
    elif cid1 != 0:
        where['cid1'] = cid1

    #7、热门书籍
    hotBooks = model.book.get_books( {'where':where,'order':{'count_view':'desc'}},['book_id', 'title', 'cid1', 'cid2', 'author', 'cover', 'desc'],1,8 )
    data['hotBooks'] = qiu.utils.get_init_list(hotBooks, tempAllCategorys ,1)

    #8、最新书籍
    newBooks = model.book.get_books( {'where':where,'order':{'book_id':'desc'}},['book_id', 'title', 'cid1', 'cid2', 'author', 'cover', 'desc'],1,8 )
    data['newBooks'] = qiu.utils.get_init_list(newBooks, tempAllCategorys ,1)

    #9、热门菜单
    tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 2, cid1)
    hotCategorys = {key: tempCategorys[key] for key in list(tempCategorys)[0:6]}
    data['hotCategorys'] = hotCategorys


    breadcrumbs = []
    if cid2 != 0:
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['pCategorys'][cid1]['route_name']]) , 'title':tempAllCategorys['pCategorys'][cid1]['title'] })
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['cCategorys'][cid2]['route_name']]) , 'title':tempAllCategorys['cCategorys'][cid2]['title'] })
        breadcrumbs.append({'url': reverse('detail',args = [tempAllCategorys['cCategorys'][cid2]['route_name'], book.book_id]) , 'title':book.title, 'cl' : 'ts-hide'})
    elif cid1 !=0:
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['pCategorys'][cid1]['route_name']]) , 'title':tempAllCategorys['pCategorys'][cid1]['title'] })
        breadcrumbs.append({'url': reverse('detail',args = [tempAllCategorys['pCategorys'][cid1]['route_name'], book.book_id]) , 'title':book.title, 'cl' : 'ts-hide'})
    

    firstBreadcrumb = qiu.utils.get_first_breadcrumb(type)
    breadcrumbs.insert(0,firstBreadcrumb)
    breadcrumbs.insert(0,{'url':reverse('index'),'title':'首页'})
    data['breadcrumbs'] = breadcrumbs

    initData = qiu.common.get_init_data(request)
    keywords = ','.join(qiu.utils.array_column_val({key: tempCategorys[key] for key in list(tempCategorys)[0:12]}, 'title'))
    initData['seo'] = qiu.common.share_seo(initData['seo'], book.title , keywords , book.desc)
    data = {**data,**initData}

    return render(request, 'book/chapter.html', data)


def detail(request , book_id = 0 , chapter_id = 0 , route_field = 'book' , route_name = ''):

    data          = {}
    data['controller'] = 'book'
    data['route_name'] = route_name

    #1、分类下导航
    type = 1
    tempAllCategorys = qiu.utils.get_categorys_by_type(type)
    tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 0, 0)

    #2、关联菜单
    relationCategorys = {key: tempCategorys[key] for key in list(tempCategorys)[0:8]}
    nav = qiu.utils.get_first_nav(type)
    relationCategorys = {**{0:nav},**relationCategorys}
    data['relationCategorys'] = relationCategorys

    #3、书籍信息
    book = model.book.get_book({'where':[['book_id','=',book_id]]},[])
    book.route_name = route_name
    data['book'] = book

    #4、书籍阅读量
    model.book.edit_book({'count_view': book.count_view + 1},{'book_id':book_id})

    #5、书籍关联用户
    tuserInfo = model.user.get_user_info(book.uid)
    data['tuserInfo'] = tuserInfo

    #6、书籍章节信息
    chapter = model.book.get_book_chapter({'where':[['book_id','=',book_id],['chapter_id','=',chapter_id]]})
    chapter.addtime = qiu.utils.time_tran(chapter.addtime)
    data['chapter'] = chapter
    chapterContent = model.book.get_chapter_content(chapter.link_id)
    data['chapterContent'] = chapterContent

    cid1 = book.cid1
    cid2 = book.cid2
    where = {}
    if cid2 != 0:
        where['cid2'] = cid2
    elif cid1 != 0:
        where['cid1'] = cid1
    
    #7、热门书籍
    hotBooks = model.book.get_books( {'where':where,'order':{'count_view':'desc'}},['book_id', 'title', 'cid1', 'cid2', 'author', 'cover', 'desc'],1,8 )
    data['hotBooks'] = qiu.utils.get_init_list(hotBooks, tempAllCategorys ,1)

    #8、最新书籍
    newBooks = model.book.get_books( {'where':where,'order':{'book_id':'desc'}},['book_id', 'title', 'cid1', 'cid2', 'author', 'cover', 'desc'],1,8 )
    data['newBooks'] = qiu.utils.get_init_list(newBooks, tempAllCategorys ,1)

    #9、热门菜单
    tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 2, cid1)
    hotCategorys = {key: tempCategorys[key] for key in list(tempCategorys)[0:6]}
    data['hotCategorys'] = hotCategorys


    breadcrumbs = []
    if cid2 != 0:
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['pCategorys'][cid1]['route_name']]) , 'title':tempAllCategorys['pCategorys'][cid1]['title'] })
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['cCategorys'][cid2]['route_name']]) , 'title':tempAllCategorys['cCategorys'][cid2]['title'] })
        breadcrumbs.append({'url': reverse('detail',args = [tempAllCategorys['cCategorys'][cid2]['route_name'], book.book_id]) , 'title':book.title, 'cl' : 'ts-hide'})
        breadcrumbs.append({'url': reverse('detail_list',args = [tempAllCategorys['cCategorys'][cid2]['route_name'], book.book_id, chapter.book_id]) , 'title':chapter.title, 'cl' : 'ts-hide'})
    elif cid1 !=0:
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['pCategorys'][cid1]['route_name']]) , 'title':tempAllCategorys['pCategorys'][cid1]['title'] })
        breadcrumbs.append({'url': reverse('detail',args = [tempAllCategorys['pCategorys'][cid1]['route_name'], book.book_id]) , 'title':book.title, 'cl' : 'ts-hide'})
        breadcrumbs.append({'url': reverse('detail_list',args = [tempAllCategorys['pCategorys'][cid1]['route_name'], book.book_id, chapter.book_id]) , 'title':chapter.title, 'cl' : 'ts-hide'})
    

    firstBreadcrumb = qiu.utils.get_first_breadcrumb(type)
    breadcrumbs.insert(0,firstBreadcrumb)
    breadcrumbs.insert(0,{'url':reverse('index'),'title':'首页'})
    data['breadcrumbs'] = breadcrumbs


    #10、上下章节
    data['prevChapter'] = model.book.get_book_chapter({'where':[['book_id','=',book_id],['chapter_id','<',chapter_id]],'order':{'chapter_id':'desc'}})
    data['nextChapter'] = model.book.get_book_chapter({'where':[['book_id','=',book_id],['chapter_id','>',chapter_id]],'order':{'chapter_id':'asc'}})

    initData = qiu.common.get_init_data(request)
    keywords = ','.join(qiu.utils.array_column_val({key: tempCategorys[key] for key in list(tempCategorys)[0:12]}, 'title'))
    initData['seo'] = qiu.common.share_seo(initData['seo'], book.title , keywords , book.desc)
    data = {**data,**initData}

    return render(request, 'book/detail.html', data)

