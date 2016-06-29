#!/usr/bin/env python

parser = argparse.ArgumentParser(description="Script standardization of file and folder,paths. The script checks the current date and organizes backups of folders and releases according to the date prior to the current day (without compromising the work), and generating log in /var/log/orgfolders/orgfolders.log.")

parser.add_argument("integers", metavar="-v", type=int, nargs="+" ,
        help="Verbose mode")

args = parser.parse_args()
print args.accumulate(args.integers)

