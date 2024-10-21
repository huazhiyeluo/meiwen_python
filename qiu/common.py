import qiu.utils
import model.category
from django.core.cache import cache
from decouple import config
import random

def get_init_data(request):
    data = {}

    #1、展示类型
    data['showType'] = showType = qiu.utils.get_show_type()

    #2、顶部推荐菜单
    cache_key = 'top_type'
    randnum = cache.get(cache_key)
    if randnum is None:
        types = [item['type'] for item in showType]
        random_index = random.randint(0, len(types) - 1)
        randnum = types[random_index]
        cache.set(cache_key, randnum, 24 * 3600)

    gettype = 2 if randnum in [1, 3] else 1
    tempAllCategorys = qiu.utils.get_categorys_by_type(randnum)
    tempCategorys = qiu.utils.get_relation_categorys(tempAllCategorys, gettype, 0)
    data['topNavCategorys'] = {key: tempCategorys[key] for key in list(tempCategorys)[0:4]}

    #3、搜索提示标题
    data['searchTitle'] = '|'.join(item['title'] for item in showType)

    #4-1、基础配置
    data['baseConfig'] = {
        'sitename':config('SITENAME', default=''),
        'contact':config('CONTACT', default=''),
        'weburl':config('WEBURL', default=''),
        'beian':config('BEIAN', default=''),
        'version':config('VERSION', default=''),
        'theme':config('THEME', default=''),
    }
    #4-2、统计打点
    data['tongji'] = config('TONGJI', default='')

    #4-3、SEO
    data['seo'] = get_seo()

    # 5、浏览器类型
    data['edittype'] = detect_device(request)

    # 6、获取微信分享参数
    data['weixin'] = {'appId':'wx15fd0f9b451abfbd', 'nonceStr' :'8AaU3AljFYjXJzyl', 'timestamp' : 1573094843, 'url': data['baseConfig']['weburl'], 'signature' : 'signature', 'rawString' : 'jsapi_ticket=sM4AOVdWfPE4DxkXGEs8VGs4TY5wRfQJl4zPiVUMk2N7MwFt2spo1urMqh2JlG3Ohi-8R0WA5rkQuMvzdKv4Ew&noncestr=8AaU3AljFYjXJzyl×tamp=1573094843&url='+data['baseConfig']['weburl']}

    return data


def detect_device(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    if 'mobile' in user_agent or 'android' in user_agent or 'iphone' in user_agent:
        return 'mobile'
    else:
        return 'pc'

def get_seo(title = '' , keywords = '' , description = '' , photo = ''):
    if title == '':
        title = config('SEO_TITLE', default='')
    if keywords == '':
        keywords = config('SEO_KEYWORDS', default='')
    if description == '':
        description = config('SEO_DESCRIPTION', default='')
    if photo == '':
        photo = config('SEO_PHOTO', default='')

    return  {
        'title':title,
        'keywords':keywords,
        'description':description,
        'photo':photo,
    }

def get_nav_seo(defaultSeo , navs , type , cid):
    title = ''
    keywords = ''
    description = ''

    cateName = qiu.utils.get_first_name(type)

    if cid != 0:
        category = model.category.get_category({'where':[['cid','=',cid]]})
        if category.cid != 0:
            title = category.meta_title
            keywords = category.meta_keywords
            description = category.meta_description

            cateName = category.title

    if len(navs) >0 :
        titles = qiu.utils.array_column_val(navs , 'title')

        num = len(titles)
        x = 12 if num >= 12 else num
        y = 18 if num >= 18 else num

        tempTitle1 = titles[0:x]
        tempTitle2 = titles[0:y]


        sitename = config('SITENAME', default='')
        weburl = config('WEBURL', default='')
        if title == "":
            title = cateName + '_' + sitename +  '网';
        if keywords == "":
            keywords = ','.join(tempTitle1)
        if description == "":
            description = sitename + '网(' + weburl + ')中' + cateName + '栏目为您提供了' + '、'.join(tempTitle2) + '等各类精美文章,欢迎阅读浏览分享！';

    if title == "":
        title = defaultSeo['title']

    if keywords == "":
        keywords = defaultSeo['keywords']

    if description == "":
        description = defaultSeo['description']

    return  {
        'title':title,
        'keywords':keywords,
        'description':description,
        'photo':defaultSeo['photo']
    }

def share_seo(defaultSeo ,title='', keywords='', description='', photo=''): 
    sitename = config('SITENAME', default='')    
    share_info = {
        'title': defaultSeo['title'],
        'keywords': defaultSeo['keywords'],
        'description': defaultSeo['description'],
        'photo': defaultSeo['photo']
    }

    if title:
        share_info['title'] = f"{title}_{sitename}网"

    if keywords:
        share_info['keywords'] = keywords

    if description:
        share_info['description'] = description

    if photo:
        share_info['photo'] = photo

    return share_info


