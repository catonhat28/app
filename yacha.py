# ==========================
# data.py
# 야다의 모험 데이터
# ==========================

import random

# --------------------------
# 야차
# --------------------------

BOSSES = [
    {
        "name": "박재우",
        "hp": 10,
        "attack": 2,
        "reward": 5,
        "bread": 3,
        "description": "야차계의 최약체."
    },
    {
        "name": "이승용",
        "hp": 30,
        "attack": 4,
        "reward": 15,
        "bread": 8,
        "description": "생각보다 강하다."
    },
    {
        "name": "임윤아",
        "hp": 40,
        "attack": 5,
        "reward": 20,
        "bread": 10,
        "description": "강력한 야차."
    },
    {
        "name": "윤윤구",
        "hp": 150,
        "attack": 10,
        "reward": 999,
        "bread": 50,
        "description": "최종보스"
    }
]

# --------------------------
# NPC
# --------------------------

NPCS = {
    "포동민호": {
        "question": "내가 먹은 마쉬멜로우 개수는?",
        "choices": [
            "1개",
            "5개",
            "7개",
            "999개"
        ],
        "answer": "999개",
        "reward": 50
    }
}

# --------------------------
# 상점
# --------------------------

SHOP_ITEMS = [
    {
        "id": "atk",
        "name": "⚔ 공격력 업그레이드",
        "price": 5,
        "description": "공격력 +1"
    },
    {
        "id": "potion",
        "name": "🧪 회복 포션",
        "price": 20,
        "description": "전투 중 HP 30 회복"
    },
    {
        "id": "album",
        "name": "📕 띠부씰 도감",
        "price": 50,
        "description": "운동 효율 +3"
    },
    {
        "id": "glasses",
        "name": "👓 안경",
        "price": 50,
        "description": "공부 효율 +3"
    }
]

# --------------------------
# 행동
# --------------------------

ACTIONS = [
    {
        "title": "📚 공부",
        "code": "study",
        "effect": "공부 +10 / 포켓몬빵 +2~5"
    },
    {
        "title": "⚽ 운동",
        "code": "exercise",
        "effect": "HP +5"
    },
    {
        "title": "😴 잠",
        "code": "sleep",
        "effect": "HP +10 / 스트레스 -10"
    },
    {
        "title": "🍔 매점",
        "code": "snack",
        "effect": "HP +3"
    },
    {
        "title": "👥 친구와 놀기",
        "code": "friend",
        "effect": "인기도 +10"
    },
    {
        "title": "🔥 야차 수색",
        "code": "hunt",
        "effect": "야차 등장 확률 매우 높음"
    },
    {
        "title": "🛒 상점",
        "code": "shop",
        "effect": "상점으로 이동"
    },
    {
        "title": "🎮 게임",
        "code": "game",
        "effect": "스트레스 -5"
    }
]

# --------------------------
# 대학 엔딩
# --------------------------

def get_university(points, defeated_final_boss=False):
    if defeated_final_boss:
        return "🏆 서울대학교 의과대학"

    if points >= 150:
        return "KAIST"

    if points >= 120:
        return "연세대 / 고려대"

    if points >= 80:
        return "서강대 / 성균관대 / 한양대"

    if points >= 50:
        return "건국대 / 동국대 / 홍익대"

    if points >= 30:
        return "경기권 대학"

    if points >= 10:
        return "지방 국립대"

    return "전문대"

# --------------------------
# 랜덤 행동
# --------------------------

def random_actions():
    return random.sample(ACTIONS, 4)

# --------------------------
# 랜덤 야차
# --------------------------

def random_boss():
    return random.choice(BOSSES).copy()
