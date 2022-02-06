
from flask_admin import AdminIndexView, expose
from flask import redirect, url_for
from flask_login import current_user

from project.setup_ import defaults as d

class AdminIndex(AdminIndexView):
    @expose('/')
    def index(self):
        if current_user.is_anonymous:
            return redirect(url_for("index.page"))
        if current_user.id != d.Admin.id:
            return redirect(url_for("index.page"))

        
        return self.render('admin/index.html')
        