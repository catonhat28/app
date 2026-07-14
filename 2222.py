import streamlit as st


def init_player():

    default = {

        "hp": 100,
        "max_hp": 100,

        "study": 0,
        "stress": 0,
        "popularity": 0,

        "pokemon_bread": 0,

        "attack": 1,

        "grade": 1,
        "day": 1,

        "yacha_point": 0,

        "potion": 0,
        "glasses": 0,
        "album": 0,

        "current_boss": None,

        "boss_hp": 0,

        "inventory": [],

        "dead": False,

        "ending": "",

        "final_clear": False

    }

    for key, value in default.items():

        if key not in st.session_state:
            st.session_state[key] = value


def next_day():

    st.session_state.day += 1

    if st.session_state.day > 30:

        st.session_state.day = 1

        if st.session_state.grade < 3:

            st.session_state.grade += 1


def heal(amount):

    st.session_state.hp += amount

    if st.session_state.hp > st.session_state.max_hp:

        st.session_state.hp = st.session_state.max_hp


def damage(amount):

    st.session_state.hp -= amount

    if st.session_state.hp <= 0:

        st.session_state.hp = 0
        st.session_state.dead = True


def add_bread(amount):

    st.session_state.pokemon_bread += amount


def use_bread(amount):

    if st.session_state.pokemon_bread >= amount:

        st.session_state.pokemon_bread -= amount

        return True

    return False


def add_attack():

    st.session_state.attack += 1


def add_study(amount):

    bonus = 0

    if st.session_state.glasses:

        bonus = 3

    st.session_state.study += amount + bonus


def add_hp(amount):

    bonus = 0

    if st.session_state.album:

        bonus = 3

    heal(amount + bonus)


def add_point(amount):

    st.session_state.yacha_point += amount


def give_potion():

    st.session_state.potion += 1


def use_potion():

    if st.session_state.potion > 0:

        st.session_state.potion -= 1

        heal(30)

        return True

    return False


def buy_glasses():

    st.session_state.glasses = 1


def buy_album():

    st.session_state.album = 1


def game_over():

    return st.session_state.dead


def status():

    return {

        "hp": st.session_state.hp,

        "study": st.session_state.study,

        "bread": st.session_state.pokemon_bread,

        "attack": st.session_state.attack,

        "grade": st.session_state.grade,

        "day": st.session_state.day,

        "point": st.session_state.yacha_point,

        "stress": st.session_state.stress,

        "popularity": st.session_state.popularity,

        "potion": st.session_state.potion

    }


def reset():

    st.session_state.clear()
