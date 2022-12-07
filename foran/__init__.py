"""In front or behind (Foran eller bagved)? version and init interface."""

# [[[fill git_describe()]]]
__version__ = '2022.12.6+parent.e68424eb'
# [[[end]]] (checksum: 42b491a202e452d0d220e3c599c4d341)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
