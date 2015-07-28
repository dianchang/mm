# coding: utf-8
from .suite import BaseSuite


class TestPiece(BaseSuite):
    def test_action(self):
        rv = self.client.get('/piece/action')
        assert rv.status_code == 200
