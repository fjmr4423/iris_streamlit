import tweepy
from datetime import datetime,timezone
import pytz
import pandas as pd
import streamlit as st
import plotly.express as px

consumer_key        = 'ZJe3WYnIBpXMh8qrciZmot1Sc'
consumer_secret     = 'gCGnokznInvpEfwOQB3WZ7Kl88pCLLbyAXJLPZslkvYkuVdi8Y'
access_token        = '1589515664741797888-mpG3vBxTP5bFqT2sM4YGSuFkdPij7A'
access_token_secret = 'VLy4ykppZIGGEPr9QS1Hxk8YnHTEd1pmEHINEGPrhx9Le'

#Twitterの認証
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#ファイルアップロード
st.sidebar.markdown("### csvファイルを入力してください")
uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files= False)
if uploaded_files:
    df = pd.read_csv(uploaded_files)
    st.dataframe(df[df['フォロワー数']>1000])
st.write(len(df[df['フォロワー数']>1000]))

df2 = df[df['フォロワー数']>1000]
list_sample = df2['ID'].to_list()
st.write(list_sample)
st.write(len(df2))

st.write(list_sample[0])

#-------------------------------------------------------------------------
text = st.text_area(label='メッセージ本文を入力してください。', value='',)
send_no = st.sidebar.text_area(label='リストのどの範囲を送付するか', value='',)
#-------------------------------------------------------------------------

if st.sidebar.button(label='DM一斉送信'):
    for i in range(0,99):
        recipient_id = "558430461"
        api.send_direct_message(recipient_id=recipient_id, text = text)

#ここからrecipient_idが調べられる　⇨ https://idtwi.com/

