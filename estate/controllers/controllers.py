from odoo import http


class EstateRout(http.Controller):
    @http.route(['/property','/property/page/<int:page>'], auth='public', website="True")
    def index(self,page=1,search="",**kw):

        pp=6
        filter=[("state", "in", ["new", "offer_received"])]
        if(search!=""):
            filter.append(('date_availability','>',search))

        property = http.request.env['estate.property'].search(filter,limit=pp,offset=(page-1)*pp)
        property_count = property.search_count(filter)

        pager = http.request.website.pager(
            url="/property",
            total=property_count,
            page=page,
            step=pp,
            url_args={'search':search}
        )
        return http.request.render("estate.index", {"property":property,'pager':pager})

    @http.route('/property/<model("estate.property"):property>', auth="public", website="True")
    def propertyDetails(self, property):

        return http.request.render("estate.property_details", {
            "property": property
        })

    @http.route("/property/offers/<model('estate.property'):property>",auth="public",website="True")
    def offers(self,property):
       
        offer = http.request.env['estate.property.offer'].search([('property_id','=',property.id)])
        return http.request.render("estate.property_offers", {
            "offers": offer
        })