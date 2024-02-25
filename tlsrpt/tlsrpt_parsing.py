# Copyright: 2022-2024, ECP, NLnet Labs, the Internet.nl contributors and SYS4 AG.
# SPDX-License-Identifier: Apache-2.0

'''
SMTP TLS Reporting policy parser as defined by:

  RFC 8460, Section "3. Reporting Policy", see: 
  https://datatracker.ietf.org/doc/html/rfc8460#section-3
'''

from pyparsing import (
    Literal,
    CaselessLiteral,
    Combine,
    Group,
    OneOrMore,
    Optional,
    ParseException,
    ParserElement,
    Regex,
    StringEnd,
    White,
    Word,
    ZeroOrMore,
    alphanums,
    alphas,
    nums,
    printables,
    pyparsing_common,
)

WSP = White(ws=' ', exact=1).suppress()   # Whitespace

field_delim = ZeroOrMore(WSP) + ';' + ZeroOrMore(WSP)   # Fields are semicolon-delimited
tlsrpt_extension = ZeroOrMore(Literal("TODO"))

regex_tld = r"(?:[a-zA-Z]{2,63}|xn--[a-zA-Z0-9]+)"
regex_mailaddr = (
    r"(?P<mailaddr>([a-zA-Z0-9]{0,61}@)?([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+" r"" + regex_tld + ")"
)
mail_uri = Combine(CaselessLiteral("mailto:") + Regex(regex_mailaddr))

tlsrpt_rua = Literal("rua=") \
             + OneOrMore(mail_uri | pyparsing_common.url).setResultsName('tlsrpt_uri')

tlsrpt_field = tlsrpt_rua #  + tlsrpt_extension

#ZeroOrMore(OneOrMore(field_delim) )


# Literal will match the version string as required by the ABNF in the RFC:
# tlsrpt-version    = %s"v=TLSRPTv1"
version = Literal("v=TLSRPTv1").setResultsName("tlsrpt_version")

record = version + OneOrMore(field_delim + tlsrpt_field)


def parse(tlsrpt_record):
    """
    Will return None if there was a parsing error and a ParseResult object otherwise.
    """
    try:
        parsed = record.parseString(tlsrpt_record)
    except ParseException:
        parsed = None
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        parsed = None
    return parsed
