#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Utilisation MONGO
from pymongo import MongoClient # librairie qui va bien
import configparser, os

config = configparser.ConfigParser()
config.read_file(open(os.path.expanduser("~/.datalab.cnf")))

CNF = "mongo"
BDD = "Datalab"

# Ouverture connection -> mongo sur serveur
client = MongoClient('mongodb://%s:%s@%s/?authSource=%s' % (config[CNF]['user'], config[CNF]['password'], config[CNF]['host'], BDD))
client


# In[18]:


dbs = client.list_database_names() # Liste des BDD
for DBname in dbs:
    #if (DBname[:4]=="MOOC"):
    if True:
        print(DBname)
        bdd = client[DBname] # La BDD
        collecs = bdd.list_collection_names() # Collections de la BDD
        #print(collecs)
        for cn in collecs:
            col = bdd[cn]
            print("    %s: %d" % (cn, col.count()))
            cids = col.distinct('content.course_id')
            #print(cids)
            for cid in cids:
                print("        %s: %d" % (cid, col.find({'content.course_id': cid}).count()))


# In[ ]:




