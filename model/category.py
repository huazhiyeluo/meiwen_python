from index.models import TsCategory

##################################微博管理##############################

def get_category(condition = {}, fields = [] ):

    db = TsCategory.objects

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

    category = db.get()
    return category