from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def inventory():
    return render_template('inventory.html')