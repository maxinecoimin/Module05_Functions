from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    requires_review,
)


def test_requires_review_over():
    assert requires_review(1500) is True


def test_requires_review_under():
    assert requires_review(500) is False


def test_requires_review_boundary():
    # Exactly at the threshold of 1000, it should not require review
    assert requires_review(1000) is False


def test_total_includes_tax():
    assert round(calculate_total(100, 2), 2) == 214.00


def test_tier_auto():
    assert get_approval_tier(400) == "auto"


def test_tier_boundary_500():
    assert get_approval_tier(500) == "auto"


def test_tier_manager():
    assert get_approval_tier(1500) == "manager"


def test_discount_ten():
    assert round(apply_discount(100, 10), 2) == 90.00
