# Copyright 2022 Arbaaz Laskar

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from time import sleep
from random import randint
import sys
import argparse
import re

from fichub_cli_metadata.utils.fetch_data import FetchData


def create_parser():
    parser = argparse.ArgumentParser(prog='ao3-fetch-urls-helper',
                                     description="""
A helper script for the '--fetch-urls' option of fichub_cli's metadata plugin which can be used to traverse all the pages.

To report issues, open an issue at https://github.com/fichub-cli-contrib/helper-scripts/issues
        """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-u", "--url", type=str,
                        help="Input url (The url should contain 'page=' for the regex to work)")

    parser.add_argument("--start", type=int,
                        help="Starting page number", default=1)

    parser.add_argument("--end", type=int, default=1,
                        help="Ending page number")

    parser.add_argument("--user-contact", type=str, default=None,
                        help="Contact email ID for user-agent. This ensures AO3 can contact you directly if there are any issues.")

    parser.add_argument("-d", "--debug", action='store_true',
                        help="Show the log in the console for debugging")

    parser.add_argument("--version", action='store_true',
                        help="Display version & quit")
    return parser


def main(argv=None):

    if argv is None:
        argv = sys.argv[1:]

    parser = create_parser()
    args = parser.parse_args(argv)

    # if no args is given, invoke help
    if len(argv) == 0:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.version is True:
        print("ao3_fetch_urls_helper: v0.2")
        sys.exit(0)

    # clean the url
    curr_url = args.url.replace('\\', '')

    for i in range(args.start, args.end+1):
        # replace the page number in url with start pg no.
        curr_url = re.sub(r"page=\d+", f"page={i}", curr_url)
        next_url = re.sub(r"page=\d+", f"page={i+1}", curr_url)

        fic = FetchData(debug=args.debug)
        sleep(randint(1, 5))  # random delay between each request
        fic.fetch_urls_from_page(curr_url, args.user_contact)
        curr_url = next_url  # update the curr url


if __name__ == "__main__":
    main()
