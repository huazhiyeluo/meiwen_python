from index.models import TsUserInfo,TsArticleMeiwen,TsArticleGushi,TsArticleZuowen
from index.models_article import TsContentArticle,TsContentArticleMul
import qiu.utils
from itertools import chain

def get_table_object(type):
    if type == 2:
        return TsArticleMeiwen
    elif type == 3:
        return TsArticleGushi
    else:
        return TsArticleZuowen

def get_db(type):
    if type == 2:
        return 'meiwen'
    elif type == 3:
        return 'gushi'
    else:
        return 'zuowen'



def get_article(type , condition = {}, fields = [] ):

    db = get_table_object(type).objects

    if 'where' in condition:
        for v in condition['where']:
            if v[1] == '=':
                db = db.filter(**{v[0]: v[2]})
            elif v[1] == '>':
                db = db.filter(**{f"{v[0]}__gt": v[2]})
            elif v[1] == '>=':
                db = db.filter(**{f"{v[0]}__gte": v[2]})
            elif v[1] == '<':
                db = db.filter(**{f"{v[0]}__lt": v[2]})
            elif v[1] == '<=':
                db = db.filter(**{f"{v[0]}__lte": v[2]})
            elif v[1] == '<>':
                db = db.exclude(**{v[0]: v[2]})
                
    if 'where_in' in condition:
        for k,v in condition['where_in'].items():
            db = db.filter(**{f"{k}__in": v})

    if 'order' in condition:
        order_by_args = []
        for k, v in condition['order'].items():
            if v == 'asc':
                order_by_args.append(k)
            else:
                order_by_args.append(f"-{k}")
        db = db.order_by(*order_by_args)

    if len(fields) > 0:
        db = db.values(*fields)

    article = db.get()
    return article



def get_articles(type , condition = {}, fields = [] , page = 1, pageSize = 15):
    startSize = pageSize * (page - 1)

    db = get_table_object(type).objects

    if 'where' in condition:
        for v in condition['where']:
            if v[1] == '=':
                db = db.filter(**{v[0]: v[2]})
            elif v[1] == '>':
                db = db.filter(**{f"{v[0]}__gt": v[2]})
            elif v[1] == '>=':
                db = db.filter(**{f"{v[0]}__gte": v[2]})
            elif v[1] == '<':
                db = db.filter(**{f"{v[0]}__lt": v[2]})
            elif v[1] == '<=':
                db = db.filter(**{f"{v[0]}__lte": v[2]})
            elif v[1] == '<>':
                db = db.exclude(**{v[0]: v[2]})
                

    if 'where_in' in condition:
        for k,v in condition['where_in'].items():
            db = db.filter(**{f"{k}__in": v})

    if 'order' in condition:
        order_by_args = []
        for k, v in condition['order'].items():
            if v == 'asc':
                order_by_args.append(k)
            else:
                order_by_args.append(f"-{k}")
        db = db.order_by(*order_by_args)

    if len(fields) > 0:
        db = db.values(*fields)

    articles = db[startSize:startSize+pageSize]

    return articles


def get_articles_list(type ,condition = {}, fields = [] , page = 1, pageSize = 15):
    startSize = pageSize * (page - 1)
    print(condition)
    db = get_table_object(type).objects

    if 'where' in condition:
        for v in condition['where']:
            if v[1] == '=':
                db = db.filter(**{v[0]: v[2]})
            elif v[1] == '>':
                db = db.filter(**{f"{v[0]}__gt": v[2]})
            elif v[1] == '>=':
                db = db.filter(**{f"{v[0]}__gte": v[2]})
            elif v[1] == '<':
                db = db.filter(**{f"{v[0]}__lt": v[2]})
            elif v[1] == '<=':
                db = db.filter(**{f"{v[0]}__lte": v[2]})
            elif v[1] == '<>':
                db = db.exclude(**{v[0]: v[2]})
                

    if 'where_in' in condition:
        for k,v in condition['where_in'].items():
            db = db.filter(**{f"{k}__in": v})

    if 'order' in condition:
        order_by_args = []
        for k, v in condition['order'].items():
            if v == 'asc':
                order_by_args.append(k)
            else:
                order_by_args.append(f"-{k}")
        db = db.order_by(*order_by_args)

    total = db.count()

    if len(fields) > 0:
        db = db.values(*fields)

    sql_query = str(db.query)
    # 打印 SQL 查询
    print(sql_query)

    articles = db[startSize:startSize+pageSize]

    return {'list':articles,'total':total}

'''
编辑文章
'''
def edit_article_content(type , article_id , data , where):
    index = article_id // 4000
    db = db = get_table_object(type).objects
    for k,v in where.items():
        db = db.filter(**{k: v})
    return db.update(**data)
    



def get_content_all(type , list):
    contentArr = {}
    tableIndex = qiu.utils.get_content_table_index(qiu.utils.array_column(list, 'is_mul_page' , 'article_id' ))
    if len(tableIndex[0]) >0:
        for index,article_ids in tableIndex[0].items():
            tmpData = get_article_content_arr(type , 0 ,index ,article_ids)
            temp = {item['article_id']: item for item in tmpData}
            contentArr = {**contentArr , **temp}

    if len(tableIndex[1]) >0:
        for index,article_ids in tableIndex[1].items():
            tmpData = get_article_content_arr(type , 1 ,index ,article_ids)
            temp = {item['article_id']: item for item in tmpData}
            contentArr = {**contentArr , **temp}

    for item in list:
        item['desc'] = qiu.utils.get_info(contentArr[item['article_id']]['content'])
        if item['cover'] == '':
            item['cover'] = qiu.utils.get_cover(contentArr[item['article_id']]['content'])

    return list



def get_article_content_arr(type , is_mul_page ,index , article_ids):
    if is_mul_page == 0:
        db = TsContentArticle.set_db_table(index).objects.using(get_db(type))
        db = db.filter(article_id__in=article_ids).values(*['article_id','content'])

    if is_mul_page == 1:
        db = TsContentArticleMul.set_db_table(index).objects.using(get_db(type))
        db = db.filter(page_num=1).filter(article_id__in=article_ids).values(*['article_id','content'])

    data = db
    return data


def get_article_content(type , article_id):
    index = article_id // 4000
    db = TsContentArticle.set_db_table(index).objects.using(get_db(type))
    db = db.filter(article_id =article_id)
    data = db.get()
    return data


def get_article_content_mul(type , article_id , page = 1):
    index = article_id // 50000
    db = TsContentArticleMul.set_db_table(index).objects.using(get_db(type))
    db = db.filter(article_id =article_id)
    db = db.filter(page_num =page)
    data = db.get()
    return data


def get_article_content_mul_count(type , article_id):
    index = article_id // 50000
    db = TsContentArticleMul.set_db_table(index).objects.using(get_db(type))
    db = db.filter(article_id =article_id)
    return db.count()