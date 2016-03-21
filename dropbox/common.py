# -*- coding: utf-8 -*-
# Auto-generated by BabelAPI, do not modify.
try:
    from . import babel_validators as bv
except (SystemError, ValueError):
    # Catch errors raised when importing a relative module when not in a package.
    # This makes testing this file directly (outside of a package) easier.
    import babel_validators as bv

Date_validator = bv.Timestamp(u'%Y-%m-%d')
DisplayName_validator = bv.String(min_length=1, pattern=u'[^/:?*<>"|]*')
DropboxTimestamp_validator = bv.Timestamp(u'%Y-%m-%dT%H:%M:%SZ')
EmailAddress_validator = bv.String(max_length=255, pattern=u"^['&A-Za-z0-9._%+-]+@[A-Za-z0-9-][A-Za-z0-9.-]*.[A-Za-z]{2,15}$")
NamePart_validator = bv.String(min_length=1, max_length=100, pattern=u'[^/:?*<>"|]*')
SharedFolderId_validator = bv.String(pattern=u'[-_0-9a-zA-Z:]+')
