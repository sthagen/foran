"""In front or behind (Foran eller bagved)? version and init interface."""

# [[[fill git_describe()]]]
__version__ = '2022.12.7+parent.43ecfe81'
# [[[end]]] (checksum: 71289b2b25248cb6f3d56c43f8d38504)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
