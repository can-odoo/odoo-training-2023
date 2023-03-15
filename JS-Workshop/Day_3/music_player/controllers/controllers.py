# -*- coding: utf-8 -*-
from odoo import http
import json


class MusicPlayer(http.Controller):
     @http.route('/music', auth='public')
     def index(self, **kw):
        return http.request.render('music_player.music_template')

     @http.route('/music/search', auth='public')
     def list(self, **kw):
         print(http.request.env["music_player.music_player"].read())
         return http.request.env["music_player.music_player"]


#     @http.route('/music_player/music_player/objects/<model("music_player.music_player"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('music_player.object', {
#             'object': obj
#         })
