<h1 align="center">ao3-fetch-urls-helper</h1>

A helper script for the `--fetch-urls` option of fichub_cli's metadata plugin which can be used to traverse all the pages.<br>

To report issues, open an issue at https://github.com/fichub-cli-contrib/helper-scripts/issues

# Installation

## Dependencies

---

This script depends on the [fichub-cli-metadata](https://github.com/fichub-cli-contrib/fichub-cli-metadata) plugin so it needs to be installed in the python environment.

## Download

---

There are many ways to download the script:

- Using [git](https://git-scm.com/downloads):

```
git clone https://github.com/fichub-cli-contrib/helper-scripts
```

- Using [Wget](https://www.gnu.org/software/wget/):

```
wget https://raw.githubusercontent.com/fichub-cli-contrib/helper-scripts/main/ao3_fetch_urls_helper/ao3_fetch_urls_helper.py
```

- Using [curl](https://curl.se/):

```
curl -O https://raw.githubusercontent.com/fichub-cli-contrib/helper-scripts/main/ao3_fetch_urls_helper/ao3_fetch_urls_helper.py

```

- From within the browser:
  - Go to this [page](https://raw.githubusercontent.com/fichub-cli-contrib/helper-scripts/main/ao3_fetch_urls_helper/ao3_fetch_urls_helper.py)
  - Right Click and save the file using "Save Page as"
  - Make sure that the filename is `ao3_fetch_urls_helper.py`, not `.txt`

## Run

---

```

python3 ao3_fetch_urls_helper.py

```

# Usage

```

> python3 ao3_fetch_urls_helper.py
> usage: ao3-fetch-urls-helper [-h] [-u URL] [--start START] [--end END] [-d]

                             [--version]

A helper script for the '--fetch-urls' option of fichub_cli's metadata plugin which can be used to traverse all the pages.

To report issues, open an issue at https://github.com/fichub-cli-contrib/helper-scripts/issues

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Input url (The url should contain 'page=' for the regex to work)
  --start START         Starting page number
  --end END             Ending page number
  --user-contact USER_CONTACT
                        Contact email ID for user-agent. Prevents IP bans since AO3 can contact you directly if there are any issues.
  -d, --debug           Show the log in the console for debugging
  --version             Display version & quit
```

---

### Notes

- The input url _must_ contain "page=" so that the regex can substitute the page number

- If you can't find the page number in your url, go to page 2 and the "page=" string should show up.

- The starting page will be 1 by default unless specified with `--start`

- You can opt-out of not using `--user-contact` for your requests even though we advise that you should since this will ensure that if AO3 has any issues with the amount of requests you are sending, they can directly contact you to resolve the issue.

---

## Example

- To fetch urls with ending page number as 5 (Starting page number will be 1 by default).

```

python3 ao3_fetch_urls_helper.py -u https://archiveofourown.org/users/The_Carnivorous_Muffin/works --end 5 --user-contact example@gmail.com

```

- To fetch urls with starting page number as 2 & ending page number as 5

```

python3 ao3_fetch_urls_helper.py -u https://archiveofourown.org/users/The_Carnivorous_Muffin/works --start 2 --end 5 --user-contact example@gmail.com

```

# Links

- [Fichub-cli](https://github.com/FicHub/fichub-cli/)
- [Official Discord Server](https://discord.gg/sByBAhX)

```

```
