fileMover2
==========
[![Build Status](https://travis-ci.org/ioawnen/fileMover2.svg?branch=develop)](https://travis-ci.org/ioawnen/fileMover2)

A less shitty version of fileMover, a script for moving files for lazy shits with too many downloads.

- [fileMover2](#filemover2)
    - [Usage](#usage)
    - [Dependencies](#dependencies)
    - [Configuration](#configuration)
        - [Settings](#settings)
            - [Logging Level (log_level)](#logging-level-loglevel)
            - [Move Tasks File Path (move_tasks_file_path)](#move-tasks-file-path-movetasksfilepath)
        - [Move Tasks](#move-tasks)
            - [Overview](#overview)
            - [Schema](#schema)

## Usage
This script uses Python 3. Run like this:

```
python3 fileMover.py
```
Easy!

## Dependencies
- Colorama

## Configuration

### Settings
On first run settings.json is created with default settings in the same directory as `fileMover.py`.

#### Logging Level (log_level)
`Default: 2`

Controls the verbosity of the console output. The following levels are supported:

 |  Input   |   Level   |
 |---------:|:----------|
 | 0        | Error     |
 | 1        | Warning   |
 | 2        | Log       |
 | 3        | Info      |
 | 4        | Silly     |

#### Move Tasks File Path (move_tasks_file_path)
`Default: move_tasks.json`

Path of the move tasks file.

### Move Tasks
On first run move_tasks.json is created with an example task. By default this is placed in the same directory as `fileMover.py`. 
*(This can be changed in settings.json)*


#### Overview
Move tasks describe where to look for files, where to move files it finds, and what files to move. Multiple move tasks can be run by adding multiple move tasks to the array.

```
[
    {
        "search_path": "/tmp/source",
        "save_path": "/tmp/destination",
        "filename_regex": "[examplefile,examplefile2].*"
    }
]
```

The above example will search in `/tmp/source` for files that match `examplefile.*` or `examplefile2.*`, then moves the matches to `/tmp/destination`.

Move tasks are stored in boring old JSON, so treat the syntax as such and there isn't much that can go wrong.

#### Schema

| Key            | Description                  |
| -------------: | :--------------------------- |
| search_path    | Path to search in            |
| save_path      | Path to save matches in      |
| filename_regex | Regex to match files against |
