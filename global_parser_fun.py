#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Module used by the two selector"""

from os import pathconf
from typing import Dict, List
from numpy import nan

def global_selector(lst_dic:List[Dict], infos_opt:Dict) -> List[Dict]:
    """ TODO WRITE DOC here"""
    out_lst = []
    path_file = infos_opt["path_file"]
    for dicexperience in lst_dic :
        if "eval" in infos_opt.keys() :
            for key, val in infos_opt["eval"].items() :
                dicexperience[key] = eval(val)
        if "cut" in infos_opt.keys() :
            for lst_tmp in infos_opt["cut"]:
                keys=lst_tmp[0]
                sep=lst_tmp[1]
                sep_names = lst_tmp[2:]
                res_sep=[i.rsplit(sep) for i in dicexperience[keys]]
                #Ajout des elements splité
                dicexperience[sep_names[0]] = [i[0] for i in res_sep]
                dicexperience[sep_names[1]] = [i[1] if len(i)!= 1 else nan for i in res_sep]
        out_lst.append(dicexperience.copy())
    return out_lst