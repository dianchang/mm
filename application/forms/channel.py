# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired


class ChannelForm(Form):
    name = StringField('名称', validators=[DataRequired('名称不能为空')])
    cover = HiddenField('', validators=[DataRequired('图标不能为空')])
    # tags = StringField('标签')
