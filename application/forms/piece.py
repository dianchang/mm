# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired, Optional


class TextForm(Form):
    channel_id = SelectField('频道', coerce=int)
    title = StringField('标题', validators=[Optional()], description='选填')
    content = TextAreaField('内容', validators=[DataRequired('内容不能为空')])


class ImageForm(Form):
    channel_id = SelectField('频道', coerce=int)
    image = HiddenField('图片', validators=[DataRequired('图片不能为空')])
    desc = TextAreaField('描述', validators=[Optional()])
