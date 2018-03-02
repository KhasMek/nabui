import json

from app import app
from app import bettercap
from app.forms import CommandForm, LoginForm
from app.models import User
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password_hash(form.password.data):
            flash('Invalid Username or Password.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/events')
@login_required
def get_events():
    response = bettercap.get_events()
    logs = []
    endpoints_new = []
    endpoints_lost = []
    for message in response:
        if 'sys.log' in message['tag']:
            logs.append(message)
        elif 'endpoint.new' in message['tag']:
            endpoints_new.append(message)
        elif 'endpoint.lost' in message['tag']:
            endpoints_lost.append(message)
    return render_template('events.html', logs=logs, endpoints_new=endpoints_new, endpoints_lost=endpoints_lost)


@app.route('/session-info')
@login_required
def session_info():
    session = json.dumps(app.config['BETTERCAP_SESSION'], sort_keys=True, indent=4, separators=(',', ': '))
    return render_template('cmd.html', header='Session Info', response=session)


@app.route('/run-command', methods=['GET', 'POST'])
@login_required
def run_cmd(cmd=None):
    print(cmd)
    form = CommandForm()
    if form.validate_on_submit():
        response = json.dumps(bettercap.run_command(form.cmd.data), sort_keys=True, indent=4, separators=(',', ': '))
        return render_template('cmd.html', header='Run Command', response=response, form=form)
    return render_template('cmd.html', header='Run Command', new_cmd=True, form=form)


@app.route('/traffic')
@login_required
def traffic():
    session = app.config['BETTERCAP_SESSION']
    packets = session['packets']['Traffic']
    if request.is_xhr:
        template = 'traffic_ext.html'
    else:
        template = 'traffic.html'
    return render_template(template, packets=packets)


@app.route('/hosts')
@login_required
def get_hosts():
    session = app.config['BETTERCAP_SESSION']
    hosts = session['lan']['hosts']
    if request.is_xhr:
        template = 'hosts_ext.html'
    else:
        template = 'hosts.html'
    return render_template(template, hosts=hosts)
