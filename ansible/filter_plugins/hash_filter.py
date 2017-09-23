#! /usr/bin/python

import crypt

class FilterModule(object):
    def filters(self):
        return {
            'hash_pas': self.hash_pas,
        }
 
    def hash_pas(self, password):
        return crypt.crypt(password, "$6$random_salt")
