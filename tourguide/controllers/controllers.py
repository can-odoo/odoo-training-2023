from odoo import http
# from odoo.addons.portal.controllers.portal import pager as portal_pager


class TOurGuide(http.Controller):

    @http.route(['/tours/', '/tours/page/<int:page>'], auth='public', website=True)
    def index(self, page=1, **kw):
        domain = [('status', '=', 'available')]
        Property = http.request.env['tour.guide']
        count = Property.search_count([])
        print(count)
        pager = http.request.website.pager(
            url='/tours/',
            total=count,
            page=page,
            url_args={'filterDate': kw.get('filterDate')},
            step=6,
        )
        return http.request.render('tourguide.tour_view', {
            'tours': Property.search(domain, limit=6, offset=pager['offset']),
            'pager': pager,
        })

    @http.route('/tours/<model("tour.guide"):tour>/', auth='public', website=True)
    def teacher(self, tour):
        return http.request.render('tourguide.tour_detail', {
            'details': tour
        })
