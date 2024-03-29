# coding: utf-8
from flask import render_template, Blueprint, request, redirect, url_for, g
from ..utils.permissions import UserPermission
from ..utils.decorators import jsonify
from ..utils.uploadsets import images, process_site_image
from ..models import Channel

bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    """Index page."""
    if not g.user:
        return redirect(url_for('.discover'))
    return render_template('site/index.html')


@bp.route('/about')
def about():
    """About page."""
    return render_template('site/about.html')


@bp.route('/upload_image', methods=['POST'])
@UserPermission()
@jsonify
def upload_image():
    """上传通用图片"""
    try:
        filename = process_site_image(request.files['file'])
    except Exception, e:
        return {'success': False, 'error': e.__repr__()}
    else:
        return {'success': True, 'file_path': images.url(filename)}


@bp.route('/discover')
def discover():
    """发现"""
    channels = Channel.query.limit(30)
    return render_template('site/discover.html', channels=channels)
