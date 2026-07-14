
import streamlit as st
def show():
 st.header("🛒 상점")
 st.write("공격력 업그레이드 : 포켓몬빵",st.session_state.atk*5)
 if st.button("⚔ 공격력 업그레이드 (+1)"):
  c=st.session_state.atk*5
  if st.session_state.bread>=c:
   st.session_state.bread-=c;st.session_state.atk+=1
 prices=[("회복 포션",20),("띠부씰 도감",50),("안경",50)]
 for n,p in prices:
  if st.button(f"{n} ({p}🍞)"):
   if st.session_state.bread>=p:
    st.session_state.bread-=p
    if n=="회복 포션": st.session_state.potions+=1
    if n=="띠부씰 도감": st.session_state.album+=1
    if n=="안경": st.session_state.glasses+=1
