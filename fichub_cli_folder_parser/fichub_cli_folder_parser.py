# Copyright 2022 Mikowmer
# Using Code that is Copyright

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import argparse

from fichub_cli.utils.fetch_data import FetchData
from fichub_cli.utils.processing import get_format_type


def create_parser():
    """Argument Parser for fichub_cli_url_parser"""
    parser = argparse.ArgumentParser(prog='fichub-cli-url-parser',
                                     description="""
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
        """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-i", "--infile", type=str,
                        help="File location for the text file to download the fics from.")

    parser.add_argument("-v", "--verbose", action='store_true',
                        help="Verbose")

    parser.add_argument("-o", "--out-dir", default='.', type=str,
                        help="Path to the Output directory for files (default: Current Directory)")

    parser.add_argument("--format", default="epub", type=str,
                        help="Download Format: epub (default), mobi, pdf or html")

    parser.add_argument("--force", action='store_true',
                        help="Force overwrite of an existing file")

    parser.add_argument("-d", "--debug", action='store_true',
                        help="Show the log in the console for debugging")

    parser.add_argument("--version", action='store_true',
                        help="Display version and quit")
    return parser


def txt_file_parser(filename, debug):
    """Parses a text file such that fics can be output to the appropriate folders"""
    try:
        with open(filename, 'r') as f:
            urls = f.read().splitlines()

    except FileNotFoundError:
        print("file could not be found. Please enter a valid file path.")
        exit(1)

    folders = {'': []}
    current_folder = folders['']
    current_path_list = ['']
    current_path_str = '/'
    current_depth = 0
    past_depth = 0

    for i, line in enumerate(urls):
        if line[0] == '#':
            current_depth = 0
            for char in line:
                if char == '#':
                    current_depth += 1
            if current_depth > past_depth:
                past_depth += 1
                if past_depth != current_depth:
                    raise RuntimeError(
                        f'You have jumped from folder level {past_depth - 1} to {current_depth} at line {i} in '
                        f'{filename}. Please correct this, and try again.'
                    )
                current_path_list.append('')
            while current_depth < past_depth:
                past_depth -= 1
                current_path_list.pop()
            current_path_list[current_depth] = line[current_depth:]

            current_path_str = ''
            for j in range(current_depth + 1):
                current_path_str += current_path_list[j] + '/'

            folders[current_path_str] = []
            current_folder = folders[current_path_str]
        else:
            current_folder.append(line)

    return folders


def main(argv=None):

    print(sys.argv)

    if argv is None:
        argv = sys.argv[1:]

    parser = create_parser()
    args = parser.parse_args(argv)

    # if no args is given, invoke help
    if len(argv) == 0:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.version is True:
        print("fichub_cli_url_parser: v0.1")
        sys.exit(0)

    format_type = get_format_type(args.format)
    out_dir = args.out_dir[:-1] if args.out_dir[-1] == "/" else args.out_dir
    force = args.force
    debug = args.debug
    automated = False
    verbose = args.verbose

    url_lists = txt_file_parser(args.infile, debug)

    dwnld_fail = False

    for directory in url_lists:
        if verbose:
            print(f"Folder: {directory}")
        tmp_out_dir = out_dir + directory

        try:
            os.mkdir(tmp_out_dir)
        except FileExistsError:
            pass

        fic = FetchData(format_type, tmp_out_dir, force,
                        debug, automated, verbose)

        url_list = url_lists[directory]

        if not url_list:
            continue

        url_str = url_list[0]

        for url in url_list[1:]:
            url_str += ',' + url

        fic.get_fic_with_list(url_str)

        if fic.exit_status == 1:
            dwnld_fail = True
            with open('err.log', 'a') as f:
                f.write('#' + directory[1:-1] + '\n')

    if dwnld_fail is True:
        print("Download failed for one or more urls! Check err.log in the current directory!")


if __name__ == '__main__':
    main()
