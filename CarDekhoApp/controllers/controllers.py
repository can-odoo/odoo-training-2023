from odoo import http
from odoo.addons.portal.controllers.portal import pager as portal_pager

class controlller(http.Controller):

    @http.route(['/car/','/car/page/<int:page>'], auth='public', website=True, type="http")
    def index(self, page=1, **kw):
        Cars = http.request.env['car.dekho.property'].search([('state','=','new')],limit=5,offset=(page-1)*5)
        pageCount = Cars.search_count([('state','in',['new','offer_received'])])

        pager = portal_pager(
            url="/car",
            total = pageCount,
            page = page,
            step = 5,
        )

        return http.request.render('CarDekhoApp.car_name_template',{
            'cars':Cars,
            'pager':pager,
            'page':page,
        })
    
    @http.route("/car/<model('car.dekho.property'):car>/", website=True, auth='public')
    def details_car(self,car):
        return http.request.render('CarDekhoApp.car_details_template',{
            'car':car,
        })