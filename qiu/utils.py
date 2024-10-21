#公共方法
from datetime import datetime
from index.models import TsCategory
from django.core.cache import cache
import model.user
from django.urls import reverse
import re

'''
通过类型获取name
'''
def get_first_name(type):
    name = ''
    if type == 1:
        name = '图书'
    elif type == 2:
        name = '美文'
    elif type == 3:
        name = '故事'
    elif type == 4:
        name = '作文'
    elif type == 5:
        name = '章节'
    return name

'''
通过类型获取name
'''
def get_controller(type):
    name = ''
    if type == 1:
        name = 'book'
    elif type == 2:
        name = 'meiwen'
    elif type == 3:
        name = 'gushi'
    elif type == 4:
        name = 'zuowen'
    elif type == 5:
        name = 'book'
    return name

'''
通过nav
'''
def get_first_nav(type):
    nav = {}
    if type == 1:
        nav = {'route_name': 'book', 'title': '全部'}
    elif type == 2:
        nav = {'route_name': 'meiwen', 'title': '全部'}
    elif type == 3:
        nav = {'route_name': 'gushi', 'title': '全部'}
    elif type == 4:
        nav = {'route_name': 'zuowen', 'title': '全部'}
    return nav


def get_show_type():
    showType = [
        {'type': 1, 'flag': 'book', 'title': '图书', 'is_show': 1},
        {'type': 2, 'flag': 'meiwen', 'title': '美文', 'is_show': 1},
        {'type': 3, 'flag': 'gushi', 'title': '故事', 'is_show': 1},
        {'type': 4, 'flag': 'zuowen', 'title': '作文', 'is_show': 1}
    ]
    return showType

def get_first_breadcrumb(type):
    breadcrumb = {}
    if type == 1:
        breadcrumb = {'url': reverse('book'), 'title': '图书'}
    elif type == 2:
        breadcrumb = {'url': reverse('meiwen'), 'title': '美文'}
    elif type == 3:
        breadcrumb = {'url': reverse('gushi'), 'title': '故事'}
    elif type == 4:
        breadcrumb = {'url': reverse('zuowen'), 'title': '作文'}
    return breadcrumb

'''
通过type 获取所有分类
'''
def get_categorys_by_type(type = 0):

    cacheKey = "allCategorys_%d" % type
    allCategorys = cache.get(cacheKey)
    if allCategorys is None:
        db = TsCategory.objects
        if type > 0: 
            db = db.filter(type=type)

        tempCategorys = db.values('cid', 'pcid', 'type', 'title', 'route_name').all().order_by('sort','cid')
        if len(tempCategorys) >0:
            pallCategorys = {}
            callCategorys = {}
            for category in tempCategorys:
                if category['pcid'] == 0:
                    pallCategorys[category['cid']] = category

            for category in tempCategorys:
                pcid = category['pcid']
                type = category['type']

                if pcid >0 :
                    category['route_name'] = "%s/%s"  % (pallCategorys[pcid]['route_name'], category['route_name'])
                    callCategorys[category['cid']] = category

            allCategorys = {"pCategorys": pallCategorys,"cCategorys":callCategorys}
            cache.set(cacheKey, allCategorys, 24 * 3600)

    return allCategorys

'''
获取相应的分类
'''
def get_relation_categorys(all_categorys, level=0, pcid=0):
    temp_categorys = {}

    if level:
        if level == 1:
            temp_categorys = all_categorys['pCategorys']
        if level == 2:
            temp_categorys = all_categorys['cCategorys']
    else:
        temp_categorys = {**all_categorys['pCategorys'],**all_categorys['cCategorys']}

    relation_categorys = {k: v for k, v in temp_categorys.items() if pcid == 0 or pcid == v['pcid']}
    return relation_categorys




'''
获取路由信息
'''
def get_route_info(allCategorys, cid1 = 0, cid2 = 0):
    info = {}
    if cid2 != 0:
        if cid2 in allCategorys['cCategorys']:
            info = allCategorys['cCategorys'][cid2]
    else:
        if cid1 in allCategorys['pCategorys']:
            info = allCategorys['pCategorys'][cid1]
    return info;


'''
初始化列表数据
'''
def get_init_list(list, allCategorys, type):
    if len(list)> 0 :
        for item in list:
            if 'uid' in item:
                userInfo = model.user.get_user_info(item['uid'])
                item['username'] = userInfo['username']
            if 'addtime' in item:
                item['addtime'] = time_tran(item['addtime'])

            routeInfo = get_route_info(allCategorys, item['cid1'], item['cid2'])
            item['route_info'] = routeInfo
    return list



'''
时间转换
'''
def time_tran(time_int, format='%Y-%m-%d %H:%M'):
    time_int = int(time_int)
    current_time = int(datetime.now().timestamp())
    time_difference = current_time - time_int
    
    if time_difference < 0:
        return time_int
    elif time_difference < 60:
        return f'{time_difference}秒前'
    elif time_difference < 3600:
        return f'{time_difference // 60}分钟前'
    elif time_difference < 86400:
        return f'{time_difference // 3600}小时前'
    elif time_difference < 259200:
        return f'{time_difference // 86400}天前'
    else:
        return datetime.fromtimestamp(time_int).strftime(format)




'''
移除html、截取字符串
'''
def get_info(content, length=150):
    # 移除 HTML 标签
    info = re.sub(r'<.*?>', '', content)
    info = info.strip()
    info = re.sub(r'&#13;| |\&nbsp;|　|\r\n|\n|\r', '', info)
    info = info[:length] + '...'
    return info.strip()

'''
获取文章封面
'''
def get_cover(content):
    cover = ''
    pattern = r'<img[^>]*src=[\'"]?([^>\'"\s]*)[\'"]?[^>]*>'
    match = re.search(pattern, content, re.I | re.S)
    
    if match:
        cover = match.group(1)
    
    return cover

def get_content_table_index(mark):
    result = {0: {}, 1: {}}

    for article_id, is_mul_page in mark.items():
        if is_mul_page == 0:
            index = article_id // 4000
            result[0].setdefault(index, []).append(article_id)
        elif is_mul_page == 1:
            index = article_id // 50000
            result[1].setdefault(index, []).append(article_id)

    return result


def array_object(lst, index_key):
    result = {item[index_key]: item for item in lst}
    return result

def array_column(lst, value_key, index_key):
    result = {item[index_key]: item[value_key] for item in lst}
    return result

def array_column_val(lst, index_key):
    result = [item[index_key] for item in lst.values()]
    return result

