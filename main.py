import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.title('S.N.D. College of Engineering')

c1, blank, c2 = st.columns([1.5, 0.5, 1.5])

with c1:
    content = '''\
    SND College of Engineering & Research Center, Babhulgaon 
    established in 2006-07 is located in Yeola. Yeola is one 
    of the Taluka in Nasik district of Maharashtra. The campus 
    is spread over natural landscape of 150 Acres. The site is 
    very healthy and beautiful & being away from city atmosphere 
    is free from pollution. The city is located at 23 Km from Manmad, 35 Km from holy place, Shirdi. The nearest airport is Aurangabad. The college is situated on Yeola – Lasalgaon road 5 Km from railway station, 3 Km from Bus stand. 
    '''
    st.info(content)

with c2:
    st.image('images/clg.png')


st.write('Below are some of the moments captured and some areas of college'
         'are shown, feel free to watch it.')

c3, c4, c5 = st.columns(3)

df = pandas.read_csv('data.csv')

with c3:
    for index, row in df[:1].iterrows():
        st.title(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])

with c4:
    for index, row in df[1:2].iterrows():
        st.title(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])

with c5:
    for index, row in df[2:3].iterrows():
        st.title(row['title'])
        st.write(row['description'])
        st.image('images/'+row['image'])