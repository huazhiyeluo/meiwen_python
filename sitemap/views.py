from django.shortcuts import render
import qiu.utils
import qiu.common
# Create your views here.

def index(request):
    data          = {}
    data['controller'] = 'index'

    newCategorys = {}
    for type in [1,2,3,4]:
        tempAllCategorys = qiu.utils.get_categorys_by_type(type)

        

        newCategorys[type] = {}
        newCategorys[type]['name'] = qiu.utils.get_first_name(type)
        newCategorys[type]['data'] = {}
        for pcid , v in tempAllCategorys['pCategorys'].items():
            
            newCategorys[type]['data'][pcid] = v
            newCategorys[type]['data'][pcid]['child'] = []
            for cid,val in tempAllCategorys['cCategorys'].items():
                if val['pcid'] == pcid:
                    newCategorys[type]['data'][pcid]['child'].append(val)

    data['newCategorys'] = newCategorys

    initData = qiu.common.get_init_data(request)
    initData['seo'] = qiu.common.share_seo(initData['seo'], "站点地图")
    data = {**data,**initData}

    return render(request, 'sitemap/index.html', data)