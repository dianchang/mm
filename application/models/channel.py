# coding: utf-8
from datetime import datetime
from ._base import db
from ..utils.uploadsets import images


class Channel(db.Model):
    """频道"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    show_order = db.Column(db.Integer, default=0)
    clicks = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    cover = db.Column(db.String(200), default='default_channel_cover.png')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('channels',
                                                      lazy='dynamic',
                                                      order_by='asc(Channel.created_at)'))

    @property
    def cover_url(self):
        return images.url(self.cover) if self.cover else None

    def __repr__(self):
        return '<Channel %s>' % self.name


class ChannelTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    channel = db.relationship('Channel', backref=db.backref('tags',
                                                            lazy='dynamic',
                                                            order_by='asc(ChannelTag.created_at)'))

    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    tag = db.relationship('Tag', backref=db.backref('channels',
                                                    lazy='dynamic',
                                                    order_by='asc(ChannelTag.created_at)'))


class Tag(db.Model):
    """标签"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Tag %s>' % self.name


class FollowChannel(db.Model):
    """关注频道"""
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    channel = db.relationship('Channel', backref=db.backref('followers',
                                                            lazy='dynamic',
                                                            order_by='asc(FollowChannel.created_at)'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('followed_channels',
                                                      lazy='dynamic',
                                                      order_by='asc(FollowChannel.created_at)'))


class ChannelComment(db.Model):
    """针对频道的评论"""
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    channel = db.relationship('Channel', backref=db.backref('comments',
                                                            lazy='dynamic',
                                                            order_by='asc(ChannelComment.created_at)'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('channel_comments',
                                                      lazy='dynamic',
                                                      order_by='asc(ChannelComment.created_at)'))
