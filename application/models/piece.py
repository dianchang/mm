# coding: utf-8
from datetime import datetime
from ._base import db


class Piece(db.Model):
    """条目"""
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.Enum('TEXT', 'IMAGE'))

    title = db.Column(db.String(200))
    content = db.Column(db.Text)

    image = db.Column(db.String(200))
    desc = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.now)

    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    channel = db.relationship('Channel', backref=db.backref('pieces',
                                                            lazy='dynamic',
                                                            order_by='asc(Piece.created_at)'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('pieces',
                                                      lazy='dynamic',
                                                      order_by='asc(Piece.created_at)'))

    def __repr__(self):
        return '<Piece %s>' % self.name


class PieceComment(db.Model):
    """针对条目的评论"""
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

    piece_id = db.Column(db.Integer, db.ForeignKey('piece.id'))
    piece = db.relationship('Piece', backref=db.backref('comments',
                                                        lazy='dynamic',
                                                        order_by='asc(PieceComment.created_at)'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('piece_comments',
                                                      lazy='dynamic',
                                                      order_by='asc(PieceComment.created_at)'))

    def __repr__(self):
        return '<Piece %s>' % self.name


class LikePiece(db.Model):
    """喜欢条目"""
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    piece_id = db.Column(db.Integer, db.ForeignKey('piece.id'))
    piece = db.relationship('Piece', backref=db.backref('likers',
                                                        lazy='dynamic',
                                                        order_by='asc(LikePiece.created_at)'))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('liked_pieces',
                                                      lazy='dynamic',
                                                      order_by='asc(LikePiece.created_at)'))
