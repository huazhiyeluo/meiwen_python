from index.models import TsWeibo,TsWeiboComment

##################################微博管理##############################

def get_weibo(condition = {}, fields = [] ):

    db = TsWeibo.objects

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

    weibo = db.get()
    return weibo


def get_weibos(condition = {}, fields = [] , page = 1, pageSize = 15):
    startSize = pageSize * (page - 1)

    db = TsWeibo.objects

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

    weibos = db[startSize:startSize+pageSize]

    return weibos


def get_weibos_list(condition = {}, fields = [] , page = 1, pageSize = 15):
    startSize = pageSize * (page - 1)

    db = TsWeibo.objects

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

    weibos = db[startSize:startSize+pageSize]

    return {'list':weibos,'total':total}


##################################微博评论管理##############################

def get_weibo_comments_list(condition = {}, fields = [] , page = 1, pageSize = 15):
    startSize = pageSize * (page - 1)

    db = TsWeiboComment.objects

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

    weibos = db[startSize:startSize+pageSize]

    return {'list':weibos,'total':total}