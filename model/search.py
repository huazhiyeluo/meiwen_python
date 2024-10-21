from django.db import connection


def get_search_all(keyword, page, pageSize):

    where = '1 = 1'
    if keyword != '':
        where = ' title like \'%' + keyword + '%\''

    limit = '%d,%d' % ((page - 1) * pageSize , pageSize);

    sql1 = "select book_id as id,0 as b_id,cid1,cid2,title,`addtime`,count_view as num,1 as `oid` from ts_book where  %s " % where;
    sql5 = "select chapter_id as id,book_id as b_id,0 as `cid1`,0 as `cid2`,title,`addtime`,count_view as num,5 as `oid` from ts_book_chapter where %s " % where;
    sql2 = "select article_id as id,0 as b_id,cid1,cid2,title,`addtime`,count_view as num,2 as `oid` from ts_article_meiwen where is_audit = 1 and  %s " % where;
    sql3 = "select article_id as id,0 as b_id,cid1,cid2,title,`addtime`,count_view as num,3 as `oid` from ts_article_gushi where is_audit = 1 and  %s " % where;
    sql4 = "select article_id as id,0 as b_id,cid1,cid2,title,`addtime`,count_view as num,4 as `oid` from ts_article_zuowen where is_audit = 1 and  %s " % where;

    sql = "%s union %s union %s union %s union %s order by addtime desc limit %s" % (sql1, sql2, sql3, sql4 ,sql5 , limit);
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]


    sqlCount1 = "select book_id as id from ts_book where %s " % where;
    sqlCount5 = "select chapter_id as id from ts_book_chapter where  %s " % where;
    sqlCount2 = "select article_id as id from ts_article_meiwen where is_audit = 1 and  %s " % where;
    sqlCount3 = "select article_id as id from ts_article_gushi where is_audit = 1 and  %s " % where;
    sqlCount4 = "select article_id as id from ts_article_zuowen where is_audit = 1 and  %s " % where;

    sqlCount = "select count(*) as num from (%s union %s union %s union %s union %s) as a" %(sqlCount1, sqlCount2, sqlCount3, sqlCount4, sqlCount5)
    with connection.cursor() as cursor:
        cursor.execute(sqlCount)
        result = cursor.fetchone() 
        total = result[0]  

    return {'list':rows,'total':total}


def get_search_book(keyword, page, pageSize):

    where = '1 = 1'
    if keyword != '':
        where = ' title like \'%' + keyword + '%\''

    limit = '%d,%d' % ((page - 1) * pageSize , pageSize);

    sql1 = "select book_id as id,0 as b_id,cid1,cid2,title,`addtime`,count_view as num,1 as `oid` from ts_book where  %s " % where;
    sql5 = "select chapter_id as id,book_id as b_id,0 as `cid1`,0 as `cid2`,title,`addtime`,count_view as num,5 as `oid` from ts_book_chapter where %s " % where;

    sql = "%s union %s order by addtime desc limit %s" % (sql1, sql2 , limit);
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]


    sqlCount1 = "select book_id as id from ts_book where %s " % where;
    sqlCount5 = "select chapter_id as id from ts_book_chapter where  %s " % where;

    sqlCount = "select count(*) as num from (%s union %s) as a" %(sqlCount1, sqlCount2)
    with connection.cursor() as cursor:
        cursor.execute(sqlCount)
        result = cursor.fetchone() 
        total = result[0]  

    return {'list':rows,'total':total}


def get_search_meiwen(keyword, page, pageSize):

    where = '1 = 1'
    if keyword != '':
        where = ' title like \'%' + keyword + '%\''

    limit = '%d,%d' % ((page - 1) * pageSize , pageSize);

    sql = "select article_id as id,0 as b_id,cid1,cid2,title,`addtime`,count_view as num,2 as `oid` from ts_article_meiwen where is_audit = 1 and  %s " % where;
    sql = "%s order by addtime desc limit %s" % (sql, limit);
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

    sqlCount = "select count(*) as num from ts_article_meiwen where is_audit = 1 and  %s " % where;
    with connection.cursor() as cursor:
        cursor.execute(sqlCount)
        result = cursor.fetchone() 
        total = result[0]  

    return {'list':rows,'total':total}

def get_search_gushi(keyword, page, pageSize):

    where = '1 = 1'
    if keyword != '':
        where = ' title like \'%' + keyword + '%\''

    limit = '%d,%d' % ((page - 1) * pageSize , pageSize);

    sql = "select article_id as id,0 as b_id,cid1,cid2,title,`addtime`,count_view as num,3 as `oid` from ts_article_gushi where is_audit = 1 and  %s " % where;
    sql = "%s order by addtime desc limit %s" % (sql, limit);
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

    sqlCount = "select count(*) as num from ts_article_gushi where is_audit = 1 and  %s " % where;
    with connection.cursor() as cursor:
        cursor.execute(sqlCount)
        result = cursor.fetchone() 
        total = result[0]  

    return {'list':rows,'total':total}


def get_search_zuowen(keyword, page, pageSize):

    where = '1 = 1'
    if keyword != '':
        where = ' title like \'%' + keyword + '%\''

    limit = '%d,%d' % ((page - 1) * pageSize , pageSize);

    sql = "select article_id as id,0 as b_id,cid1,cid2,title,`addtime`,count_view as num,4 as `oid` from ts_article_zuowen where is_audit = 1 and  %s " % where;
    sql = "%s order by addtime desc limit %s" % (sql, limit);
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

    sqlCount = "select count(*) as num from ts_article_zuowen where is_audit = 1 and  %s " % where;
    with connection.cursor() as cursor:
        cursor.execute(sqlCount)
        result = cursor.fetchone() 
        total = result[0]  

    return {'list':rows,'total':total}