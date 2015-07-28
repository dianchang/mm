# coding: utf-8
from .suite import BaseSuite


class TestChannel(BaseSuite):
    def test_action(self):
        rv = self.client.get('/channel/action')
        assert rv.status_code == 200
