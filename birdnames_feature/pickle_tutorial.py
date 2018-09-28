#!/usr/bin/env python

#tutorial for pickling and unpickling data to better understand the workflow
#to be deleted upon completion
#softbobo 27/09/2018
import os
import pickle

# save_path = os.getcwd
# dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

filename = 'dogs.pickle'
# outfile = open(filename, 'wb')
# pickle.dump(dogs_dict,outfile)
# outfile.close()

infile = open(filename, 'rb')
new_dict = pickle.load(infile)

infile.close()

print(new_dict)


