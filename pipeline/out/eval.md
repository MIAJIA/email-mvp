# Offline extraction vs ground truth

People in ground truth: 13; notes found: 13.

| Metric | Score |
|---|---|
| Address accuracy (per person x context) | 15/15 = 100% |
| Honorific accuracy (per person) | 13/13 = 100% |
| Fact recall | 51/60 = 85% |

| Person | Address (expected -> got) | Honorific (expected -> got) | Facts recalled |
|---|---|---|---|
| **Ethan Park** | default:Ethan -> default:Ethan (1/1) | - -> - (ok) | 5/5 |
| **唐书远** | private:老唐, default:书远, formal:唐书远老师 -> private:老唐, default:书远, formal:唐书远老师 (3/3) | 您 (formal only) -> 您 (formal only) (ok) | 8/10 |
| **王建华** | default:王老师 -> default:王老师 (1/1) | 您 -> 您 (ok) | 10/10 |
| **赵立群** | default:赵总 -> default:赵总 (1/1) | 您 -> 您 (ok) | 7/8 |
| Amy 王 | default:Amy -> default:Amy (1/1) | - -> 你 (ok) | 1/1 |
| 周航 | default:周航 -> default:周航 (1/1) | - -> 你 (ok) | 2/3 |
| Hannah Kim | default:Hannah -> default:Hannah (1/1) | - -> - (ok) | 2/2 |
| Julien Moreau | default:Julien -> default:Julien (1/1) | - -> - (ok) | 5/5 |
| Kevin Chen | default:Kevin -> default:Kevin (1/1) | - -> 你 (ok) | 0/2 |
| Priya Shah | default:Priya -> default:Priya (1/1) | - -> - (ok) | 1/1 |
| Bambu Indah Reservations | default:Made -> default:Made, formal:Bambu Indah Team (1/1) | - -> - (ok) | 2/4 |
| Hoshinoya Kyoto | default:Kenji -> default:Kenji (1/1) | - -> - (ok) | 4/5 |
| 林小雨 | default:小雨 -> default:小雨 (1/1) | - -> 你 (ok) | 4/4 |

Facts missed for the focus people:

- 唐书远: 华人文化节在 9 月 26 日
- 唐书远: Mia 做了文化节宣传海报（中英双语）
- 赵立群: 2025 年 9 月来湾区开会，和 Mia 吃过饭
