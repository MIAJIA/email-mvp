# Offline extraction vs ground truth

People in ground truth: 13; notes found: 13.

| Metric | Score |
|---|---|
| Address accuracy (per person x context) | 15/15 = 100% |
| Honorific accuracy (per person) | 13/13 = 100% |
| Fact recall | 41/60 = 68% |

| Person | Address (expected -> got) | Honorific (expected -> got) | Facts recalled |
|---|---|---|---|
| **Ethan Park** | default:Ethan -> default:Ethan (1/1) | - -> - (ok) | 1/5 |
| **唐书远** | private:老唐, default:书远, formal:唐书远老师 -> private:老唐, default:书远, formal:唐书远老师 (3/3) | 您 (formal only) -> 您 (formal only) (ok) | 8/10 |
| **王建华** | default:王老师 -> default:王老师 (1/1) | 您 -> 您 (ok) | 8/10 |
| **赵立群** | default:赵总 -> default:赵总 (1/1) | 您 -> 您 (ok) | 7/8 |
| Amy 王 | default:Amy -> default:Amy (1/1) | - -> 你 (ok) | 1/1 |
| 周航 | default:周航 -> default:周航 (1/1) | - -> 你 (ok) | 0/3 |
| Hannah Kim | default:Hannah -> default:Hannah (1/1) | - -> - (ok) | 2/2 |
| Julien Moreau | default:Julien -> default:Julien (1/1) | - -> - (ok) | 4/5 |
| Kevin Chen | default:Kevin -> default:Kevin (1/1) | - -> 你 (ok) | 1/2 |
| Priya Shah | default:Priya -> default:Priya (1/1) | - -> - (ok) | 1/1 |
| Bambu Indah Reservations | default:Made -> default:Made (1/1) | - -> - (ok) | 2/4 |
| Hoshinoya Kyoto | default:Kenji -> default:Kenji (1/1) | - -> - (ok) | 3/5 |
| 林小雨 | default:小雨 -> default:小雨 (1/1) | - -> 你 (ok) | 3/4 |

Facts missed for the focus people:

- 王建华: 王老师是 Mia 读研时在实验室的导师
- 王建华: Mia 2026 年 11 月中旬回北京两周，要去家里看望
- 唐书远: 妻子苏晴，聚会时负责甜点
- 唐书远: 华人文化节组委会负责人
- 赵立群: 2025 年 9 月来湾区开会，和 Mia 吃过饭
- Ethan Park: Ethan 是 Mia 的教练
- Ethan Park: Ethan 也给 Victor 上课
- Ethan Park: 常在 Red Rock Coffee 见面
- Ethan Park: Mia 偏好线下见面
