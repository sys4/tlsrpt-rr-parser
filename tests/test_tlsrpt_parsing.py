import pytest

from tlsrpt import tlsrpt_parsing


def test_record_parse_simple_mailto():
    TXT_RECORD="v=TLSRPTv1; rua=mailto:reports@example.com"
    parsed = tlsrpt_parsing.record.parseString(TXT_RECORD)
    assert parsed is not None
    assert parsed.tlsrpt_version == 'v=TLSRPTv1'
    assert parsed.tlsrpt_uri[0] == 'mailto:reports@example.com'


def test_record_parse_simple_https():
    TXT_RECORD = "v=TLSRPTv1; rua=https://reporting.example.com/v1/tlsrpt"
    parsed = tlsrpt_parsing.record.parseString(TXT_RECORD)
    assert parsed.tlsrpt_version == 'v=TLSRPTv1'
    assert parsed.tlsrpt_uri[0] == 'https://reporting.example.com/v1/tlsrpt'
    assert parsed is not None
