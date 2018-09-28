#!/usr/bin/env python

#python script dynamically collect birdnames the jibjib ml model is trained for
#collects names in html file as specified by task.md
#created by softbobo 26/09/2018

import os
import pickle
import time

current_date = time.ctime()
save_path = os.path.abspath(os.path.join(os.getcwd(), current_date))


dict_1 = open('bird_id_map_<version>.pickle', 'rb')
bird_id_map = pickle.load(dict_1)
dict_1.close

dict_2 = open('train_id_list_<version>.pickle', 'rb')
train_id_list = pickle.load(dict_2)
dict_2.close




