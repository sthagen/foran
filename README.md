# foran

[![license](https://img.shields.io/github/license/sthagen/foran.svg?style=flat)](https://github.com/sthagen/foran/blob/default/LICENSE)
[![version](https://img.shields.io/pypi/v/foran.svg?style=flat)](https://pypi.python.org/pypi/foran/)
[![downloads](https://img.shields.io/pypi/dm/foran.svg?style=flat)](https://pypi.python.org/pypi/foran/)
[![wheel](https://img.shields.io/pypi/wheel/foran.svg?style=flat)](https://pypi.python.org/pypi/foran/)
[![supported-versions](https://img.shields.io/pypi/pyversions/foran.svg?style=flat)](https://pypi.python.org/pypi/foran/)
[![supported-implementations](https://img.shields.io/pypi/implementation/foran.svg?style=flat)](https://pypi.python.org/pypi/foran/)

Answering if a local is in front of its remote.

The English "in front" may translate to the Danish "foran".

... and the default report stem `foran-eller-bagved` alludes to the English "In front or behind?" question which corresponds to the Danish "Foran eller bagved?"

## Status

Experimental.

**Note**: The default branch is `default`.

# Use

<!-- MarkdownTOC -->

- `foran`
	- `foran diff`
	- `foran label`
	- `foran template`
	- `foran version`

<!-- /MarkdownTOC -->

# `foran`

In front or behind (Foran eller bagved)?

Identify and diff a local repository against the remote using templates for reports.

**Usage**:

```console
$ foran [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-V, --version`: Display the foran version and exit  [default: False]
* `-h, --help`: Show this message and exit.

**Commands**:

* `diff`: Diff the local against the remote repository...
* `label`: Labels the local repository state
* `template`: Output an example jinja template representing...
* `version`: Display the foran version and exit

## `foran diff`

Diff the local against the remote repository state

**Usage**:

```console
$ foran diff [OPTIONS] [SOURCE]
```

**Arguments**:

* `[SOURCE]`: [default: .]

**Options**:

* `-i, --input TEXT`: [default: ]
* `-o, --output TEXT`: [default: ]
* `-t, --template TEXT`: [default: ]
* `-h, --help`: Show this message and exit.

## `foran label`

Labels the local repository state

**Usage**:

```console
$ foran label [OPTIONS] [SOURCE]
```

**Arguments**:

* `[SOURCE]`: [default: .]

**Options**:

* `-i, --input TEXT`: [default: ]
* `-o, --output TEXT`: [default: ]
* `-t, --template TEXT`: [default: ]
* `-h, --help`: Show this message and exit.

## `foran template`

Output an example jinja template representing the defaults

**Usage**:

```console
$ foran template [OPTIONS]
```

**Options**:

* `-o, --output TEXT`: [default: ]
* `-h, --help`: Show this message and exit.

## `foran version`

Display the foran version and exit

**Usage**:

```console
$ foran version [OPTIONS]
```

**Options**:

* `-h, --help`: Show this message and exit.
