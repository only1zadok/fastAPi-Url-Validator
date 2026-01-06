import pytest
from pydantic import ValidationError
from app.schemas import WebsiteIn


def test_valid_https():
    m = WebsiteIn(website="https://example.com")
    assert str(m.website).startswith("https://")


def test_valid_without_scheme_is_invalid_for_httpurl():
    # HttpUrl requires scheme, so this should fail.
    with pytest.raises(ValidationError):
        WebsiteIn(website="example.com")


def test_blocks_non_http_scheme():
    with pytest.raises(ValidationError):
        WebsiteIn(website="ftp://example.com")


def test_blocks_localhost():
    with pytest.raises(ValidationError):
        WebsiteIn(website="http://localhost:8000")


def test_blocks_private_ip_literal():
    with pytest.raises(ValidationError):
        WebsiteIn(website="http://192.168.1.10")


def test_unresolvable_domain_fails():
    with pytest.raises(ValidationError):
        WebsiteIn(website="https://this-domain-should-not-exist-xyz-1234567890.com")
