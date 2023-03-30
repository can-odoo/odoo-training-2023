from odoo import http
from odoo.addons.portal.controllers.portal import pager as portal_pager


class Property(http.Controller):

    @http.route(['/properties/','/properties/page/<int:page>'], auth='public', website=True)
    def index(self, page=1, search="", **kw):

        filter = [("state","in",["new","offer_received"])]
        if(search!=""):
            filter.append(('date_availability','>',search))

        Properties = http.request.env['estate.property'].search(filter,limit=6,offset=(page-1)*6)

        property_count = Properties.search_count([])
        pager = http.request.website.pager(
            url="/properties",
            total=property_count,
            page=page,
            step=6,
            url_args={'search':search}
        )

        return http.request.render('estate.index', {
            'properties': Properties,
            'pager':pager
         })
    
    @http.route('/<model("estate.property"):property>/', auth='public', website=True)
    def property(self, property):
        return http.request.render('estate.details', {
            'property': property
        })
    
    @http.route("/offers/<model('estate.property'):property>",auth="public",website="True")
    def offers(self,property):

        offer = http.request.env['estate.property.offer'].search([('property_id','=',property.id)])
        return http.request.render("estate.property_offers", {
            'offers': offer
        })
