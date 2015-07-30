# coding: utf-8
from flask import Blueprint, render_template, redirect, url_for, g, request
from ..utils.permissions import UserPermission
from ..forms.channel import ChannelForm
from ..models import db, Channel, Piece
from ..utils.decorators import jsonify
from ..utils.uploadsets import images, process_channel_cover

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


@bp.route('/channel/<int:uid>/edit', methods=['GET', 'POST'])
@UserPermission()
def edit(uid):
    """编辑频道"""
    channel = Channel.query.get_or_404(uid)
    form = ChannelForm(obj=channel)
    if form.validate_on_submit():
        # channel.cover = form.cover.data
        channel.name = form.name.data
        db.session.add(channel)
        db.session.commit()
        return redirect(url_for('.view', uid=channel.id))
    return render_template('channel/edit.html', form=form, channel=channel)


@bp.route('/channel/<int:uid>')
def view(uid):
    """频道主页"""
    channel = Channel.query.get_or_404(uid)
    pieces = channel.pieces
    return render_template('channel/view.html', channel=channel, pieces=pieces)


@bp.route('/channel/upload_cover', methods=['POST'])
@UserPermission()
@jsonify
def upload_cover():
    """上传通用图片"""
    try:
        filename = process_channel_cover(request.files['file'])
    except Exception, e:
        return {'result': False, 'error': e.__repr__()}
    else:
        return {'result': True, 'url': images.url(filename), 'path': filename}
