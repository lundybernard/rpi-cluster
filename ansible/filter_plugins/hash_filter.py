#! /usr/bin/python

class FilterModule(object):
    def filters(self):
        return {
            'hash_pas': self.hash_pas,
        }
 
    def hash_pas(self, a_variable):
        a_new_variable = a_variable + ' CRAZY NEW FILTER'
        return a_new_variable
