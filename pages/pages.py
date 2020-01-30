from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

import json

from functions import app
from functions.connect_to import getConnection
from models import User
from sqlalchemy import create_engine

@app.route('/dashboard', methods=['GET'])
def dashboard():

    login_user(User.query.get(1))

    args = {
            'gift_card_eligible': True,
            'cashout_ok': True,
            'user_below_silver': current_user.is_below_tier('Silver'),
    }
    return render_template("dashboard.html", **args)

@app.route('/community', methods=['GET'])
def community():

    login_user(User.query.get(1))

    settings = getConnection('access')
    url = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (settings['user'], settings['password'], settings['host'], settings['port'], settings['database'])
    engine = create_engine(url)

    result = []
    with engine.connect() as con:
        sql = ('SELECT u.display_name, u.tier, u.point_balance, '
               'GROUP_CONCAT(rum.attribute SEPARATOR ", ") AS phones FROM '
               'user u LEFT JOIN rel_user_multi rum ON u.user_id = rum.user_id '
               'GROUP BY u.user_id, u.display_name, u.tier, u.point_balance '
               'ORDER BY u.user_id DESC LIMIT 5')
        query = con.execute(sql)
        result = [(dict(row.items())) for row in query]

    results = {'result': result}

    return render_template("community.html", **results)
