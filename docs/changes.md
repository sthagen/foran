# Changelog

## 2022.7.25

* Bumped dependencies for development and test
* Moved documentation to https://codes.dilettant.life/docs/foran
* Moved tracker to https://todo.sr.ht/~sthagen/foran
* Moved normative source repo to https://git.sr.ht/~sthagen/foran
* Added test coverage link to documentation and coverage to https://codes.dilettant.life/coverage/foran

## v2021.10.17

* Changed behavior for lists: Using list symbols `*` for commits, `+` for staged files, and `-` for modified files
* Enhanced implementation of adding a path to local repository as optional CLI argument (#9)
* Added documentation of use to github pages and python packaging (pypi.org)
* Amended metadata for python packaging
* Added more tests conrtibuting to 98 % test line coverage

## v2021.10.16

* Experimental implementation of adding a path to local repository as optional CLI argument (#9)
* Added dependency typer as base for implementing the enhanced command line API
* More tests to cover the command line API but less coverage due to expanded code (new commands)
* Exposed console entrypoint naturally named `foran` to ease script use cases

## v2021.10.15

* Experimental implementation of alerting on local staged for commit (#6)

## v2021.10.14

* Fixed typing use to enable ancient python 3.8.x versions 
* Increased test coverage by adding test with non-remote repository
* Enhanced github pages documentation

## v2021.10.13

* Learned to place nice when there is no remote at all
* Reduced python minimal version requirement down to >=3.8

## v2021.10.12

* Added report stem parameter (name of report file)

## v2021.10.11

* Corrected missing dependency

## v0.0.1 (2021-10-11)

* Initial release on PyPI
