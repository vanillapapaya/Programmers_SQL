#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Apr 26 2020

@author: vanillapapaya

"""
import pymysql
import csv
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


#print("Please Enter your MySQL root Password")
#password = input()

#engine = create_engine("mysql+mysqldb://root:" + password
#                       + "@192.168.0.2/covid", encoding = 'utf-8')

engine = create_engine("mysql+mysqldb://root:" + "qhans7810!"
                       + "@192.168.0.2/AAC", encoding = 'utf-8')

conn = engine.connect()

ANIMAL_INS = pd.read_csv("../DATA/aac_intakes.csv").sort_values(by = "animal_id").reset_index()
ANIMAL_OUTS = pd.read_csv("../DATA/aac_outcomes.csv").sort_values(by = "animal_id").reset_index()

ANIMAL_INS["animal_id_num"] = ANIMAL_INS["animal_id"].str.replace("A", "").apply(pd.to_numeric)
ANIMAL_INS = ANIMAL_INS[(ANIMAL_INS["animal_id_num"] >= 349996) & (ANIMAL_INS["animal_id_num"] <= 414513)].drop_duplicates(subset = "animal_id", keep = "first")
ANIMAL_OUTS["animal_id_num"] = ANIMAL_OUTS["animal_id"].str.replace("A", "").apply(pd.to_numeric)
ANIMAL_OUTS = ANIMAL_OUTS[(ANIMAL_OUTS["animal_id_num"] >= 349480) & (ANIMAL_OUTS["animal_id_num"] <= 412626)].drop_duplicates(subset = "animal_id", keep = "first")

ANIMAL_INS[["animal_id", "animal_type", "datetime", "intake_condition", "name", "sex_upon_intake"]].to_sql(name = "ANIMAL_INS", con = engine, if_exists = 'replace')
ANIMAL_OUTS[["animal_id", "animal_type", "datetime", "name", "sex_upon_outcome"]].to_sql(name = "ANIMAL_OUTS", con = engine, if_exists = 'replace')