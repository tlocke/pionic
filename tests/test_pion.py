from pion import load, loads, PionException
from io import StringIO
from datetime import (
    datetime as Datetime, timezone as Timezone, timedelta as Timedelta)
import pytest
from decimal import Decimal


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
            2007),

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
    if isinstance(pyth, Exception):
        with pytest.raises(PionException):
            loads(ion_str)
    else:
        assert loads(ion_str) == pyth


@pytest.mark.parametrize(
    "ion_str", [
        'null',

        # Identical to unadorned null
        'null.null',

        'null.bool',
        'null.int',
        'null.float',
        'null.decimal',
        'null.timestamp',
        'null.string',
        'null.symbol',
        'null.blob',
        'null.clob',
        'null.struct',
        'null.list',
        'null.sexp'])
def test_nulls(ion_str):
    assert loads(ion_str) is None


@pytest.mark.parametrize(
    "ion_str,pyth", [
        ('true', True),
        ('false', False)])
def test_booleans(ion_str, pyth):
    assert loads(ion_str) == pyth


@pytest.mark.parametrize(
    "ion_str,pyth", [

        # Zero.  Surprise!
        ('0', 0),

        # ...the same value with a minus sign
        ('-0', 0),

        # A normal int
        ('123', 123),

        # Another negative int
        ('-123', -123),

        # An int denoted in hexadecimal
        ('0xBeef', 0xBeef),

        # An int denoted in binary
        ('0b0101', 0b0101),

        # An int with underscores
        ('1_2_3', 123),

        # An int denoted in hexadecimal with underscores
        ('0xFA_CE', 0xFACE),

        # An int denoted in binary with underscores
        ('0b10_10_10', 0b101010),

        # ERROR: leading plus not allowed
        ('+1', PionException()),

        # ERROR: leading zeros not allowed (no support for octal notation)
        ('0123', PionException()),

        # ERROR: trailing underscore not allowed
        ('1_', PionException()),

        # ERROR: consecutive underscores not allowed
        ('1__2', PionException()),

        # ERROR: underscore can only appear between digits (the radix prefix is
        # not a digit)
        ('0x_12', PionException()),

        # A symbol (ints cannot start with underscores)
        ('_1', '_1')])
def test_integers(ion_str, pyth):
    if isinstance(pyth, Exception):
        with pytest.raises(PionException):
            loads(ion_str)
    else:
        assert loads(ion_str) == pyth


@pytest.mark.parametrize(
    "ion_str,pyth", [

        # Type is decimal
        ('0.123', Decimal('0.123')),


        # Type is float
        ('-0.12e4', -0.12e4),

        # Type is decimal
        ('-0.12d4', Decimal('-0.12e4')),

        # Zero as float
        ('0E0', float(0)),

        # Zero as decimal
        ('0D0', Decimal('0')),

        #   ...the same value with different notation
        ('0.', Decimal('0')),

        # Negative zero float   (distinct from positive zero)
        ('-0e0', float(-0)),

        # Negative zero decimal (distinct from positive zero)
        ('-0d0', Decimal('-0')),

        #   ...the same value with different notation
        ('-0.', Decimal('-0')),

        # Decimal maintains precision: -0. != -0.0
        ('-0d-1', Decimal('-0.0')),

        # Decimal with underscores
        ('123_456.789_012', Decimal('123456.789012')),

        # ERROR: underscores may not appear next to the decimal point
        ('123_._456', PionException()),

        # ERROR: consecutive underscores not allowed
        ('12__34.56', PionException()),

        # ERROR: trailing underscore not allowed
        ('123.456_', PionException()),

        # ERROR: underscore after negative sign not allowed
        ('-_123.456', PionException()),

        # ERROR: the symbol '_123' followed by an unexpected dot
        ('_123.456', PionException())])
def test_reals(ion_str, pyth):
    if isinstance(pyth, Exception):
        with pytest.raises(PionException):
            loads(ion_str)
    else:
        assert loads(ion_str) == pyth


@pytest.mark.parametrize(
    "ion_str,pyth", [

        # An empty string value
        ('""', ''),

        # A normal string
        ('" my string "', ' my string '),

        # Contains one double-quote character
        ('"\\""', '"'),

        # Contains one unicode character
        (r'"\uABCD"', '\uABCD'),

        # String with type annotation 'xml'
        ('xml::"<e a=\'v\'>c</e>"', "<e a='v'>c</e>"),

        # Sexp with one element
        ("( '''hello '''\r'''world!'''  )", ('hello world!',)),

        # The exact same sexp value
        ('("hello world!")', ('hello world!',)),

        # This Ion value is a string containing three newlines. The serialized
        # form's first newline is escaped into nothingness.
        (r"""'''\
The first line of the string.
This is the second line of the string,
and this is the third line.
'''""", """The first line of the string.
This is the second line of the string,
and this is the third line.
""")])
def test_strings(ion_str, pyth):
    if isinstance(pyth, Exception):
        with pytest.raises(PionException):
            loads(ion_str)
    else:
        assert loads(ion_str) == pyth


'''
def test_str():
    for c in pstr:
        print(ord(c))
    conv = loads(pstr)
    assert conv == ('hello world!',)
    for c in conv:
        print(ord(c))
    raise Exception()
'''
