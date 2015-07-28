# coding: utf-8
from flask import Blueprint, render_template, redirect, url_for, g
from ..utils.permissions import UserPermission
from ..forms.piece import TextForm, ImageForm
from ..models import db, Piece

bp = Blueprint('piece', __name__)


@bp.route('/piece/add')
@UserPermission()
def add():
    """添加条目"""
    return render_template('piece/add.html')


@bp.route('/piece/add_text', methods=['GET', 'POST'])
@UserPermission()
def add_text():
    """添加文字类条目"""
    form = TextForm()
    form.channel_id.choices = [(c.id, c.name) for c in g.user.channels]
    if form.validate_on_submit():
        piece = Piece(title=form.title.data, content=form.content.data, channel_id=form.channel_id.data,
                      user_id=g.user.id, kind='TEXT')
        db.session.add(piece)
        db.session.commit()
        return redirect(url_for('.view', uid=piece.id))
    return render_template('piece/add_text.html', form=form)


@bp.route('/piece/edit_text')
def edit_text():
    """编辑文字类条目"""
    return render_template('piece/edit_text.html')


@bp.route('/piece/add_image', methods=['GET', 'POST'])
@UserPermission()
def add_image():
    """添加图片"""
    form = ImageForm()
    form.channel_id.choices = [(c.id, c.name) for c in g.user.channels]
    if form.validate_on_submit():
        piece = Piece(image=form.image.data, desc=form.desc.data, channel_id=form.channel_id.data, user_id=g.user.id,
                      kind='IMAGE')
        db.session.add(piece)
        db.session.commit()
        return redirect(url_for('.view', uid=piece.id))
    return render_template('piece/add_image.html', form=form)


@bp.route('/piece/edit_image')
def edit_image():
    return render_template('piece/edit_image.html')


@bp.route('/piece/<int:uid>')
def view(uid):
    """单个条目"""
    piece = Piece.query.get_or_404(uid)
    return render_template('piece/view.html', piece=piece)


@bp.route('/piece/<int:uid>/edit', methods=['GET', 'POST'])
@UserPermission()
def edit(uid):
    """编辑条目"""
    piece = Piece.query.get_or_404(uid)
    if piece.kind == 'TEXT':
        form = TextForm(obj=piece)
        form.channel_id.choices = [(c.id, c.name) for c in g.user.channels]
        if form.validate_on_submit():
            piece.title = form.title.data
            piece.content = form.content.data
            piece.channel_id = form.channel_id.data
            db.session.add(piece)
            db.session.commit()
            return redirect(url_for('.view', uid=uid))
        return render_template('piece/edit_text.html', form=form)

    elif piece.kind == 'IMAGE':
        form = ImageForm(obj=piece)
        form.channel_id.choices = [(c.id, c.name) for c in g.user.channels]
        if form.validate_on_submit():
            piece.image = form.image.data
            piece.desc = form.desc.data
            piece.channel_id = form.channel_id.data
            db.session.add(piece)
            db.session.commit()
            return redirect(url_for('.view', uid=uid))
        return render_template('piece/edit_image.html', form=form)
