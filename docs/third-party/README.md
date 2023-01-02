# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/foran/blob/default/sbom.json) with SHA256 checksum ([4549b779 ...](https://git.sr.ht/~sthagen/foran/blob/default/sbom.json.sha256 "sha256:4549b779cd37f0f57c9bd77a5d5bfccfb3ec7e6345f766127c4eb12b96c6c63d")).
<!--[[[end]]] (checksum: 5cc41d31b80ab5b4cfe8c90e49e2bac0)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                           | Version                                              | License     | Author                         | Description (from packaging data)                                    |
|:---------------------------------------------------------------|:-----------------------------------------------------|:------------|:-------------------------------|:---------------------------------------------------------------------|
| [GitPython](https://github.com/gitpython-developers/GitPython) | [3.1.30](https://pypi.org/project/GitPython/3.1.30/) | BSD License | Sebastian Thiel, Michael Trier | GitPython is a python library used to interact with Git repositories |
| [typer](https://github.com/tiangolo/typer)                     | [0.7.0](https://pypi.org/project/typer/0.7.0/)       | MIT License | Sebastián Ramírez              | Typer, build great CLIs. Easy to code. Based on Python type hints.   |
<!--[[[end]]] (checksum: 06e6ed0aca7ea6b2375fdde945381d00)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                   | Version                                          | License     | Author          | Description (from packaging data)                                   |
|:-------------------------------------------------------|:-------------------------------------------------|:------------|:----------------|:--------------------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)          | [8.1.3](https://pypi.org/project/click/8.1.3/)   | BSD License | Armin Ronacher  | Composable command line interface toolkit                           |
| [gitdb](https://github.com/gitpython-developers/gitdb) | [4.0.10](https://pypi.org/project/gitdb/4.0.10/) | BSD License | Sebastian Thiel | Git Object Database                                                 |
| [smmap](https://github.com/gitpython-developers/smmap) | [5.0.0](https://pypi.org/project/smmap/5.0.0/)   | BSD License | Sebastian Thiel | A pure Python implementation of a sliding window memory map manager |
<!--[[[end]]] (checksum: 96b6ce9789804a79d61fdc2413fdb173)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
GitPython==3.1.30
  - gitdb [required: >=4.0.1,<5, installed: 4.0.10]
    - smmap [required: >=3.0.1,<6, installed: 5.0.0]
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: 7ad6d7d32fa97403e34879bbab34cf92)-->
