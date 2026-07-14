
import streamlit as st
import random

st.set_page_config(page_title="야다의 모험", page_icon="🎮")

def init():
    ss=st.session_state
    ss.setdefault("hp",100)
    ss.setdefault("study",0)
    ss.setdefault("stress",0)
    ss.setdefault("bread",0)
    ss.setdefault("atk",1)
    ss.setdefault("point",0)
    ss.setdefault("grade",1)
    ss.setdefault("turn",1)
    ss.setdefault("boss",None)

init()

actions=[
("📚 공부","study"),("⚽ 운동","exercise"),("🍔 매점","snack"),("😴 잔다","sleep"),
("👥 친구","friend"),("🍞 상점","shop"),("🔥 야차 수색","hunt"),("🎮 게임","game")
]
bosses=[
{"name":"박재우","hp":10,"reward":5},
{"name":"이승용","hp":30,"reward":15},
{"name":"임윤아","hp":40,"reward":20},
{"name":"윤윤구","hp":150,"reward":999},
]

if "today" not in st.session_state:
    st.session_state.today=random.sample(actions,4)

st.title("🎮 야다의 모험")
c1,c2,c3=st.columns(3)
c1.metric("❤️",st.session_state.hp)
c1.metric("⚔",st.session_state.atk)
c2.metric("📚",st.session_state.study)
c2.metric("🍞",st.session_state.bread)
c3.metric("🏆",st.session_state.point)
c3.metric("🎒",f"{st.session_state.grade}학년")

if st.session_state.boss:
    b=st.session_state.boss
    st.subheader(f"🔥 {b['name']} 등장!")
    st.progress(max(b["hp"],0)/b["max"])
    st.write(f"HP : {b['hp']}/{b['max']}")
    if st.button("⚔ 공격"):
        dmg=st.session_state.atk*(2 if random.random()<0.2 else 1)
        b["hp"]-=dmg
        if b["hp"]<=0:
            if b["name"]=="윤윤구":
                st.success("🎉 윤윤구를 쓰러뜨렸다! 서울대 의대 엔딩!")
                st.stop()
            st.success(f"{b['name']} 처치! +{b['reward']}P")
            st.session_state.point+=b["reward"]
            st.session_state.boss=None
        else:
            st.session_state.hp-=random.randint(1,5)
            if st.session_state.hp<=0:
                st.error("게임 오버")
                if st.button("다시 시작"):
                    st.session_state.clear();st.rerun()
        st.rerun()
else:
    st.subheader("오늘 무엇을 할까?")
    for n,c in st.session_state.today:
        if st.button(n):
            if c=="study":
                st.session_state.study+=10
                st.session_state.stress+=5
                st.session_state.bread+=random.randint(2,5)
            elif c=="exercise":
                st.session_state.hp+=5
            elif c=="snack":
                st.session_state.hp+=3
            elif c=="sleep":
                st.session_state.hp=min(100,st.session_state.hp+10)
                st.session_state.stress=max(0,st.session_state.stress-10)
            elif c=="friend":
                pass
            elif c=="game":
                st.session_state.stress=max(0,st.session_state.stress-5)
            elif c=="shop":
                cost=st.session_state.atk*5
                if st.session_state.bread>=cost:
                    st.session_state.bread-=cost
                    st.session_state.atk+=1
                else:
                    st.warning("포켓몬빵 부족")
            elif c=="hunt" or random.random()<0.2:
                x=random.choice(bosses).copy()
                x["max"]=x["hp"]
                st.session_state.boss=x
            st.session_state.turn+=1
            if st.session_state.turn%10==0 and st.session_state.grade<3:
                st.session_state.grade+=1
            st.session_state.today=random.sample(actions,4)
            st.rerun()

if st.session_state.grade==3 and st.session_state.turn>=30 and not st.session_state.boss:
    p=st.session_state.point
    if p>=150: e="카이스트"
    elif p>=120: e="연고대"
    elif p>=80: e="서성한"
    elif p>=50: e="건동홍"
    elif p>=30: e="경기권 대학"
    elif p>=10: e="지방대"
    else: e="전문대"
    st.success(f"🎓 엔딩 : {e}")
