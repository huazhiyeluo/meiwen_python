from django.shortcuts import render
from django.core.paginator import Paginator
import model.weibo
import model.user
import qiu.utils
import qiu.common
from qiu.mypage import MyPaper


# Create your views here.

# Create your views here.
def index(request , page = 1):

    size = 15

    data          = {}
    data['controller'] = 'weibo'

    #1、微博列表
    weibos = model.weibo.get_weibos_list({'where': [['is_audit','=',1]],'order':{'weibo_id':'desc'}},[],page,size)
    for weibo in weibos['list']:
        userInfo = model.user.get_user_info(weibo.uid)
        weibo.username = userInfo['username']
        weibo.photo = userInfo['photo']
        weibo.addtime = qiu.utils.time_tran(weibo.addtime)
        weibo.content = weibo.content.replace("\n", "<br />")

    paginator = MyPaper(page, size,weibos['total'])  # 10表示每页显示的项数
    data['list'] = weibos['list']
    data['page'] = paginator.create_links('weibo')

    #2、热门微博
    hotweibos = model.weibo.get_weibos({'where': [['is_audit','=',1]],'order':{'count_comment':'desc'}},[],1,30)
    for weibo in hotweibos:
        userInfo = model.user.get_user_info(weibo.uid)
        weibo.username = userInfo['username']
        weibo.photo = userInfo['photo']
        weibo.addtime = qiu.utils.time_tran(weibo.addtime)
        weibo.content = weibo.content.replace("\n", "<br />")

    data['hotweibos'] = hotweibos
        
    initData = qiu.common.get_init_data(request)
    initData['seo'] = qiu.common.share_seo(initData['seo'], '树洞_树洞_秘密,在这里看八卦闲聊、分享秘密' , '树洞,树洞网,秘密,爱嗨网' , '树洞是一个基于情感倾诉、烦恼咨询的多应用匿名社区网站,在这里，我们为您寄存秘密、心事。拨动你的心弦，倾听来自心海的回音！')
    data = {**data,**initData}
    
    return render(request, 'weibo/index.html', data)


def detail(request , weibo_id = 1 , page = 1):
    size = 12

    data          = {}
    data['controller'] = 'weibo'

    #1、微博详情
    weibo = model.weibo.get_weibo({'where': [['weibo_id','=',weibo_id]]},[])
    weibo.content = weibo.content.replace("\n", "<br />")
    weibo.addtime = qiu.utils.time_tran(weibo.addtime)
    data['weibo'] = weibo

    tuserInfo = model.user.get_user_info(weibo.uid)
    data['tuserInfo'] = tuserInfo

    #2、微博评论列表
    comments = model.weibo.get_weibo_comments_list({'where': [['weibo_id','=',weibo_id]],'order':{'commentid':'desc'}},[],page,size)
    for comment in comments['list']:
        userInfo = model.user.get_user_info(comment.uid)
        comment.username = userInfo['username']
        comment.photo = userInfo['photo']
        comment.addtime = qiu.utils.time_tran(comment.addtime)
        comment.content = comment.content.replace("\n", "<br />")

    paginator = MyPaper(page, size,comments['total'])  # 10表示每页显示的项数
    data['list'] = comments['list']
    data['page'] = paginator.create_links('weibo_detail',[weibo_id])

    #3、个人其他微博
    otherweibos = model.weibo.get_weibos({'where': [['is_audit','=',1],['weibo_id','<>',1]],'order':{'weibo_id':'desc'}},[],1,20)
    for weibo in otherweibos:
        weibo.addtime = qiu.utils.time_tran(weibo.addtime)
        weibo.content = qiu.utils.get_info(weibo.content,50)

    data['otherweibos'] = otherweibos

    initData = qiu.common.get_init_data(request)
    initData['seo'] = qiu.common.share_seo(initData['seo'], qiu.utils.get_info(weibo.content,25) , '树洞,树洞网,秘密,爱嗨网' , qiu.utils.get_info(weibo.content),tuserInfo['photo'])
    data = {**data,**initData}

    return render(request, 'weibo/detail.html', data)

def createdo(request):
    data          = {}
    return render(request, 'index/info.html', data)

def replydo(request):
    data          = {}
    return render(request, 'index/info.html', data)

def delete(request):
    data          = {}
    return render(request, 'index/info.html', data)