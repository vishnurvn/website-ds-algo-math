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
        "display_name": "Linked List",
        "name": "linked_list",
        "gist": "361d250a135c165524d44ccdc7b7e128"
    }, {
        "display_name": "Double Linked List",
        "name": "double_linked_list",
        "gist": "e9c5e374a9f17d5536196283168d6758"
    }, {
        "display_name": "Queue",
        "name": "queue",
        "gist": "40ad8fa6bcd9d99348f1d334578307ce"
    }]
    return render_template('ds_main.html', data=data_structure)


@ds.route('/datastructures/<string:d_s>')
def test_route(d_s):
    gist_link = "https://gist.github.com/vishnurvn/{}.js".format(d_s)
    return render_template('data_structure_detail.html', link={
        "link": gist_link
    })