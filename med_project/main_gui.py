#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Main module to run the right script with the given options
"""

import argparse
from os import path as ptah
import yaml
import med_project.expe_med_to_csv as expe
import med_project.file_med_to_csv as file
from gooey import Gooey, GooeyParser

@Gooey
def main() :
    """main function, calls expe_med_to_csv or file_med_to_csv depending on the path"""
    parser = GooeyParser(prog="med_to_csv",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("path", type=str,
                        help="""Path to the group directory which contains data files from :
                                - Medassociate""", widget="DirChooser")
    parser.add_argument("option", type=str, 
                        help= """Path to option config file.""", widget="FileChooser")
    parser.add_argument("output", type=str,   
                        help= """Path output of the csv file""", widget="FileSaver")
    # parser.add_argument("-v","--verbose", type=str, help= """Verbose mode""")

    args = parser.parse_args()
    #load user parameters
    with open(args.option, "r") as ymlfile:
        opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    parser = argparse.ArgumentParser(prog="med_to_csv",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    if ptah.isdir(args.path):
        # print(f"path={args.path}, notes={args.notes}, sortie={args.sortie}, echo={args.verbose}")
        expe.main(path=args.path, output_file = args.output, opt=opt_dic)
    else:
        df_res = file.read_path(args.path, opt_dic)
        df_res.to_csv(args.file, index=False)

if __name__ == "__main__":
    main()