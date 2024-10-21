from django.shortcuts import render

from .models import TsLinks
from django.core.cache import cache
import model.article 
import model.book
import qiu.utils
import qiu.common

# Create your views here.

def index(request):

    cacheKey = "HOME_DATA"
    data = cache.get(cacheKey)

    if data is None:
        data          = {}
        data['controller'] = 'index'

        #1、定义分类
        allCategorys = {'pCategorys':{},'cCategorys':{}}

        #2、推荐书籍
        tempAllCategorys = qiu.utils.get_categorys_by_type(1)
        # tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 1, 0);
        allCategorys['pCategorys'] = {**allCategorys['pCategorys'],**tempAllCategorys['pCategorys']}
        allCategorys['cCategorys'] = {**allCategorys['cCategorys'],**tempAllCategorys['cCategorys']}

        books = model.book.get_books( {'order':{'book_id':'desc'}},['book_id', 'title', 'cid1', 'cid2', 'author', 'cover', 'desc'],1,6 )
        data['recBooks'] = qiu.utils.get_init_list(books, tempAllCategorys ,1)
        
        #3、友链
        friendchain = TsLinks.objects.values('sitename', 'url', 'keywords').order_by("sort")
        data['friendchain'] = friendchain

        
        #4、推荐文章
        types = [2,3,4]
        data['list'] = {}
        data['newArticles'] = {}
        data['hotArticles'] = {}
        for type in types:
            print(type)
            tempAllCategorys = qiu.utils.get_categorys_by_type(type)
            tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, 1, 0);
            allCategorys['pCategorys'] = {**allCategorys['pCategorys'],**tempAllCategorys['pCategorys']}
            allCategorys['cCategorys'] = {**allCategorys['cCategorys'],**tempAllCategorys['cCategorys']}

            categorys = {key: tempCategorys[key] for key in list(tempCategorys)[:4]}
            
            if len(categorys) > 0:
                for k,v in categorys.items():
                    data['list'][v['cid']] = {}
                    articles = model.article .get_articles(type, {'where': [['cid1','=',v['cid']],['is_audit','=',1]],'order':{'article_id':'desc'}},['article_id', 'cid1', 'cid2', 'title'],1,18)
                    data['list'][v['cid']]['articles'] = qiu.utils.get_init_list(articles, tempAllCategorys ,1)
                    data['list'][v['cid']]['category'] = v

            if type == 2:
                articles = model.article.get_articles(type, {'where': [['cover','<>','']],'order':{'article_id':'desc'}},['article_id', 'cid1', 'cid2','cover', 'title'],1,2)
                data['coverArticles'] = qiu.utils.get_init_list(articles, tempAllCategorys ,1)


            data['newArticles'][type] = {}
            data['hotArticles'][type] = {}

            articles = model.article.get_articles(type, {'where': [['is_audit','=',1]],'order':{'article_id':'desc'}},['article_id', 'cid1', 'cid2','title'],1,22)
            data['newArticles'][type]['list'] = qiu.utils.get_init_list(articles, tempAllCategorys ,1)
            data['newArticles'][type]['name'] = qiu.utils.get_first_name(type)

            articles = model.article.get_articles(type, {'where': [['is_audit','=',1]],'order':{'count_view':'desc'}},['article_id', 'cid1', 'cid2','title'],1,22)
            data['hotArticles'][type]['list'] = qiu.utils.get_init_list(articles, tempAllCategorys ,1)
            data['hotArticles'][type]['name'] = qiu.utils.get_first_name(type)

        # 5、取得所有导航
        tempCategorys = qiu.utils.get_relation_categorys(allCategorys, 0, 0)

        #6、推荐导航
        recCategorys = {key: tempCategorys[key] for key in list(tempCategorys)[6:42]}
        data['recCategorys'] = recCategorys;

        #7、热门导航
        hotCategorys = {key: tempCategorys[key] for key in list(tempCategorys)[0:6]}
        data['hotCategorys'] = hotCategorys;

        # 8、初始化数据【1、展示类型 | 2、顶部推荐菜单 | 3、搜索标题】 
        initData = qiu.common.get_init_data(request)

        data = {**data,**initData}

        cache.set(cacheKey, data, 24 * 3600)
    

    return render(request, 'index/index.html', data)

def info(request , **kwargs):
    data          = {}
    data['controller'] = 'index'
    data["tag"] = kwargs.get("tag")

    initData = qiu.common.get_init_data(request)

    data = {**data,**initData}

    return render(request, 'index/info.html', data)