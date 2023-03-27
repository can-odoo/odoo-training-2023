from odoo import http

class FranchiseRout(http.Controller):
    
    @http.route(['/store','/store/page/<int:page>'],auth="public",website=True )
    def index(self,page=1,location="",**kw):
        
        pp = 6
        filter=[]
        if location!="":
            filter = [('location','ilike',location)]
        store = http.request.env["franchise.store.property"].search(filter,offset=(page-1)*pp,limit=6)
        total_store=store.search_count(filter)

        pager = http.request.website.pager(
            url="/store",
            total=total_store,
            page=page,
            step=pp,
            url_args={'location':location}
        )
        return http.request.render("franchise_ERP.index_website",{
            "stores":store,
            "pager":pager
        })
    
    @http.route('/store/<model("franchise.store.property"):store>',auth="public",website=True)
    def StoreProperty(self,store,**kw):
        return http.request.render("franchise_ERP.store_properties_website",{
            "store":store
        })
