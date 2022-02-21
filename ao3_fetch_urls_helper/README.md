<h1 align="center">ao3-fetch-urls-helper</h1>

A helper script for the '--fetch-urls' option of fichub_cli's metadata plugin which can be used to traverse all the pages.<br>

To report issues, open an issue at https://github.com/fichub-cli-contrib/helper-scripts/issues

# Installation

Download the scripts and run using:

```
python ao3_fetch_urls_helper.py
```

# Dependencies

This script depends on the [fichub-cli-metadata](https://github.com/fichub-cli-contrib/fichub-cli-metadata) plugin so it needs to be installed in the python environment.

# Usage

```
> python ao3_fetch_urls_helper.py
usage: ao3-fetch-urls-helper [-h] [-u URL] [--start START] [--end END] [-d]
                             [--version]

A helper script for the '--fetch-urls' option of fichub_cli's metadata plugin which can be used to traverse all the pages.

To report issues, open an issue at https://github.com/fichub-cli-contrib/helper-scripts/issues


optional arguments:
  -h, --help         show this help message and exit
  -u URL, --url URL  Input url (The url should contain 'page=' for the regex to work)
  --start START      Starting page number
  --end END          Ending page number
  -d, --debug        Show the log in the console for debugging
  --version          Display version & quit
```

---

### Notes

- The input url _must_ contain "page=" so that the regex can substitute the page number

- If you can't find the page number in your url, go to page 2 and the "page=" string should show up.

- The starting page will be 1 by default unless specified with `--start`

---

## Example

- To fetch urls with ending page number as 5 (Starting page number will be 1 by default).

```
python ao3_fetch_urls_helper.py -u https://archiveofourown.org/users/The_Carnivorous_Muffin/works --end 5
```

- To fetch urls with starting page number as 2 & ending page number as 5

```
python ao3_fetch_urls_helper.py -u https://archiveofourown.org/users/The_Carnivorous_Muffin/works --start 2 --end 5
```

# Links

- [Fichub-cli](https://github.com/FicHub/fichub-cli/)
- [Official Discord Server](https://discord.gg/sByBAhX)
