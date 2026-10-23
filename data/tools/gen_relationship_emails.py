"""Generate data/emails/synthetic_relationship.jsonl (honorific / special-address recipients)."""
import json, sys

OUT = sys.argv[1]

WANG = ("wang.jianhua@example.com", "王建华")
TANG = ("tang.shuyuan@example.com", "唐书远")
ZHAO = ("zhao.liqun@example.com", "赵立群")

E = []


def add(thread, n, date, who, subject, body, category, address, honorific, facts, prev=None):
    E.append({
        "thread_id": f"syn-rel-{thread}",
        "message_id": f"syn-rel-{thread}-m{n}",
        "date": date,
        "to": who[0],
        "to_name": who[1],
        "subject": subject,
        "body": body,
        "prev": prev,
        "prev_sender": who[0] if prev else None,
        "category": category,
        "source": "synthetic",
        "planted_address": address,
        "planted_honorific": honorific,
        "planted_facts": [{"fact_id": f, "quote": q} for f, q in facts],
    })


# ---- Wang Jianhua: former graduate advisor; addressed as 王老师 with 您 ----
add("wang-001", 1, "2025-01-20T02:10:00Z", WANG, "新年问候",
    "王老师：\n\n您好！新年快要到了，提前给您和李阿姨拜个早年。\n\n毕业这么多年，一直很感谢您当年在实验室对我的指导。我现在在湾区做 AI 相关的产品，经常会想起您说的“先把问题定义清楚，再动手”。\n\n给您寄了一饼云南的老普洱，记得您以前在实验室最爱喝这个，应该下周能到。\n\n祝您身体健康，新春愉快！\n\n学生 Mia 敬上",
    "zh_formal", "王老师", True,
    [("wang.f1", "一直很感谢您当年在实验室对我的指导"),
     ("wang.f2", "给您寄了一饼云南的老普洱，记得您以前在实验室最爱喝这个"),
     ("wang.f3", "先把问题定义清楚，再动手")])
add("wang-001", 2, "2025-02-05T03:30:00Z", WANG, "Re: 新年问候",
    "王老师：\n\n您收到就好！您喜欢的话下次我再给您带。\n\n也请代我向李阿姨问好，谢谢她当年常给我们包饺子。\n\nMia 敬上",
    "zh_formal", "王老师", True,
    [("wang.f4", "也请代我向李阿姨问好，谢谢她当年常给我们包饺子")],
    prev="Mia：\n\n茶收到了，谢谢你还记得。你李阿姨也说这个茶好。在那边工作注意身体。\n\n王建华")
add("wang-002", 1, "2025-09-15T01:20:00Z", WANG, "Re: 近况",
    "王老师：\n\n谢谢您的关心！我们这边一切都好。听周航师兄说您退休后每天都在练书法，还在老年大学开了一个小班，真为您高兴。\n\n您之前说想看看现在的 AI 能做什么，我整理了一份简单的介绍，附在邮件里，您有空的时候翻翻就好，不用回复。\n\n祝您秋安！\n\n学生 Mia",
    "zh_formal", "王老师", True,
    [("wang.f5", "听周航师兄说您退休后每天都在练书法，还在老年大学开了一个小班"),
     ("wang.f6", "您之前说想看看现在的 AI 能做什么")],
    prev="Mia：\n\n好久没有你的消息，最近怎么样？\n\n王建华")
add("wang-003", 1, "2026-04-10T02:05:00Z", WANG, "书法作品整理成册",
    "王老师：\n\n您好！最近北京应该暖和起来了吧。上次您提到想把书法作品拍照整理成一本小册子，我问了一下，可以用 Google Photos 自动排版成相册，我把步骤写在下面了，您看看是否方便。\n\n如有任何不清楚的地方，您随时告诉我，我视频给您演示。\n\n学生 Mia 敬上",
    "zh_formal", "王老师", True,
    [("wang.f7", "上次您提到想把书法作品拍照整理成一本小册子")])
add("wang-004", 1, "2026-10-08T01:40:00Z", WANG, "十一月回北京",
    "王老师：\n\n您好！我十一月中旬会回北京待两周，想去家里看望您和李阿姨，不知道您哪天方便？\n\n这次我会带上次您说好喝的那款普洱，再给您带一本 Victor 帮我挑的字帖。\n\n周航师兄说也想一起去，如果您不介意，我们就一起过来。\n\n学生 Mia 敬上",
    "zh_formal", "王老师", True,
    [("wang.f8", "我十一月中旬会回北京待两周，想去家里看望您和李阿姨"),
     ("wang.f9", "周航师兄说也想一起去")])
add("wang-004", 2, "2026-10-12T02:15:00Z", WANG, "Re: 十一月回北京",
    "王老师：\n\n好的，那我们就定 11 月 18 号下午三点左右过来，到之前我先给您打电话。\n\n您不用特意准备，我们坐一会儿就好。\n\n学生 Mia",
    "zh_formal", "王老师", True,
    [("wang.f10", "那我们就定 11 月 18 号下午三点左右过来")],
    prev="Mia：\n\n18 号下午我和你李阿姨都在家，你们来吧。\n\n王建华")

# ---- Tang Shuyuan: Victor's college roommate; 老唐 in private, 书远 by default, 唐书远老师 + 您 in committee emails ----
add("tang-001", 1, "2024-11-02T18:40:00Z", TANG, "Re: 周末烧烤",
    "老唐\n\n周六可以！Victor 说要把他新买的 smoker 搬过来 哈哈\n我们带腌好的鸡翅和饮料 苏晴姐说不用带甜点 那我就不带啦",
    "zh_en_casual", "老唐", False,
    [("tang.f1", "苏晴姐说不用带甜点")],
    prev="周六来我家烧烤？苏晴说甜点她包了。\n\n老唐")
add("tang-002", 1, "2025-03-22T05:10:00Z", TANG, "上下铺",
    "老唐\n\n你和 Victor 大学睡上下铺的照片我找到了 笑死😂\n周末聚会的时候放 slideshow 怎么样",
    "zh_en_casual", "老唐", False,
    [("tang.f2", "你和 Victor 大学睡上下铺的照片我找到了")])
add("tang-003", 1, "2025-06-30T20:25:00Z", TANG, "Re: 中文学校",
    "书远，\n\n上次你说想给朵朵找中文学校，我问了一下林小雨，她家姐姐在 Cupertino 那家上了两年，说老师很负责。我把她的联系方式发你，你们可以直接聊。\n\nMia",
    "zh_en_casual", "书远", False,
    [("tang.f3", "上次你说想给朵朵找中文学校"),
     ("tang.f4", "我问了一下林小雨，她家姐姐在 Cupertino 那家上了两年")],
    prev="Mia，你们朋友里有没有孩子在上中文学校的？想给朵朵找一家。\n\n书远")
add("tang-004", 1, "2026-08-20T17:00:00Z", TANG, "【华人文化节】志愿者分工确认",
    "唐书远老师：\n\n您好！感谢您和组委会的信任。关于 9 月 26 日华人文化节的志愿者分工，我这边确认如下：\n\n1. 我负责签到台，上午 9:00 到 12:00；\n2. Victor 负责舞台音响，全天；\n3. 宣传海报的电子版我会在 9 月 10 日前发给您审核。\n\n如有调整，请您随时告知。\n\n此致\n敬礼\n\nMia Song",
    "zh_formal", "唐书远老师", True,
    [("tang.f5", "感谢您和组委会的信任"),
     ("tang.f6", "关于 9 月 26 日华人文化节的志愿者分工"),
     ("tang.f7", "我负责签到台，上午 9:00 到 12:00")],
    prev="各位志愿者：\n\n请大家在本周内确认各自的分工，抄送组委会。\n\n唐书远\n华人文化节组委会")
add("tang-005", 1, "2026-09-09T16:30:00Z", TANG, "【华人文化节】宣传海报初稿",
    "唐书远老师：\n\n您好！宣传海报初稿已附上，中英文双语版本各一份。按您上次的意见，主办单位的名称放在了最上方。\n\n请您审阅，如需修改我今天之内可以调整。\n\n谢谢！\nMia Song",
    "zh_formal", "唐书远老师", True,
    [("tang.f8", "宣传海报初稿已附上，中英文双语版本各一份")])
add("tang-006", 1, "2026-09-10T04:50:00Z", TANG, "海报颜色",
    "书远，\n\n海报我按组委会的意见改好了，发在群里了。你私下帮我看看颜色是不是太亮，我自己有点拿不准。\n\nMia",
    "zh_en_casual", "书远", False,
    [("tang.f9", "你私下帮我看看颜色是不是太亮")])
add("tang-007", 1, "2026-09-28T03:15:00Z", TANG, "辛苦啦",
    "老唐\n\n文化节辛苦啦！！苏晴姐的桂花糕被抢光了 好多人问哪里买的哈哈\n下周末来我们家吃饭吧 给你们俩补补",
    "zh_en_casual", "老唐", False,
    [("tang.f10", "苏晴姐的桂花糕被抢光了")])

# ---- Zhao Liqun: former boss; addressed as 赵总 with 您 ----
add("zhao-001", 1, "2025-01-27T01:00:00Z", ZHAO, "新春问候",
    "赵总：\n\n您好！春节将至，给您和家人拜个早年。\n\n在您团队的那三年是我成长最快的一段时间，尤其是您带我们做第一版推荐系统的时候，很多做事方法我到现在都还在用。\n\n祝您新春快乐，阖家幸福！\n\nMia",
    "zh_formal", "赵总", True,
    [("zhao.f1", "在您团队的那三年是我成长最快的一段时间"),
     ("zhao.f2", "您带我们做第一版推荐系统的时候")])
add("zhao-002", 1, "2025-08-18T15:20:00Z", ZHAO, "Re: 九月来湾区",
    "赵总：\n\n欢迎来湾区！9 月 9 日到 12 日我都在，您看哪天晚上方便，我请您吃饭。Palo Alto 有一家粤菜您应该会喜欢，记得您以前在上海常去吃早茶。\n\nMia",
    "zh_formal", "赵总", True,
    [("zhao.f3", "记得您以前在上海常去吃早茶"),
     ("zhao.f4", "9 月 9 日到 12 日我都在")],
    prev="Mia：\n\n九月中旬我去湾区开会，有空见一面。\n\n赵立群")
add("zhao-002", 2, "2025-09-13T05:30:00Z", ZHAO, "Re: 九月来湾区",
    "赵总：\n\n谢谢您昨天抽时间见面！您说的“小团队先把一个场景做透”我记下了，回来又想了很久。\n\n祝您回程顺利。\n\nMia",
    "zh_formal", "赵总", True,
    [("zhao.f5", "小团队先把一个场景做透")])
add("zhao-003", 1, "2026-03-05T02:45:00Z", ZHAO, "雨桐的夏令营",
    "赵总：\n\n您好！您上次提到雨桐今年暑假想来湾区参加夏令营，我问了一下身边的朋友，报名一般 3 月底截止，链接附在下面，您可以让她先看看。\n\n如果她来了需要人接机或者带她转转，您随时跟我说。\n\nMia",
    "zh_formal", "赵总", True,
    [("zhao.f6", "您上次提到雨桐今年暑假想来湾区参加夏令营")])
add("zhao-003", 2, "2026-07-20T04:10:00Z", ZHAO, "Re: 雨桐的夏令营",
    "赵总：\n\n您放心，雨桐已经顺利到了，Victor 下午去机场接的她，现在在我们家吃完饭了。周末我们带她去 Half Moon Bay 转转。\n\nMia",
    "zh_formal", "赵总", True,
    [("zhao.f7", "Victor 下午去机场接的她")],
    prev="Mia：\n\n雨桐的航班今天下午到旧金山，麻烦你们了。\n\n赵立群")
add("zhao-004", 1, "2026-10-02T03:00:00Z", ZHAO, "Re: 十月线上分享",
    "赵总：\n\n谢谢您的邀请！10 月 30 日晚上的线上分享我可以参加，题目暂定“怎么让 AI 写出像你自己写的邮件”，大约 30 分钟。PPT 我会在 10 月 25 日前发给您的助理。\n\nMia",
    "zh_formal", "赵总", True,
    [("zhao.f8", "10 月 30 日晚上的线上分享我可以参加")],
    prev="Mia：\n\n公司月底有一个 AI 主题的内部分享会，想请你线上讲半小时，讲讲你在湾区做的东西。\n\n赵立群")

with open(OUT, "w", encoding="utf-8") as f:
    for e in E:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")
print(f"wrote {len(E)} emails to {OUT}")
