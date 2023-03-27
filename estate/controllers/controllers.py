from odoo import http
# from odoo.addons.portal.controllers.portal import pager as portal_pager


class Estate(http.Controller):

    @http.route(['/properties/', '/properties/page/<int:page>'], auth='public', website=True)
    def index(self, page=1, **kw):
        domain = [('state', 'in', ['offer_received', 'offer_accepted', 'new'])]
        Property = http.request.env['estate.property']
        count = Property.search_count([])
        if kw.get('inputdate'):
            domain = ['&', ('date_availability', '>', kw.get('inputdate')), ('state', 'in', [
                'offer_received', 'offer_accepted', 'new'])]

            count = Property.search_count(['&', ('date_availability', '>', kw.get(
                'inputdate')), ('state', 'in', ['offer_received', 'offer_accepted', 'new'])])
        print(count)
        pager = http.request.website.pager(
            url='/properties/',
            total=count,
            page=page,
            url_args={'filterDate': kw.get('filterDate')},
            step=6,
        )
        return http.request.render('estate.index', {
            'properties': Property.search(domain, limit=6, offset=pager['offset']),
            'pager': pager,
        })

    @http.route('/estate/<model("estate.property"):property>/', auth='public', website=True)
    def teacher(self, property):
        return http.request.render('estate.property_page', {
            'properties': property
        })
