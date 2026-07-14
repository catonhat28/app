
import streamlit as st
def init():
 s=st.session_state
 d={"hp":100,"atk":1,"bread":0,"study":0,"potions":0,"glasses":0,"album":0,"points":0}
 for k,v in d.items(): s.setdefault(k,v)
