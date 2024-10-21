from index.models import TsUserInfo
from django.core.cache import cache
from django.conf import settings


def get_user_info(uid , isUpdate = False):
    cacheKey = "CACHE_USER_IFNO_%d" % uid
    userInfo = cache.get(cacheKey)
    if userInfo is None or isUpdate:
        tempUserInfo = TsUserInfo.objects.get(uid=uid)
        userInfo = {
            'uid': tempUserInfo.uid,
            'username': tempUserInfo.username,
            'photo': tempUserInfo.photo,
        }
        if userInfo['photo'] == '':
            userInfo['photo'] = "%simage/user_large.png" % settings.STATIC_URL
        cache.set(cacheKey, userInfo, 24 * 3600)
    return userInfo