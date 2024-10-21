# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TsArticleGushi(models.Model):
    article_id = models.AutoField(primary_key=True, db_comment='文章ID')
    uid = models.IntegerField(db_comment='用户ID')
    cid1 = models.SmallIntegerField(db_comment='分类ID')
    cid2 = models.SmallIntegerField(db_comment='子分类ID')
    title = models.CharField(max_length=100, db_comment='标题')
    tags = models.CharField(max_length=50, db_comment='标签')
    cover = models.CharField(max_length=100, db_comment='图片路径')
    count_comment = models.SmallIntegerField(db_comment='评论数')
    count_view = models.SmallIntegerField(db_comment='浏览数')
    is_recommend = models.IntegerField(db_comment='是否推荐')
    is_audit = models.IntegerField(db_comment='是否审核')
    is_mul_page = models.IntegerField(db_comment='是否多页')
    addtime = models.IntegerField(db_comment='新增时间')

    class Meta:
        managed = False
        db_table = 'ts_article_gushi'
        db_table_comment = '文章'


class TsArticleMeiwen(models.Model):
    article_id = models.AutoField(primary_key=True, db_comment='文章ID')
    uid = models.IntegerField(db_comment='用户ID')
    cid1 = models.SmallIntegerField(db_comment='分类ID')
    cid2 = models.SmallIntegerField(db_comment='子分类ID')
    title = models.CharField(max_length=100, db_comment='标题')
    tags = models.CharField(max_length=50, db_comment='标签')
    cover = models.CharField(max_length=100, db_comment='图片路径')
    count_comment = models.SmallIntegerField(db_comment='评论数')
    count_view = models.SmallIntegerField(db_comment='浏览数')
    is_recommend = models.IntegerField(db_comment='是否推荐')
    is_audit = models.IntegerField(db_comment='是否审核')
    is_mul_page = models.IntegerField(db_comment='是否多页')
    addtime = models.IntegerField(db_comment='新增时间')

    class Meta:
        managed = False
        db_table = 'ts_article_meiwen'
        db_table_comment = '文章'


class TsArticleZuowen(models.Model):
    article_id = models.AutoField(primary_key=True, db_comment='文章ID')
    uid = models.IntegerField(db_comment='用户ID')
    cid1 = models.SmallIntegerField(db_comment='分类ID')
    cid2 = models.SmallIntegerField(db_comment='子分类ID')
    title = models.CharField(max_length=100, db_comment='标题')
    tags = models.CharField(max_length=50, db_comment='标签')
    cover = models.CharField(max_length=100, db_comment='图片路径')
    count_comment = models.SmallIntegerField(db_comment='评论数')
    count_view = models.SmallIntegerField(db_comment='浏览数')
    is_recommend = models.IntegerField(db_comment='是否推荐')
    is_audit = models.IntegerField(db_comment='是否审核')
    is_mul_page = models.IntegerField(db_comment='是否多页')
    addtime = models.IntegerField(db_comment='新增时间')

    class Meta:
        managed = False
        db_table = 'ts_article_zuowen'
        db_table_comment = '文章'


class TsBook(models.Model):
    book_id = models.AutoField(primary_key=True, db_comment='书本ID')
    uid = models.IntegerField(db_comment='创建者uid')
    cid1 = models.SmallIntegerField(db_comment='分类ID')
    cid2 = models.SmallIntegerField(db_comment='子分类ID')
    title = models.CharField(max_length=100, db_comment='名称')
    author = models.CharField(max_length=50, db_comment='作者')
    cover = models.CharField(max_length=255, db_comment='图片')
    desc = models.CharField(max_length=2000, db_comment='描述')
    tags = models.CharField(max_length=128, db_comment='标签')
    count_comment = models.SmallIntegerField(db_comment='评论数')
    count_view = models.SmallIntegerField(db_comment='浏览数')
    is_recommend = models.IntegerField(db_comment='是否推荐')
    meta_title = models.CharField(max_length=50, db_comment='SEO的网页标题')
    meta_keywords = models.CharField(max_length=255, db_comment='关键字')
    meta_description = models.CharField(max_length=255, db_comment='描述')
    addtime = models.IntegerField(db_comment='新增时间')

    class Meta:
        managed = False
        db_table = 'ts_book'
        db_table_comment = '书名'


class TsBookChapter(models.Model):
    link_id = models.AutoField(primary_key=True, db_comment='关联ID')
    chapter_id = models.SmallIntegerField(db_comment='章节ID')
    book_id = models.SmallIntegerField(db_comment='书本ID')
    title = models.CharField(max_length=100, db_comment='标题')
    tags = models.CharField(max_length=50, db_comment='标签')
    count_comment = models.SmallIntegerField(db_comment='评论数')
    count_view = models.SmallIntegerField(db_comment='浏览数')
    addtime = models.IntegerField(db_comment='新增时间')

    class Meta:
        managed = False
        db_table = 'ts_book_chapter'
        unique_together = (('chapter_id', 'book_id'),)
        db_table_comment = '小说章节表'


class TsCategory(models.Model):
    cid = models.SmallAutoField(primary_key=True, db_comment='分类ID')
    pcid = models.SmallIntegerField(db_comment='上级ID')
    type = models.SmallIntegerField(db_comment='1书本 2美文 3故事 4作文')
    title = models.CharField(max_length=20, db_comment='分类名称')
    spider_title = models.CharField(max_length=20, db_comment='分类名称(爬虫)')
    route_name = models.CharField(max_length=50, db_comment='路由名称')
    spider_route_name = models.CharField(max_length=50, db_comment='路由名称(爬虫)')
    meta_title = models.CharField(max_length=50, db_comment='SEO的网页标题')
    meta_keywords = models.CharField(max_length=255, db_comment='关键字')
    meta_description = models.CharField(max_length=255, db_comment='描述')
    sort = models.SmallIntegerField(db_comment='排序')
    is_delete = models.SmallIntegerField(db_comment='0 正常 1 删除')

    class Meta:
        managed = False
        db_table = 'ts_category'
        db_table_comment = '文章分类'


class TsComment(models.Model):
    comment_id = models.AutoField(primary_key=True, db_comment='评论ID')
    article_id = models.IntegerField(db_comment='文章ID')
    type = models.IntegerField(db_comment='类型 1图书 2美文 3故事 4作文')
    uid = models.IntegerField(db_comment='用户ID')
    content = models.TextField(db_comment='评论内容')
    addtime = models.IntegerField(db_comment='评论时间')
    is_audit = models.IntegerField(db_comment='是否审核')

    class Meta:
        managed = False
        db_table = 'ts_comment'
        db_table_comment = '文章评论'


class TsLinks(models.Model):
    link_id = models.AutoField(primary_key=True, db_comment='友链ID')
    sitename = models.CharField(max_length=100, db_comment='站点名')
    url = models.CharField(max_length=100, db_comment='链接地址')
    keywords = models.CharField(max_length=100, db_comment='关键字')
    start_time = models.IntegerField(db_comment='开始时间')
    end_time = models.IntegerField(db_comment='结束时间')
    sort = models.SmallIntegerField(db_comment='排序')
    is_delete = models.IntegerField(db_comment='是否删除 0 默认 1删除')

    class Meta:
        managed = False
        db_table = 'ts_links'
        db_table_comment = '友链管理'


class TsTag(models.Model):
    tag_id = models.AutoField(primary_key=True, db_comment='自增ID')
    tagname = models.CharField(unique=True, max_length=32, db_comment='标签名称')
    count_user = models.IntegerField(db_comment='统计用户标签')
    count_book = models.IntegerField(db_comment='统计书籍标签')
    count_book_chapter = models.IntegerField(db_comment='统计书籍章节标签')
    count_weibo = models.IntegerField(db_comment='统计书籍章节标签')
    count_article = models.IntegerField(db_comment='统计文章标签')
    is_enable = models.IntegerField(db_comment='是否可用')
    uptime = models.IntegerField(db_comment='更新时间')

    class Meta:
        managed = False
        db_table = 'ts_tag'
        db_table_comment = '标签表'


class TsTagArticleIndex(models.Model):
    article_id = models.IntegerField(db_comment='帖子ID')
    tag_id = models.IntegerField(db_comment='标签ID')

    class Meta:
        managed = False
        db_table = 'ts_tag_article_index'
        unique_together = (('article_id', 'tag_id'),)
        db_table_comment = '文章标签关联'


class TsTagBookChapterIndex(models.Model):
    chapter_id = models.IntegerField(db_comment='帖子ID')
    tag_id = models.IntegerField(db_comment='标签ID')

    class Meta:
        managed = False
        db_table = 'ts_tag_book_chapter_index'
        unique_together = (('chapter_id', 'tag_id'),)
        db_table_comment = '书籍章节标签关联'


class TsTagBookIndex(models.Model):
    book_id = models.IntegerField(db_comment='帖子ID')
    tag_id = models.IntegerField(db_comment='标签ID')

    class Meta:
        managed = False
        db_table = 'ts_tag_book_index'
        unique_together = (('book_id', 'tag_id'),)
        db_table_comment = '书籍标签关联'


class TsTagUserIndex(models.Model):
    uid = models.IntegerField(db_comment='用户ID')
    tag_id = models.IntegerField(db_comment='标签ID')

    class Meta:
        managed = False
        db_table = 'ts_tag_user_index'
        unique_together = (('uid', 'tag_id'),)
        db_table_comment = '用户标签关联'


class TsTagWeiboIndex(models.Model):
    weibo_id = models.IntegerField(db_comment='帖子ID')
    tag_id = models.IntegerField(db_comment='标签ID')

    class Meta:
        managed = False
        db_table = 'ts_tag_weibo_index'
        unique_together = (('weibo_id', 'tag_id'),)
        db_table_comment = '书籍标签关联'


class TsUser(models.Model):
    openid = models.CharField(unique=True, max_length=64, db_comment='openid')
    email = models.CharField(max_length=64, db_comment='用户email')
    phone = models.CharField(max_length=64, db_comment='手机号')
    password = models.CharField(max_length=32, db_comment='用户密码')
    salt = models.CharField(max_length=32, db_comment='加点盐')
    code = models.CharField(max_length=32, db_comment='邮箱验证码')

    class Meta:
        managed = False
        db_table = 'ts_user'
        db_table_comment = 'ts用户'


class TsUserFollow(models.Model):
    uid = models.IntegerField(db_comment='用户ID')
    uid_follow = models.IntegerField(db_comment='被关注的用户ID')
    addtime = models.IntegerField(db_comment='添加时间')

    class Meta:
        managed = False
        db_table = 'ts_user_follow'
        unique_together = (('uid', 'uid_follow'),)
        db_table_comment = '用户关注跟随'


class TsUserGb(models.Model):
    reid = models.IntegerField(db_comment='回复留言ID')
    uid = models.IntegerField(db_comment='留言用户ID')
    touid = models.IntegerField(db_comment='被留言用户ID')
    content = models.TextField(db_comment='内容')
    addtime = models.IntegerField(db_comment='新增时间')

    class Meta:
        managed = False
        db_table = 'ts_user_gb'
        db_table_comment = '留言表'


class TsUserInfo(models.Model):
    uid = models.IntegerField(primary_key=True,unique=True, db_comment='用户ID')
    roleid = models.SmallIntegerField(db_comment='角色ID')
    username = models.CharField(max_length=32, db_comment='用户名')
    gender = models.IntegerField(db_comment='性别 1男 2女 0 未知')
    email = models.CharField(max_length=64, db_comment='Email邮箱')
    phone = models.CharField(max_length=11, db_comment='电话号码')
    photo = models.CharField(max_length=100, db_comment='头像')
    signed = models.CharField(max_length=100, db_comment='签名')
    address = models.CharField(max_length=64, db_comment='地址')
    blog = models.CharField(max_length=32, db_comment='博客')
    about = models.CharField(max_length=255, db_comment='关于我')
    allscore = models.IntegerField(db_comment='所有获得的总积分')
    count_score = models.IntegerField(db_comment='统计积分')
    count_follow = models.IntegerField(db_comment='统计用户跟随的')
    count_followed = models.IntegerField(db_comment='统计用户被跟随的')
    is_admin = models.IntegerField(db_comment='是否是管理员')
    is_audit = models.IntegerField(db_comment='是否审核')
    is_verify = models.IntegerField(db_comment='0未验证1验证')
    is_verifyphone = models.IntegerField(db_comment='手机号验证0未验证1验证')
    is_renzheng = models.IntegerField(db_comment='是否认证0未认证1认证')
    is_recommend = models.IntegerField(db_comment='是否推荐')
    reg_time = models.IntegerField(db_comment='注册时间')
    reg_ip = models.CharField(max_length=32, db_comment='注册IP')
    login_time = models.IntegerField(db_comment='登陆时间')
    login_ip = models.CharField(max_length=32, db_comment='登陆IP')

    class Meta:
        managed = False
        db_table = 'ts_user_info'
        db_table_comment = '用户信息'


class TsUserOpen(models.Model):
    uid = models.AutoField(primary_key=True, db_comment='用户ID')
    sid = models.IntegerField(db_comment='连接网站（0.普通注册 1.QQ | 2.微博 |3百度）')
    openid = models.CharField(max_length=64, db_comment='openid')
    access_token = models.CharField(max_length=128, db_comment='access_token')
    uptime = models.IntegerField(db_comment='更新时间')

    class Meta:
        managed = False
        db_table = 'ts_user_open'
        unique_together = (('sid', 'openid'), ('uid', 'sid'),)
        db_table_comment = '连接登录Open设置'


class TsWeibo(models.Model):
    weibo_id = models.AutoField(primary_key=True, db_comment='自增唠叨ID')
    uid = models.IntegerField(db_comment='用户ID')
    content = models.TextField(db_comment='内容')
    count_comment = models.IntegerField(db_comment='评论数')
    photo = models.CharField(max_length=100, db_comment='图片')
    is_audit = models.IntegerField(db_comment='是否审核')
    addtime = models.IntegerField(blank=True, null=True, db_comment='新增时间')
    uptime = models.IntegerField(db_comment='最后更新时间')

    class Meta:
        managed = False
        db_table = 'ts_weibo'
        db_table_comment = '唠叨'


class TsWeiboComment(models.Model):
    commentid = models.AutoField(primary_key=True, db_comment='自增评论ID')
    weibo_id = models.IntegerField(db_comment='唠叨ID')
    uid = models.IntegerField(db_comment='用户ID')
    touid = models.IntegerField(db_comment='回复用户ID')
    content = models.TextField(db_comment='内容')
    is_read = models.IntegerField(db_comment='是否已阅')
    is_audit = models.IntegerField(db_comment='是否审核')
    addtime = models.IntegerField(db_comment='新增时间')

    class Meta:
        managed = False
        db_table = 'ts_weibo_comment'
        db_table_comment = '唠叨回复'
