import pytest

from src.matchers import BoyerMooreMatcher

from .base import MatcherBaseTests


class TestBoyerMooreMatcher(MatcherBaseTests):

    @pytest.fixture
    def matcher(self):
        return BoyerMooreMatcher()
