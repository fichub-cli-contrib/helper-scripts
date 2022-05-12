<h1 align="center">fichub-cli-folder-parser</h1>

A helper script for the `--fetch-urls` option of fichub_cli's metadata plugin which can be used to traverse all the pages.<br>

To report issues, open an issue at https://github.com/fichub-cli-contrib/helper-scripts/issues

# Installation

## Dependencies

This script depends on the [fichub-cli-metadata](https://github.com/fichub-cli-contrib/fichub-cli-metadata) plugin so it needs to be installed in the python environment.

## Download

There are many ways to download the script:

- Using [git](https://git-scm.com/downloads):

```
git clone https://github.com/fichub-cli-contrib/helper-scripts
```

- Using [Wget](https://www.gnu.org/software/wget/):

```
wget https://raw.githubusercontent.com/fichub-cli-contrib/helper-scripts/main/fichub_cli_folder_parser/fichub_cli_folder_parser.py
```

- Using [curl](https://curl.se/):

```
curl -O https://raw.githubusercontent.com/fichub-cli-contrib/helper-scripts/main/fichub_cli_folder_parser/fichub_cli_folder_parser.py
```

- From within the browser:
  - Go to this [page](https://raw.githubusercontent.com/fichub-cli-contrib/helper-scripts/main/fichub_cli_folder_parser/fichub_cli_folder_parser.py)
  - Right Click and save the file using "Save Page as"
  - Make sure that the filename is `fichub_cli_folder_parser.py`, not `.txt`

## Run

```
python3 fichub_cli_folder_parser.py
```

# Usage

```
> python3 fichub_cli_folder_parser.py
> usage: fichub-cli-url-parser [-h] [-i INFILE] [-v] [-o OUT_DIR]
                             [--format FORMAT] [--force] [-d] [--version]

A helper script for for fichub-cli which can be used to separate urls in a text file into folders for easier archival.
Replaces the '-i' and '--infile' options for fichub-cli.

To report issues, open an issue at https://github.com/fichub-cli-contrib/helper-scripts/issues

To use:
To mark a new folder, use a newline with '#' as the first character. To nest folders, use multiple '#'.

For example:

url1
url2
#folder1
url3
url4
#folder2
url5
##folder3
url6
#folder4
url7

Will produce a folder structure as follows:
./
├─ fic1
├─ fic2
├─ folder1/
│  ├─ fic3
│  ├─ fic4
├─ folder2/
│  ├─ fic5
│  ├─ folder3/
│  │  ├─ fic6
├─ folder4/
│  ├─ fic7

Do note that you need to only go one nest at a time, i.e. don't go from level 1 to level 3 like this:
#folder1
###folder3

This will raise an error and stop the script. 
        

options:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        File location for the text file to download the fics from.
  -v, --verbose         Verbose
  -o OUT_DIR, --out-dir OUT_DIR
                        Path to the Output directory for files (default: Current Directory)
  --format FORMAT       Download Format: epub (default), mobi, pdf or html
  --force               Force overwrite of an existing file
  -d, --debug           Show the log in the console for debugging
  --version             Display version and quit
```

---

### Notes

- Do be aware that you must set up the folder structure in a sensible manner. If you go from 1 folder deep to 3 folders deep in a single line, because you haven't defined the intervening folder structure the script will raise an error and exit.

---

## Example

- To fetch urls and place them in multiple folders, you can set up a text file as follows:

```
https://m.fanfiction.net/s/12853431/1/Transformers-RWBY-The-Flames-of-Redemption
#Star Craft
https://forums.spacebattles.com/threads/when-in-doubt-blame-q-star-trek-starcraft-cross.971242/
#Harry Potter
https://www.fanfiction.net/s/13915969/1/Harry-Potter-and-the-Phoenix-Wand
##Enter the Dragon
https://www.fanfiction.net/s/5585493/1/Enter-the-Dragon
https://www.fanfiction.net/s/12069854/1/Sort-the-Dragon
https://forum.questionablequesting.com/threads/enter-the-dragon-harry-potter-shadowrun.7861/
#Other
https://forums.sufficientvelocity.com/threads/a-dance-of-wyverns-original-victorian-england.86874/
```

- To execute the script, with a text file called 'List of Fics.txt', run:

```
python3 fichub_cli_folder_parser.py -i "List of Fics.txt"
```

# Links

- [Fichub-cli](https://github.com/FicHub/fichub-cli/)
- [Official Discord Server](https://discord.gg/sByBAhX)
