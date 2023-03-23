from odoo import http
from odoo.addons.portal.controllers.portal import pager as portal_pager

class Properties(http.Controller):
    
    @http.route(['/properties/','/properties/page/<int:page>'], auth='public',website=True, type='http')
    def index(self, page=1, **kw):
        Properties = http.request.env['estate.recurring.plan'].search([('state','not in',['offer_accepted','sold','cancle'])],
                                                                limit=6,offset=(page-1)*6)
        pageCount = Properties.search_count([('state','not in',['offer_accepted','sold','cancle'])])    
        if kw.get('filterDate'):
            Properties = http.request.env['estate.recurring.plan'].search(['&',('date_availability', '>', kw.get('filterDate')),('state','not in',['offer_accepted','sold','cancle'])],
                                                                limit=6,offset=(page-1)*6)
            pageCount = Properties.search_count(['&',('date_availability', '>', kw.get('filterDate')),('state','not in',['offer_accepted','sold','cancle'])])
        # http.request.website.pager
        pager = portal_pager(
            url='/properties',
            total=pageCount,
            page=page,
            url_args={'filterDate':kw.get('filterDate')},
            step=6,
        )        
        return http.request.render('estate.properties_page_template',{
            'properties': Properties,
            'pager':pager,
            'page':page,
        })

    @http.route('/properties/<model("estate.recurring.plan"):property>/',auth='public', website=True)
    def details(self,property):
        return http.request.render('estate.properties_details',{
            'prop':property
        })
