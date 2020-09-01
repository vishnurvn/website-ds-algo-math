from flask import Blueprint, render_template


ds = Blueprint('data_structs', __name__, template_folder='templates',
               static_folder='static')


@ds.route('/datastructures')
def ds_home():
    # item = mongo.db.data_structure.find_one()
    # data_structure = [{
    #     "name": item['display_name']
    # }]
    data_structure = [{
        "name": "Linked List"
    }]
    return render_template('ds_main.html', data=data_structure)
