import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
data=pd.read_csv('train.csv')
st.title('Prediksi Kelulusan Mahasiswa')
st.write(data.head())
X=data[['Umur','Jam_Belajar','Absensi','Nilai_Ujian']]
y=data['Lulus']
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.2,random_state=42)
m=RandomForestClassifier(random_state=42)
m.fit(Xtr,ytr)
st.success(f'Akurasi: {accuracy_score(yte,m.predict(Xte))*100:.2f}%')
u=st.number_input('Umur',18,30,20)
j=st.number_input('Jam Belajar',0,10,2)
a=st.number_input('Absensi',0,100,80)
n=st.number_input('Nilai Ujian',0,100,75)
if st.button('Prediksi'):
 st.write('Lulus' if m.predict([[u,j,a,n]])[0] else 'Tidak Lulus')
