fileMover2
==========
[![Build Status](https://travis-ci.org/ioawnen/fileMover2.svg?branch=develop)](https://travis-ci.org/ioawnen/fileMover2)

A less shitty version of fileMover, a script for moving files for lazy shits with too many downloads.


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
Controls the verbosity of the console output. The following levels are supported:

 |  Input   |   Level   |
 |---------:|:----------|
 | 0        | Error     |
 | 1        | Warning   |
 | 2        | Log       |
 | 3        | Info      |
 | 4        | Silly     |

#### Move Tasks File Path (move_tasks_file_path)
Location of the move tasks file.

### Move Tasks
On first run move_tasks.json is created with an example task. By default this is placed in the same directory as `fileMover.py`. 
*(This can be changed in settings.json)*
#### TODO: ADD MOVE TASKS DETAIL
