# tlsrpt-policy

Parse and validate SMTP TLS Reporting (RFC 8460) policies in Python.

[RFC 8460](https://datatracker.ietf.org/doc/html/rfc8460) defines a mechanism for 
receiving reports about TLS misconfigurations and errors. In order to receive a report, 
mail server administors will add a special TXT-record (e.g. `_smtp._tls.example.com`)
to their domain. This record is called the TLSRPT policy and looks something like 
this: `TXT	"v=TLSRPTv1; rua=mailto:smtp-tls-report@example.com"`.

The purpose of this module is to provide a parser and validator for these records in Python.
It uses [PyParsing](https://pypi.org/project/pyparsing/) to implement the grammar as 
specified in [RFC 8460, section 3](https://datatracker.ietf.org/doc/html/rfc8460#section-3).

## Installation

tlsrpt-policy is hosted on PyPI and you can install it in a virtual environment like this:

```bash
$ pip install tlsrpt-policy
```

## How to use

### parse_silent()

The function `parse_silent()` will not throw an error when parsing an invalid TLSRPT policy record.
If the record is not well-formed then this function will simply return `None`.

Here is an example of how to use the silent parser:

```
>>> from tlsrpt_policy.tlsrpt_parsing import parse_silent
>>> TXT_RECORD = "v=TLSRPTv1; rua=https://reporting.example.com/v1/tlsrpt"
>>> tlsrpt_parsing.parse_silent(TXT_RECORD)
...
```

## Developed With Support By

- sys4 AG, Germany: https://sys4.de/

## Credits

- Platform Internetstandaarden, the Netherlands: https://internet.nl/

Based on the [SPF parser](https://github.com/internetstandards/Internet.nl/blob/main/checks/tasks/spf_parser.py) of the Internet.nl project.

