# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/foran/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([66094f6c ...](https://git.sr.ht/~sthagen/foran/blob/default/etc/sbom/cdx.json.sha256 "sha256:66094f6c48ca6138f8aeaa72799377aa67cf0d52622cc5c5a1560586d83d8301")).
<!--[[[end]]] (checksum: da1ad385e10fb4efbc4b5148d3b02543)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                           | Version                                              | License     | Author                         | Description (from packaging data)                                    |
|:---------------------------------------------------------------|:-----------------------------------------------------|:------------|:-------------------------------|:---------------------------------------------------------------------|
| [GitPython](https://github.com/gitpython-developers/GitPython) | [3.1.40](https://pypi.org/project/GitPython/3.1.40/) | BSD License | Sebastian Thiel, Michael Trier | GitPython is a Python library used to interact with Git repositories |
| [typer](https://github.com/tiangolo/typer)                     | [0.9.0](https://pypi.org/project/typer/0.9.0/)       | MIT License | Sebastián Ramírez              | Typer, build great CLIs. Easy to code. Based on Python type hints.   |
<!--[[[end]]] (checksum: 20fc0fd9a632213b370bbc20e8218b61)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                   | Version                                          | License     | Author                                | Description (from packaging data)                                   |
|:-------------------------------------------------------|:-------------------------------------------------|:------------|:--------------------------------------|:--------------------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)          | [8.1.5](https://pypi.org/project/click/8.1.5/)   | BSD License | Pallets <contact@palletsprojects.com> | Composable command line interface toolkit                           |
| [gitdb](https://github.com/gitpython-developers/gitdb) | [4.0.10](https://pypi.org/project/gitdb/4.0.10/) | BSD License | Sebastian Thiel                       | Git Object Database                                                 |
| [smmap](https://github.com/gitpython-developers/smmap) | [5.0.0](https://pypi.org/project/smmap/5.0.0/)   | BSD License | Sebastian Thiel                       | A pure Python implementation of a sliding window memory map manager |
<!--[[[end]]] (checksum: 4f66948069497394ad6d14fcf30a4d3d)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
GitPython==3.1.40
└── gitdb [required: >=4.0.1,<5, installed: 4.0.10]
    └── smmap [required: >=3.0.1,<6, installed: 5.0.0]
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.5]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 456e3de0699609dd0d9f0e9dcfdf7548)-->
