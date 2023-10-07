#!/usr/bin/python3

################################################################################
# Sets are similar to lists, but are unordered and cannot contain duplications #
################################################################################

my_set = {1,2,3,4,5,6,5,4,3}
print(my_set)
my_set.add(7)
print(my_set)
my_set.update({8,9})
print(my_set)
my_set.clear()
print(my_set)

#################################################################
# Tuples are used to store multiple items in a single variable  #
# A tuple is a collection which is ordered and unchangeable     #
#################################################################

my_tuple = ("a", "b", "c")
print(my_tuple)
