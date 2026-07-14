
import streamlit as st, random
from player import init
from data import NPC
from shop import show
init()
page=st.sidebar.radio("메뉴",["학교","상점","NPC"])
st.title("🎮 야다의 모험")
st.write(f"❤️{st.session_state.hp} ⚔{st.session_state.atk} 🍞포켓몬빵 {st.session_state.bread}")
if page=="상점":
 show()
elif page=="NPC":
 st.header("포동민호")
 q=NPC["포동민호"]
 st.write(q["question"])
 ans=st.radio("선택",q["choices"])
 if st.button("제출"):
  if ans==q["answer"]:
   st.session_state.bread+=50
   st.success("정답! 포켓몬빵 +50")
  else: st.error("틀렸다!")
else:
 acts=[
 ("📚 공부 (+10공부,+2~5🍞)","study"),
 ("⚽ 운동 (HP+5)","ex"),
 ("😴 잠 (HP+10)","sl"),
 ("🔥 야차수색 (야차 등장↑)","hunt")
 ]
 for t,c in random.sample(acts,4):
  if st.button(t):
   if c=="study":
    st.session_state.study+=10
    st.session_state.bread+=random.randint(2,5)+st.session_state.glasses
   elif c=="ex":
    st.session_state.hp+=5+st.session_state.album
   elif c=="sl":
    st.session_state.hp=min(100,st.session_state.hp+10)
   elif c=="hunt":
    st.warning("야차 등장! (전투 시스템 구현 예정)")
   st.rerun()
