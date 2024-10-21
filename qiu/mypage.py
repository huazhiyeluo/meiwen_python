from django.urls import reverse


class MyPaper:
    def __init__(self, page=1, page_size=15, total=0):
        self.page = page
        self.page_size = page_size
        self.total = total
        self.total_page = -(-total // page_size)  # 等同于 ceil(total / page_size)
        self.first = max(page - 2, 1)
        self.last = min(page + 2, self.total_page)

    def create_links(self, route_name, param = [], sep='_', fix=''):
        if self.total == 0:
            return ''

        if self.total_page == 1:
            return ''

        html = '<ul class="pagination justify-content-center pt-3">'
        
        if self.first > 1:
            url = self.get_link(route_name,param, sep, 1, fix)
            html += f'<li class="page-item"><a href="{url}" class="page-link"><span aria-hidden="true"><<</span></a></li>'
            url = self.get_link(route_name,param, sep, self.page - 1, fix)
            html += f'<li class="page-item"><a href="{url}" class="page-link"><span aria-hidden="true"><</span></a></li>'

        for i in range(self.first, self.last + 1):
            url = self.get_link(route_name,param, sep, i, fix)
            if self.page == i:
                html += f'<li class="page-item active"><a href="{url}" class="page-link">{i}</a></li>'
            else:
                html += f'<li class="page-item"><a href="{url}" class="page-link">{i}</a></li>'

        if self.page < self.last:
            url = self.get_link(route_name,param, sep, self.page + 1, fix)
            html += f'<li class="page-item"><a href="{url}" class="page-link"><span aria-hidden="true">></span></a></li>'
            url = self.get_link(route_name,param, sep, self.total_page, fix)
            html += f'<li class="page-item"><a href="{url}" class="page-link"><span aria-hidden="true">>></span></a></li>'
        
        html += '</ul>'
        return html

    def get_link(self, route_name, param, sep, page, fix=''):
        if page > 1:
            url = reverse(route_name + sep + 'list', args = param +[page])
        else:
            url = reverse(route_name, args = param)
        return url + fix
