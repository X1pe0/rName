#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from random import randint
from collections import defaultdict
rstring = randint(2, 10001)
columns = defaultdict(list)
with open('data') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items(): 
            columns[k].append(v) 
print('\n' + columns['nameset'][rstring] + ' ' + columns['gender'][rstring] + '\n' + columns['title'][rstring] + ' ' + columns['givenname'][rstring] + ' ' + columns['middleinitial'][rstring] + ' ' + columns['maidenname'][rstring] + '\n' + columns['streetaddress'][rstring] + '\n' + columns['city'][rstring] + ' ' + columns['statefull'][rstring] + ' ' + columns['state'][rstring] + ' ' + columns['zipcode'][rstring] + '\n\nEmail: ' + columns['emailaddress'][rstring] + '\nUsername: ' + columns['username'][rstring] + '\nPassword: ' + columns['password'][rstring] + '\nPhone: ' + columns['telephonenumber'][rstring] + '\n\nBrowser: ' + columns['browseruseragent'][rstring] + '\nBirthday: ' + columns['birthday'][rstring] + '\nAge: ' + columns['age'][rstring] + '\n' + columns['cctype'][rstring] + ': ' + columns['ccnumber'][rstring] + '\nCVV: ' + columns['cvv2'][rstring] + '\nExires: ' + columns['ccexpires'][rstring] + '\nSSN: ' + columns['nationalid'][rstring] + '\n\nJob: ' + columns['occupation'][rstring] + '\nCompany: ' + columns['company'][rstring] + '\nVehicle: ' + columns['vehicle'][rstring] + '\nBlood Type: ' + columns['bloodtype'][rstring] + '\nWeight: ' + columns['pounds'][rstring] + '\nHeight: ' + columns['feetinches'][rstring] + '\n')