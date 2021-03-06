from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
from pymongo import MongoClient
import random
import datetime

#connecting with the mongodb cluster using the connection token
client = MongoClient('mongodb+srv://dbuser2:covac@eshop.m8tu7.mongodb.net/test')

#declaring the database
db = client['Covac']

#declaring the collections
c1 = db['centers']
c2 = db['admin']
c3 = db['patient']
c4 = db['appoinment']
c5 = db['vaccinated']

def reshedule(aid):
  st.title('Reshedule')
  today = datetime.date.today()
  tomorrow = today + datetime.timedelta(days=2)
  d1 = st.date_input('Date', tomorrow)
  d = str(d1)
  slot = st.select_slider('Time Slot',['10AM','1PM','4PM'])
  data = {'aid':aid}
  c = c4.find(data)
  for i in c:
    center = i['center']

  z = c4.find({'center':center,'date':d,'slot':slot}).count()
  st.write(str(20-z)+' slots are left')
  a = st.button('Reshedule')

  if a and z<20:
    # c4.update_one(data,{"$set":{}})
    c4.update_one(data,{"$set":{"status":'resheduled',"date":d,'slot':slot}})
    st.success('Your vaccination appoinment reshduled at '+d+' at '+slot+' slot')
  if z>=20:
    st.warning('Choose another date/slot')