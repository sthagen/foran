# Usage


## `foran`

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

### `foran diff`

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

### `foran label`

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

### `foran template`

Output an example jinja template representing the defaults

**Usage**:

```console
$ foran template [OPTIONS]
```

**Options**:

* `-o, --output TEXT`: [default: ]
* `-h, --help`: Show this message and exit.

### `foran version`

Display the foran version and exit

**Usage**:

```console
$ foran version [OPTIONS]
```

**Options**:

* `-h, --help`: Show this message and exit.
