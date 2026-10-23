"""Generate data/ground_truth/people.json and external.json. Every quote is checked by data/validate.py."""
import json, sys, os

GT = sys.argv[1]


def ev(mid, quote):
    return {"message_id": mid, "quote": quote}


def fact(fid, text, *evs):
    return {"id": fid, "text": text, "evidence": list(evs)}


def edge(to, to_name, typ, *evs):
    return {"to": to, "to_name": to_name, "type": typ, "evidence": list(evs)}


def addr(context, value, *evs, honorific=False):
    return {"context": context, "value": value, "honorific": honorific, "evidence": list(evs)}


def planted(thread, n, fid):
    """Fact text lives in synthetic_relationship.jsonl; reuse its planted quote."""
    return f"syn-rel-{thread}-m{n}", fid


REL = {}
with open(os.path.join(GT, "..", "emails", "synthetic_relationship.jsonl"), encoding="utf-8") as f:
    for line in f:
        e = json.loads(line)
        for pf in e["planted_facts"]:
            REL[pf["fact_id"]] = ev(e["message_id"], pf["quote"])

P = []

# ---------------- 新增：需要敬语或特殊称呼的中文收件人 ----------------
P.append({
    "id": "wang_jianhua", "email": "wang.jianhua@example.com", "display_name": "王建华",
    "relationship": "读研时的导师（已退休）", "language": "zh",
    "core_connection": {"text": "Mia 读研时的导师，毕业后每年春节问候、寄普洱；2026 年 11 月 18 日下午要和周航师兄去家里看望他和李阿姨。",
                        "evidence": [REL["wang.f1"], REL["wang.f10"]]},
    "address_as": [addr("default", "王老师", ev("syn-rel-wang-001-m1", "王老师："), ev("syn-rel-wang-004-m1", "王老师："), honorific=True)],
    "honorific": {"uses_nin": True, "evidence": [ev("syn-rel-wang-001-m1", "您好！新年快要到了"), ev("syn-rel-wang-004-m2", "您不用特意准备")]},
    "sign_off": {"value": "学生 Mia 敬上", "evidence": [ev("syn-rel-wang-001-m1", "学生 Mia 敬上"), ev("syn-rel-wang-003-m1", "学生 Mia 敬上")]},
    "facts": [
        fact("wang.f1", "王老师是 Mia 读研时在实验室的导师", REL["wang.f1"]),
        fact("wang.f2", "王老师爱喝普洱，Mia 给他寄过云南老普洱", REL["wang.f2"]),
        fact("wang.f3", "王老师的教导：先把问题定义清楚，再动手", REL["wang.f3"]),
        fact("wang.f4", "李阿姨（王老师夫人）当年常给学生包饺子", REL["wang.f4"]),
        fact("wang.f5", "王老师退休后每天练书法，在老年大学开了小班", REL["wang.f5"]),
        fact("wang.f6", "王老师想了解现在的 AI 能做什么", REL["wang.f6"]),
        fact("wang.f7", "王老师想把书法作品拍照整理成小册子", REL["wang.f7"]),
        fact("wang.f8", "Mia 2026 年 11 月中旬回北京两周，要去家里看望", REL["wang.f8"]),
        fact("wang.f9", "周航师兄也要一起去看望王老师", REL["wang.f9"]),
        fact("wang.f10", "已约定 11 月 18 日下午三点左右去王老师家", REL["wang.f10"]),
    ],
    "edges": [
        edge("person:li_ayi", "李阿姨", "spouse", REL["wang.f4"]),
        edge("hang.zhou@example.com", "周航", "former_student", REL["wang.f5"]),
        edge("mia", "Mia", "former_student", REL["wang.f1"]),
    ],
    "external": ["ext-wang-1"],
})

P.append({
    "id": "tang_shuyuan", "email": "tang.shuyuan@example.com", "display_name": "唐书远",
    "relationship": "Victor 的大学室友，家庭朋友；华人文化节组委会负责人", "language": "zh",
    "core_connection": {"text": "Victor 大学时睡上下铺的室友，两家常一起烧烤吃饭；Mia 在他负责的华人文化节（2026-09-26）做志愿者。",
                        "evidence": [REL["tang.f2"], REL["tang.f6"]]},
    "address_as": [
        addr("private", "老唐", ev("syn-rel-tang-001-m1", "老唐"), ev("syn-rel-tang-002-m1", "老唐"), ev("syn-rel-tang-007-m1", "老唐")),
        addr("default", "书远", ev("syn-rel-tang-003-m1", "书远，"), ev("syn-rel-tang-006-m1", "书远，")),
        addr("formal", "唐书远老师", ev("syn-rel-tang-004-m1", "唐书远老师："), ev("syn-rel-tang-005-m1", "唐书远老师："), honorific=True),
    ],
    "honorific": {"uses_nin": "formal_only", "evidence": [ev("syn-rel-tang-004-m1", "感谢您和组委会的信任"), ev("syn-rel-tang-005-m1", "请您审阅")]},
    "sign_off": {"value": None, "by_context": {"private": None, "default": "Mia", "formal": "Mia Song"},
                 "evidence": [ev("syn-rel-tang-004-m1", "此致\n敬礼\n\nMia Song"), ev("syn-rel-tang-006-m1", "拿不准。\n\nMia")]},
    "facts": [
        fact("tang.f1", "妻子苏晴，聚会时负责甜点", REL["tang.f1"]),
        fact("tang.f2", "和 Victor 大学睡上下铺", REL["tang.f2"]),
        fact("tang.f3", "女儿朵朵，在找中文学校", REL["tang.f3"]),
        fact("tang.f4", "Mia 把林小雨介绍给他问中文学校", REL["tang.f4"]),
        fact("tang.f5", "华人文化节组委会负责人", REL["tang.f5"]),
        fact("tang.f6", "华人文化节在 9 月 26 日", REL["tang.f6"]),
        fact("tang.f7", "Mia 在文化节负责签到台，上午 9:00 到 12:00", REL["tang.f7"]),
        fact("tang.f8", "Mia 做了文化节宣传海报（中英双语）", REL["tang.f8"]),
        fact("tang.f9", "私下会请他帮忙看海报颜色", REL["tang.f9"]),
        fact("tang.f10", "苏晴做的桂花糕在文化节被抢光", REL["tang.f10"]),
    ],
    "edges": [
        edge("person:victor", "Victor", "college_roommate", REL["tang.f2"]),
        edge("person:su_qing", "苏晴", "spouse", REL["tang.f1"]),
        edge("person:duoduo", "朵朵", "child", REL["tang.f3"]),
        edge("xiaoyu.lin@example.com", "林小雨", "introduced_by_mia", REL["tang.f4"]),
    ],
    "external": ["ext-tang-1"],
})

P.append({
    "id": "zhao_liqun", "email": "zhao.liqun@example.com", "display_name": "赵立群",
    "relationship": "前老板（上海，公司创始人）", "language": "zh",
    "core_connection": {"text": "Mia 在他团队工作过三年，做过第一版推荐系统；现在仍保持联系：2026 年夏天帮他女儿雨桐在湾区落脚，10 月 30 日给他公司做线上分享。",
                        "evidence": [REL["zhao.f1"], REL["zhao.f8"]]},
    "address_as": [addr("default", "赵总", ev("syn-rel-zhao-001-m1", "赵总："), ev("syn-rel-zhao-004-m1", "赵总："), honorific=True)],
    "honorific": {"uses_nin": True, "evidence": [ev("syn-rel-zhao-001-m1", "给您和家人拜个早年"), ev("syn-rel-zhao-003-m2", "您放心")]},
    "sign_off": {"value": "Mia", "evidence": [ev("syn-rel-zhao-002-m1", "我请您吃饭")]},
    "facts": [
        fact("zhao.f1", "Mia 在他团队工作过三年", REL["zhao.f1"]),
        fact("zhao.f2", "他带团队做过第一版推荐系统", REL["zhao.f2"]),
        fact("zhao.f3", "以前在上海常去吃早茶，喜欢粤菜", REL["zhao.f3"]),
        fact("zhao.f4", "2025 年 9 月来湾区开会，和 Mia 吃过饭", REL["zhao.f4"]),
        fact("zhao.f5", "他的建议：小团队先把一个场景做透", REL["zhao.f5"]),
        fact("zhao.f6", "女儿雨桐 2026 年暑假来湾区参加夏令营", REL["zhao.f6"]),
        fact("zhao.f7", "Victor 去机场接的雨桐", REL["zhao.f7"]),
        fact("zhao.f8", "Mia 10 月 30 日晚上给他公司做线上分享", REL["zhao.f8"]),
    ],
    "edges": [
        edge("person:zhao_yutong", "雨桐", "child", REL["zhao.f6"]),
        edge("mia", "Mia", "former_manager_of", REL["zhao.f1"]),
    ],
    "external": ["ext-zhao-1"],
})

# ---------------- 现有人物（事实全部来自 emails.jsonl） ----------------
P.append({
    "id": "ethan_park", "email": "ethan.park@example.com", "display_name": "Ethan Park",
    "relationship": "Mia 和 Victor 的教练（coaching sessions）", "language": "en",
    "core_connection": {"text": "Mia 的教练，也给 Victor 上课；Mia 总想线下见，常约 Red Rock Coffee 或 Starbucks。",
                        "evidence": [ev("19ad08024b9953ee", "coaching session?"), ev("19877bc1b9e23b00", "would you be open to meeting in person at Red Rock")]},
    "address_as": [addr("default", "Ethan", ev("199e0f4032bd1990", "Hey Ethan,"), ev("19ad08024b9953ee", "Hi Ethan,"))],
    "honorific": {"uses_nin": False, "evidence": []},
    "sign_off": {"value": "Mia", "evidence": [ev("19a7f7dcc18e3131", "See you soon\n\nMia")]},
    "facts": [
        fact("ethan.f1", "Ethan 是 Mia 的教练", ev("19ad08024b9953ee", "coaching session?")),
        fact("ethan.f2", "Ethan 也给 Victor 上课", ev("198af30eb0ec850f", "I noticed your meeting with Victor wraps up around 2pm."), ev("199e38acd7fedecd", "before or after Victor's session today")),
        fact("ethan.f3", "常在 Red Rock Coffee 见面", ev("198ab7139243711d", "see you tomorrow at Red Rock!"), ev("19877bc1b9e23b00", "would you be open to meeting in person at Red Rock")),
        fact("ethan.f4", "Maple Village 有一家 Starbucks 对双方都方便", ev("19a46d93cabaa53e", "Starbucks sounds great — there’s actually one at Maple Village")),
        fact("ethan.f5", "Mia 偏好线下见面", ev("19de5186aaeb9ed5", "Are you available to meet offline?")),
    ],
    "edges": [
        edge("mia", "Mia", "coach_of", ev("19ad08024b9953ee", "coaching session?")),
        edge("person:victor", "Victor", "coach_of", ev("198af30eb0ec850f", "I noticed your meeting with Victor wraps up around 2pm.")),
    ],
    "external": ["ext-ethan-1", "ext-ethan-2"],
})

P.append({
    "id": "julien_moreau", "email": "julien.moreau@example.com", "display_name": "Julien Moreau",
    "relationship": "老朋友，在首尔工作的法国人，指导过 ShopPilot", "language": "en",
    "core_connection": {"text": "一起去过里斯本的老朋友，曾指导 Mia 的 ShopPilot 项目；现在在首尔，跨时区约视频。",
                        "evidence": [ev("1978b9a014deb894", "the ShopPilot project you helped mentor"), ev("syn-old_friend_catchup-001-m1", "Lisbon trip last week and thought of you")]},
    "address_as": [addr("default", "Julien", ev("1978b9a014deb894", "Hi Julien,"), ev("199649c298edd6b1", "Hey Julien,"))],
    "honorific": {"uses_nin": False, "evidence": []},
    "facts": [
        fact("julien.f1", "在韩国的新公司工作", ev("1978b9a014deb894", "how’s life in Korea and the new company treating you?")),
        fact("julien.f2", "指导过 ShopPilot 项目", ev("1978b9a014deb894", "the ShopPilot project you helped mentor")),
        fact("julien.f3", "跑过春川半马", ev("syn-old_friend_catchup-008-m1", "How did the half marathon in Chuncheon go?")),
        fact("julien.f4", "伴侣 Claire 上韩语课", ev("syn-old_friend_catchup-015-m1", "Is Claire still doing the")),
        fact("julien.f5", "和 Mia 一起去过里斯本", ev("syn-old_friend_catchup-001-m1", "Lisbon trip last week and thought of you")),
    ],
    "edges": [edge("person:claire", "Claire", "partner", ev("syn-old_friend_catchup-015-m1", "Is Claire still doing the"))],
    "external": ["ext-julien-1"],
})

P.append({
    "id": "zhou_hang", "email": "hang.zhou@example.com", "display_name": "周航",
    "relationship": "中文朋友，读研时的同门师兄，常聊 AI 工具", "language": "zh_en_mixed",
    "core_connection": {"text": "王老师门下的师兄，现在常和 Mia 聊 Claude Code、MCP 和 prompt，一起爬 Mission Peak。",
                        "evidence": [REL["wang.f5"], ev("syn-zh_en_casual-011-m1", "现在基本都是 Claude Code 了")]},
    "address_as": [addr("default", "周航", ev("syn-zh_en_casual-001-m1", "周航"))],
    "honorific": {"uses_nin": False, "evidence": []},
    "facts": [
        fact("zhou.f1", "一起爬 Mission Peak", ev("syn-zh_en_casual-004-m1", "走！几点停车场集合？")),
        fact("zhou.f2", "向 Mia 请教 Blender MCP", ev("syn-zh_en_casual-001-m1", "装一个 blender-mcp 的 plugin 然后 Claude 连上就行")),
        fact("zhou.f3", "讨论 Cursor 和 Claude Code", ev("syn-zh_en_casual-011-m1", "现在基本都是 Claude Code 了")),
    ],
    "edges": [edge("wang.jianhua@example.com", "王建华", "student_of", REL["wang.f5"])],
    "external": [],
})

P.append({
    "id": "lin_xiaoyu", "email": "xiaoyu.lin@example.com", "display_name": "林小雨",
    "relationship": "中文朋友，都是妈妈，常交换旅行攻略", "language": "zh_en_mixed",
    "core_connection": {"text": "常互相要旅行攻略（京都、Maui、墨西哥城）的妈妈朋友，女儿（姐姐）爱画画。",
                        "evidence": [ev("syn-zh_en_casual-017-m1", "第一次去的话 Maui 吧"), ev("syn-zh_en_casual-016-m1", "感觉姐姐会喜欢")]},
    "address_as": [addr("default", "小雨", ev("syn-zh_en_casual-017-m1", "小雨"))],
    "honorific": {"uses_nin": False, "evidence": []},
    "facts": [
        fact("xiaoyu.f1", "家里大女儿（姐姐）喜欢画画", ev("syn-zh_en_casual-016-m1", "感觉姐姐会喜欢")),
        fact("xiaoyu.f2", "问过 Maui 还是 Big Island", ev("syn-zh_en_casual-017-m1", "第一次去的话 Maui 吧")),
        fact("xiaoyu.f3", "Mia 给她讲过京都红叶季攻略", ev("syn-zh_en_casual-007-m1", "对 我们去的就是红叶季")),
        fact("xiaoyu.f4", "Mia 推荐墨西哥城住 Roma Norte", ev("syn-zh_en_casual-019-m1", "住的 Roma Norte")),
    ],
    "edges": [edge("tang.shuyuan@example.com", "唐书远", "introduced_by_mia", REL["tang.f4"])],
    "external": ["ext-xiaoyu-1"],
})

P.append({
    "id": "hannah_kim", "email": "hannah.kim@example.com", "display_name": "Hannah Kim",
    "relationship": "老朋友，在新加坡", "language": "en",
    "core_connection": {"text": "新加坡的老朋友，Mia 每次去新加坡都约她；伴侣 Ben。",
                        "evidence": [ev("syn-old_friend_catchup-007-m1", "Did you and Ben finally settle into the")]},
    "address_as": [addr("default", "Hannah", ev("syn-old_friend_catchup-003-m1", "Hey Hannah,"))],
    "honorific": {"uses_nin": False, "evidence": []},
    "facts": [
        fact("hannah.f1", "早上在 East Coast Park 游泳", ev("syn-old_friend_catchup-003-m1", "morning swims at East Coast Park?")),
        fact("hannah.f2", "和 Ben 搬到 Bukit Timah 新家", ev("syn-old_friend_catchup-007-m1", "new place in Bukit Timah?")),
    ],
    "edges": [edge("person:ben", "Ben", "partner", ev("syn-old_friend_catchup-007-m1", "Did you and Ben finally settle into the"))],
    "external": [],
})

P.append({
    "id": "kevin_chen", "email": "kevin.chen@example.com", "display_name": "Kevin Chen",
    "relationship": "中文朋友，写 newsletter，常聊 MCP 和 eval", "language": "zh_en_mixed",
    "core_connection": {"text": "常交流 MCP、本地模型和 LLM as judge 的技术朋友。",
                        "evidence": [ev("syn-zh_en_casual-009-m1", "好奇你这个 local MCP 是自己写的还是用现成的？")]},
    "address_as": [addr("default", "Kevin", ev("syn-zh_en_casual-014-m1", "Kevin"))],
    "honorific": {"uses_nin": False, "evidence": []},
    "facts": [
        fact("kevin.f1", "自己做了一个 local MCP", ev("syn-zh_en_casual-009-m1", "好奇你这个 local MCP 是自己写的还是用现成的？")),
        fact("kevin.f2", "在做 LLM as judge", ev("syn-zh_en_casual-018-m1", "我们当时是把打分改成 pass/fail")),
    ],
    "edges": [], "external": [],
})

P.append({
    "id": "amy_wang", "email": "amy.wang@example.com", "display_name": "Amy 王",
    "relationship": "中文朋友，住得近，常聊吃的和带娃", "language": "zh_en_mixed",
    "core_connection": {"text": "住得近的妈妈朋友，一起吃火锅、交换 TJ 好物和 daycare 经验。",
                        "evidence": [ev("syn-zh_en_casual-003-m1", "Cupertino 那家小龙坎还不错，辣是真辣。")]},
    "address_as": [addr("default", "Amy", ev("syn-zh_en_casual-012-m1", "Amy"))],
    "honorific": {"uses_nin": False, "evidence": []},
    "facts": [fact("amy.f1", "一起去 Cupertino 的小龙坎", ev("syn-zh_en_casual-003-m1", "Cupertino 那家小龙坎还不错，辣是真辣。"))],
    "edges": [], "external": [],
})

P.append({
    "id": "priya_shah", "email": "priya.shah@example.com", "display_name": "Priya Shah",
    "relationship": "前同事", "language": "en",
    "core_connection": {"text": "前同事，偶尔约在 Red Rock 喝咖啡叙旧。",
                        "evidence": [ev("syn-friend_scheduling-001-m2", "See you Thursday 10am at Red Rock")]},
    "address_as": [addr("default", "Priya", ev("syn-friend_scheduling-001-m1", "Hi Priya,"))],
    "honorific": {"uses_nin": False, "evidence": []},
    "facts": [fact("priya.f1", "在 Red Rock 见过面", ev("syn-friend_scheduling-001-m2", "See you Thursday 10am at Red Rock"))],
    "edges": [], "external": [],
})

P.append({
    "id": "bambu_indah", "email": "reservations@bambuindah.example.com", "display_name": "Bambu Indah Reservations",
    "relationship": "商家：巴厘岛 Ubud 的酒店，联系人 Made", "language": "en",
    "core_connection": {"text": "2024 年 9 月住过、2026 年 4 月回访的酒店，和联系人 Made 打交道。",
                        "evidence": [ev("syn-vendor_service-002-m1", "We stayed with you in September 2024 and would love to come back.")]},
    "address_as": [addr("default", "Made", ev("syn-vendor_service-001-m1", "Dear Made,"), ev("syn-vendor_service-002-m2", "Dear Made,"))],
    "honorific": {"uses_nin": False, "evidence": []},
    "facts": [
        fact("bambu.f1", "2024 年 9 月住过，2026 年 4 月回访", ev("syn-vendor_service-002-m1", "We stayed with you in September 2024 and would love to come back.")),
        fact("bambu.f2", "通常是 2 个大人：Mia 和 Victor", ev("syn-vendor_service-001-m1", "2 adults: Mia & Victor")),
        fact("bambu.f3", "2026 年住的是 Moon House", ev("syn-vendor_service-002-m2", "The Moon House sounds lovely.")),
        fact("bambu.f4", "订过 Founders Tour", ev("syn-vendor_service-019-m2", "9:30 AM Founders Tour on April 16")),
    ],
    "edges": [], "external": ["ext-bambu-1"],
})

P.append({
    "id": "hoshinoya_kyoto", "email": "reservations@hoshinoya-kyoto.example.com", "display_name": "Hoshinoya Kyoto",
    "relationship": "商家：京都岚山的酒店，联系人 Kenji", "language": "en",
    "core_connection": {"text": "住过两次的京都酒店（2025-03-28 到 30、2026-04-06 到 08），联系人 Kenji 帮忙寄回过落下的围巾。",
                        "evidence": [ev("syn-vendor_service-004-m1", "Thank you so much for a wonderful stay from March 28 to 30."), ev("syn-vendor_service-018-m1", "it is lovely to hear from you again")]},
    "address_as": [addr("default", "Kenji", ev("syn-vendor_service-003-m1", "Dear Kenji,"), ev("syn-vendor_service-004-m1", "Dear Kenji,"))],
    "honorific": {"uses_nin": False, "evidence": []},
    "facts": [
        fact("hoshinoya.f1", "2025 年 3 月 28 到 30 日住过", ev("syn-vendor_service-004-m1", "Thank you so much for a wonderful stay from March 28 to 30.")),
        fact("hoshinoya.f2", "落下过一条灰色羊毛围巾，酒店寄回", ev("syn-vendor_service-004-m1", "I believe I left a gray wool scarf in our room")),
        fact("hoshinoya.f3", "2026 年 4 月再次入住", ev("syn-vendor_service-018-m1", "it is lovely to hear from you again")),
        fact("hoshinoya.f4", "订过茶道体验", ev("syn-vendor_service-018-m2", "Please book the 3:00 PM tea ceremony on April 7 for both of us.")),
        fact("hoshinoya.f5", "Victor 不吃生贝类", ev("syn-vendor_service-003-m2", "Victor prefers not to have raw shellfish")),
    ],
    "edges": [], "external": ["ext-hoshinoya-1", "ext-hoshinoya-2"],
})

EXTERNAL = {
    "_mock": True,
    "_note": "全部是 mock 数据，由上下文数据线编写，不来自任何真实网站或社交媒体。人物和商家都是虚构的。",
    "items": [
        {"id": "ext-ethan-1", "person_id": "ethan_park", "mock": True, "date": "2026-10-18",
         "source_label": "Ethan 的 X 动态（mock）",
         "text": "Ethan 宣布从 11 月起每周六早上 9 点在 Las Palmas Park 开一个散步式 coaching 小组，边走边聊。"},
        {"id": "ext-ethan-2", "person_id": "ethan_park", "mock": True, "date": "2026-10-09",
         "source_label": "Ethan 的 LinkedIn 动态（mock）",
         "text": "Ethan 分享了一篇文章：远程工作的父母如何安排每周一次的线下复盘。"},
        {"id": "ext-julien-1", "person_id": "julien_moreau", "mock": True, "date": "2026-10-12",
         "source_label": "Julien 的 Instagram（mock）",
         "text": "Julien 晒了春川马拉松的完赛照片，说明年想挑战全马。"},
        {"id": "ext-wang-1", "person_id": "wang_jianhua", "mock": True, "date": "2026-10-15",
         "source_label": "社区公众号（mock）",
         "text": "王建华老师的书法作品《行书·兰亭序节临》入选社区老年书画展，10 月 20 日至 11 月 30 日在社区文化中心展出。"},
        {"id": "ext-tang-1", "person_id": "tang_shuyuan", "mock": True, "date": "2026-09-27",
         "source_label": "唐书远的朋友圈（mock）",
         "text": "唐书远发了华人文化节的大合影，感谢所有志愿者，说明年想加一个儿童书法角。"},
        {"id": "ext-zhao-1", "person_id": "zhao_liqun", "mock": True, "date": "2026-10-16",
         "source_label": "公司 LinkedIn 主页（mock）",
         "text": "赵立群的公司宣布 11 月 8 日在上海举办 AI 产品发布会，主题是“企业知识助手”。"},
        {"id": "ext-xiaoyu-1", "person_id": "lin_xiaoyu", "mock": True, "date": "2026-10-19",
         "source_label": "林小雨的小红书（mock）",
         "text": "林小雨发了女儿画的万圣节南瓜绘本，问大家有没有好用的 AI 绘本工具。"},
        {"id": "ext-hoshinoya-1", "person_id": "hoshinoya_kyoto", "mock": True, "date": "2026-10-01",
         "source_label": "Hoshinoya Kyoto 官网活动页（mock）",
         "text": "红叶季特别活动：11 月 10 日至 12 月 5 日，每晚 6:30 加开一班红叶夜游船，住客可在前台预约。"},
        {"id": "ext-hoshinoya-2", "person_id": "hoshinoya_kyoto", "mock": True, "date": "2026-10-05",
         "source_label": "Hoshinoya Kyoto 官网活动页（mock）",
         "text": "11 月每周六下午 3 点在书院举办红叶茶会，限 8 位住客。"},
        {"id": "ext-bambu-1", "person_id": "bambu_indah", "mock": True, "date": "2026-10-10",
         "source_label": "Bambu Indah Instagram（mock）",
         "text": "雨季前的稻田瑜伽周：11 月 1 日至 15 日每天早上 7 点在河边平台免费为住客开课。"},
    ],
}

with open(os.path.join(GT, "people.json"), "w", encoding="utf-8") as f:
    json.dump({"_note": "标准答案，只供生成样例邮件和评估用。离线管线不能读 data/ground_truth/。", "people": P}, f, ensure_ascii=False, indent=2)
with open(os.path.join(GT, "external.json"), "w", encoding="utf-8") as f:
    json.dump(EXTERNAL, f, ensure_ascii=False, indent=2)
print(f"people={len(P)} external={len(EXTERNAL['items'])}")
