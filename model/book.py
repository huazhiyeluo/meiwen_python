from index.models import TsBook,TsBookChapter
from index.models_book import TsContent

##################################书籍管理##############################

def get_book(condition = {}, fields = [] ):

    db = TsBook.objects

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

    book = db.get()
    return book


def get_books(condition = {}, fields = [] , page = 1, pageSize = 15):
    startSize = pageSize * (page - 1)

    db = TsBook.objects

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

    books = db[startSize:startSize+pageSize]

    return books


def get_books_list(condition = {}, fields = [] , page = 1, pageSize = 15):
    startSize = pageSize * (page - 1)

    db = TsBook.objects

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

    books = db[startSize:startSize+pageSize]

    return {'list':books,'total':total}


def add_book(data = {}):
    db = TsBook.objects
    return db.create(**data) 

    return db.update(**data)

def edit_book(data = {},where = {}):
    db = TsBook.objects
    for field,val in where.items():
        db = db.filter(**{field: val})

    return db.update(**data)

def del_book(where = {}):
    db = TsBook.objects
    for field,val in where.items():
        db = db.filter(**{field: val})

    return db.delete()


##################################书籍章节管理##############################
def get_book_chapter(condition = {}, fields = [] ):

    db = TsBookChapter.objects

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

    chapter = db.first()
    return chapter



def get_book_chapters(condition = {}, fields = [] , page = 1, pageSize = 15):
    startSize = pageSize * (page - 1)

    db = TsBookChapter.objects

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

    chapters = db[startSize:startSize+pageSize]

    return chapters


def get_chapter_content(link_id):
    TsContent().set_db_table(link_id // 4000)  # 设置动态表名
    db = TsContent.objects.using('book')
    db = db.filter(link_id =link_id)

    sql_query = str(db.query)
    # 打印 SQL 查询
    print(sql_query)

    chapter_content = db.get()
    return chapter_content
