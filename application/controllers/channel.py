# coding: utf-8
from flask import Blueprint, render_template, redirect, url_for, g
from ..utils.permissions import UserPermission
from ..forms.channel import ChannelForm
from ..models import db, Channel

bp = Blueprint('channel', __name__)


@bp.route('/channel/add', methods=['GET', 'POST'])
@UserPermission()
def add():
    """创建频道"""
    form = ChannelForm()
    if form.validate_on_submit():
        channel = Channel(name=form.name.data, user_id=g.user.id)
        db.session.add(channel)
        db.session.commit()
        return redirect(url_for('.view', uid=channel.id))
    return render_template('channel/add.html', form=form)


@bp.route('/channel/remove', methods=['POST'])
@UserPermission()
def remove():
    """移除频道"""
    pass


@bp.route('/channel/edit', methods=['GET', 'POST'])
@UserPermission()
def edit():
    """编辑频道"""
    return render_template('channel/edit.html')


@bp.route('/channel/<int:uid>')
def view(uid):
    """频道主页"""
    channel = Channel.query.get_or_404(uid)
    return render_template('channel/view.html', channel=channel)
