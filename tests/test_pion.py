from pion import load, loads, PionException
from io import StringIO
from datetime import (
    datetime as Datetime, timezone as Timezone, timedelta as Timedelta)
import pytest


def test_load():
    assert load(StringIO('{}')) == {}


def test_loads():
    assert loads('{}') == {}


@pytest.mark.parametrize(
    "ion_str,pyth", [

        # A null timestamp value
        (
            'null.timestamp',
            None),

        # Seconds are optional, but local offset is not
        (
            '2007-02-23T12:14Z',
            Datetime(2007, 2, 23, 12, 14, tzinfo=Timezone.utc)),

        # A timestamp with millisecond precision and PST local time
        (
            '2007-02-23T12:14:33.079-08:00',
            Datetime(
                2007, 2, 23, 12, 14, 33, 79000,
                tzinfo=Timezone(Timedelta(hours=-8)))),

        # The same instant in UTC ("zero" or "zulu")
        (
            '2007-02-23T20:14:33.079Z',
            Datetime(2007, 2, 23, 20, 14, 33, 79000, tzinfo=Timezone.utc)),

        # The same instant, with explicit local offset
        (
            '2007-02-23T20:14:33.079+00:00',
            Datetime(
                2007, 2, 23, 20, 14, 33, 79000,
                tzinfo=Timezone(Timedelta(hours=0)))),

        # The same instant, with unknown local offset
        (
            '2007-02-23T20:14:33.079-00:00',
            Datetime(
                2007, 2, 23, 20, 14, 33, 79000,
                tzinfo=Timezone(Timedelta(hours=0)))),

        # Happy New Year in UTC, unknown local offset
        (
            '2007-01-01T00:00-00:00',
            Datetime(2007, 1, 1, tzinfo=Timezone.utc)),

        # The same instant, with days precision, unknown local offset
        (
            '2007-01-01',
            Datetime(2007, 1, 1, tzinfo=Timezone.utc)),

        # The same value, different syntax.
        # Shouldn't actually be an error, but arrow says it is.
        (
            '2007-01-01T',
            Exception()),

        # The same instant, with months precision, unknown local offset
        # Shouldn't actually be an error, but arrow says it is.
        (
            '2007-01T',
            Exception()),

        # The same instant, with years precision, unknown local offset
        # Shouldn't actually be an error, but arrow says it is.
        (
            '2007T',
            Exception()),

        # A day, unknown local offset
        (
            '2007-02-23',
            Datetime(2007, 2, 23, tzinfo=Timezone.utc)),

        # The same instant, but more precise and in UTC
        (
            '2007-02-23T00:00Z',
            Datetime(2007, 2, 23, tzinfo=Timezone.utc)),

        # An equivalent format for the same value
        (
            '2007-02-23T00:00+00:00',
            Datetime(2007, 2, 23, tzinfo=Timezone.utc)),

        # The same instant, with seconds precision
        (
            '2007-02-23T00:00:00-00:00',
            Datetime(2007, 2, 23, tzinfo=Timezone.utc)),

        # Not a timestamp, but an int
        (
            '2007',
            Exception()),

        # ERROR: Must end with 'T' if not whole-day precision, this results
        # as an invalid-numeric-stopper error
        (
            '2007-01',
            Exception()),

        # ERROR: Must have at least one digit precision after decimal point.
        (
            '2007-02-23T20:14:33.Z',
            Exception())])
def test_timestamps(ion_str, pyth):
    print('ion_str', ion_str, 'pyth', pyth)
    if isinstance(pyth, Exception):
        with pytest.raises(PionException):
            loads(ion_str)
    else:
        assert loads(ion_str) == pyth
