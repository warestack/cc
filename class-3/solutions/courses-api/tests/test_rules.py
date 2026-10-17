from datetime import datetime, timedelta, timezone

import pytest

from rules import enrolment_is_open


@pytest.mark.parametrize("seconds, expected", [(-1, True), (0, False), (1, False)])
def test_enrolment_boundary(seconds, expected):
    closes_at = datetime(2026, 11, 1, 12, tzinfo=timezone.utc)
    now = closes_at + timedelta(seconds=seconds)
    assert enrolment_is_open(closes_at, now) is expected
