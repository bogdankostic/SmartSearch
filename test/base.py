import pytest

from src.matchers import BaseMatcher


class MatcherBaseTests:

    @pytest.fixture
    def matcher(self) -> BaseMatcher:
        """Base fixture, to be reimplemented when deriving from DocumentStoreBaseTests"""
        raise NotImplementedError()

    def test_search_returns_empty_list_when_no_match(self, matcher):
        assert matcher.search("pattern", "text") == []

    def test_search_returns_correct_indices_when_match(self, matcher):
        assert matcher.search("pattern", "patternpattern") == [0, 7]

    def test_search_method_raises_type_error_when_pattern_not_string(self, matcher):
        with pytest.raises(TypeError):
            matcher.search(123, "text")

    def test_search_method_raises_type_error_when_text_not_string(self, matcher):
        with pytest.raises(TypeError):
            matcher.search("pattern", 123)

    def test_search_method_returns_empty_list_when_pattern_empty_string(self, matcher):
        assert matcher.search("", "text") == []

    def test_search_method_returns_list_with_one_element_when_pattern_equal_to_text(self, matcher):
        assert matcher.search("text", "text") == [0]

    def test_search_method_returns_empty_list_when_text_empty_string(self, matcher):
        assert matcher.search("pattern", "") == []

    def test_search_method_returns_empty_list_when_pattern_longer_than_text(self, matcher):
        assert matcher.search("patternpattern", "pattern") == []

    def test_case_insensitive_search(self, matcher):
        matcher.case_sensitive = False
        assert matcher.search("pattern", "Pattern") == [0]
        assert matcher.search("pattern", "patternPattern") == [0, 7]
        assert matcher.search("PATTERN", "patternPattern") == [0, 7]

    def test_case_sensitive_search(self, matcher):
        assert matcher.search("pattern", "Pattern") == []
        assert matcher.search("pattern", "patternPattern") == [0]
        assert matcher.search("Pattern", "patternPattern") == [7]
        assert matcher.search("PATTERN", "patternPattern") == []
