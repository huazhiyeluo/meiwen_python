from django.shortcuts import render

from django.core.cache import cache
import qiu.utils
import model.article 
from django.urls import reverse

from qiu.mypage import MyPaper
# Create your views here.

# 定义index函数，用于获取文章列表
def index(request ,  page = 1 , cid1 =0 , cid2 =0 , route_field = '' , route_name = '', temptype = 2, **kwargs):
    # 获取参数
    type = kwargs.get("type")
    if type == None:
        type = temptype
    type = int(type)
    

    controller = qiu.utils.get_controller(type)
    if route_field == '':
        route_field = controller
        route_name = controller

    cacheKey = "ARTICLE_%d" % (type,)
    data = cache.get(cacheKey)

    size = 15
    data          = {}
    data['controller'] = controller
    data['route_field'] = route_field
    data['route_name'] = route_name
    data['tag_name'] = qiu.utils.get_first_name(type)

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

    where = []
    if cid2 != 0:
        where.append(['cid2','=',cid2])
    elif cid1 != 0:
        where.append(['cid1','=',cid1])

    #3、文章列表
    articles = model.article.get_articles_list(type, {'where':where,'order':{'article_id':'desc'}},['article_id', 'uid','is_mul_page','title', 'cid1', 'cid2', 'cover','addtime'],page,size )
    articles['list'] = model.article.get_content_all(type, articles['list']);
    articles['list'] = qiu.utils.get_init_list(articles['list'], tempAllCategorys ,1)

    paginator = MyPaper(page, size, articles['total'])  # 10表示每页显示的项数
    data['list'] = articles['list']
    data['page'] = paginator.create_links(route_field,paginatorParams)

    #4、热门书籍
    hotArticles = model.article.get_articles( type,{'where':where,'order':{'count_view':'desc'}},['article_id', 'title', 'cid1', 'cid2'],1,22 )
    data['hotArticles'] = qiu.utils.get_init_list(hotArticles, tempAllCategorys ,1)

    #5、最新书籍
    newArticles = model.article.get_articles(type, {'where':where,'order':{'article_id':'desc'}},['article_id', 'title', 'cid1', 'cid2'],1,22 )
    data['newArticles'] = qiu.utils.get_init_list(newArticles, tempAllCategorys ,1)

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

    return render(request, 'article/index.html', data)



# 定义index函数，用于获取文章列表
def detail(request , article_id = 0 ,  page = 1 , route_field = '' , route_name = '' , type = 2):

    article_id = int(article_id)
    # 获取参数
    controller = qiu.utils.get_controller(type)
    
    size = 15
    data          = {}
    data['controller'] = controller
    data['route_field'] = route_field
    data['route_name'] = route_name
    data['tag_name'] = qiu.utils.get_first_name(type)

    tempAllCategorys = qiu.utils.get_categorys_by_type(type)
    tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 0, 0)


    relationCategorys = {key: tempCategorys[key] for key in list(tempCategorys)[0:8]}
    nav = qiu.utils.get_first_nav(type)
    relationCategorys = {**{0:nav},**relationCategorys}
    data['relationCategorys'] = relationCategorys

    where = []
    where.append(['article_id','=',article_id])
    article = model.article.get_article(type, {'where':where},[])

    model.article.edit_article_content(type , article_id,{'count_view':article.count_view+1},{'article_id':article_id})

    if article.is_mul_page == 0:
        articleContent = model.article.get_article_content(type,article_id)
    else:
        articleContent = model.article.get_article_content_mul(type,article_id)
        total = model.article.get_article_content_mul_count(type, article_id)

        paginator = MyPaper(page, size, total)  # 10表示每页显示的项数
        data['page'] = paginator.create_links(route_field,[route_name,article_id])

    article.count_view = article.count_view+1
    article.content = articleContent.content
    article.info = qiu.utils.get_info(article.content)
    article.addtime = qiu.utils.time_tran(article.addtime)
    data['article'] = article
    tuserInfo = model.user.get_user_info(article.uid)
    data['tuserInfo'] = tuserInfo

    cid1 = article.cid1
    cid2 = article.cid2

    where = []
    if cid2 != 0:
        where.append(['cid2','=',cid2])
    elif cid1 != 0:
        where.append(['cid1','=',cid1])

    hotArticles = model.article.get_articles( type,{'where':where,'order':{'count_view':'desc'}},['article_id', 'title', 'cid1', 'cid2'],1,22 )
    data['hotArticles'] = qiu.utils.get_init_list(hotArticles, tempAllCategorys ,1)

    newArticles = model.article.get_articles(type, {'where':where,'order':{'article_id':'desc'}},['article_id', 'title', 'cid1', 'cid2'],1,22 )
    data['newArticles'] = qiu.utils.get_init_list(newArticles, tempAllCategorys ,1)

    tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 2, cid1)
    hotCategorys = {key: tempCategorys[key] for key in list(tempCategorys)[0:6]}
    data['hotCategorys'] = hotCategorys


    breadcrumbs = []
    if cid2 != 0:
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['pCategorys'][cid1]['route_name']]) , 'title':tempAllCategorys['pCategorys'][cid1]['title'] })
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['cCategorys'][cid2]['route_name']]) , 'title':tempAllCategorys['cCategorys'][cid2]['title'] })
        breadcrumbs.append({'url': reverse('detail',args = [tempAllCategorys['cCategorys'][cid2]['route_name'], article.article_id]) , 'title':article.title, 'cl' : 'ts-hide'})
    elif cid1 !=0:
        breadcrumbs.append({'url': reverse('list',args = [tempAllCategorys['pCategorys'][cid1]['route_name']]) , 'title':tempAllCategorys['pCategorys'][cid1]['title'] })
        breadcrumbs.append({'url': reverse('detail',args = [tempAllCategorys['pCategorys'][cid1]['route_name'], article.article_id]) , 'title':article.title, 'cl' : 'ts-hide'})
    

    firstBreadcrumb = qiu.utils.get_first_breadcrumb(type)
    breadcrumbs.insert(0,firstBreadcrumb)
    breadcrumbs.insert(0,{'url':reverse('index'),'title':'首页'})
    data['breadcrumbs'] = breadcrumbs

    initData = qiu.common.get_init_data(request)
    keywords = ','.join(qiu.utils.array_column_val({key: tempCategorys[key] for key in list(tempCategorys)[0:12]}, 'title'))
    initData['seo'] = qiu.common.share_seo(initData['seo'], article.title , keywords , article.info)

    data = {**data,**initData}

    return render(request, 'article/detail.html', data)