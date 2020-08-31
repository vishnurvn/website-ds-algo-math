from flask import Blueprint, render_template

ds = Blueprint('data_structs', __name__, template_folder='templates',
               static_folder='static')


@ds.route('/datastructures')
def ds_home():
    return render_template('ds_main.html')
