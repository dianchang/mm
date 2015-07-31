# coding: utf-8
from flask import Blueprint, render_template, g
from ..models import Channel, User
from ..utils.permissions import UserPermission

bp = Blueprint('user', __name__)


@bp.route('/my/channels')
@UserPermission()
def channels():
    """我的频道"""
    channels = g.user.channels
    return render_template('user/channels.html', channels=channels)


@bp.route('/u/<int:uid>')
def profile(uid):
    """用户主页"""
    user = User.query.get_or_404(uid)
    channels = user.channels.limit(6)
    return render_template('user/profile.html', user=user, channels=channels)
