# cora
cora - COde Replacement Api

This python-based command-line tools allows to render file placeholders in other files.
The tools is independent of the document type, since it is assumed that the chosen
syntax does not interfere with syntax of any (especially markup) languages.

## Usage

Insert a placeholder of the following syntax inside a file (here 
`file_with_placeholder.md`):

```md
§§§<filename>:<start>:<end>§§§
```

Afterwards, you can render the placeholder by running

```bash
$ cora -i "file_with_placeholder.md"
```

This will replace the original line in the markdown file  with the content of the 
file `<filename>` from line `<start>` to line `<end>`. 
The file in the repository will no be changed, but before building the
docs, a script will create a processed copy of the corresponding markdown file.

**Using a URL instead of a file from the repository**

If you want to link a file that is not present in the umami repo, but you have a URL
to that exact file, you can use the following syntax:

```md
§§§url="<url>":<start>:<end>§§§
```

*Note that this requires `wget` to be installed on your machine*


## Examples

Below you can find different versions for inserting different parts of the file 
`examples/plotting/plot_rocs.py` into your markdown file.

| Placeholder | Result |
|-------------|--------|
|`§§§examples/file.py§§§` | whole file |
|`§§§examples/file.py::§§§` | whole file |
|`§§§examples/file.py:10:20§§§` | from line 10 to line 20 |
|`§§§examples/file.py::10§§§` | from top to line 10 |
|`§§§examples/file.py:10§§§` | from line 10 to bottom |
|`§§§examples/file.py:10:§§§` | from line 10 to bottom |

## Installation

`cora` can simply be installed using `pip install`:

```bash
pip install cora
# or
pip install https://github.com/umami-hep/cora/archive/master.tar.gz