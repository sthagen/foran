"""In front or behind (Foran eller bagved)? version and init interface."""

# [[[fill git_describe()]]]
__version__ = '2023.6.19+parent.ceabb81a'
# [[[end]]] (checksum: d8b05f53d76c29819c0a875977b220a3)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
