import pytest

from src.matchers import NaiveMatcher

from .base import MatcherBaseTests


class TestNaiveMatcher(MatcherBaseTests):

        @pytest.fixture
        def matcher(self):
            return NaiveMatcher()
