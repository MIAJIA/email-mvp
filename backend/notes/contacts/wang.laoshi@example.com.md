---
email: wang.laoshi@example.com
display_name: 王老师
relationship: Mia的老师，为她写博士申请推荐信
scenario: zh_formal
address_as:
  value: 王老师您好
  count: 3
  total: 3
  status: learned
  evidence:
  - message_id: hw-wang-001
    quote: 王老师您好，
  - message_id: hw-wang-003
    quote: 王老师您好，
honorific:
  value: 您
  count: 3
  total: 3
  status: learned
  evidence:
  - message_id: hw-wang-001
    quote: 冒昧打扰您。
  - message_id: hw-wang-002
    quote: 麻烦您有空时看一下。
sign_off:
  value: 祝好，
  count: 2
  total: 3
  status: learned
  evidence:
  - message_id: hw-wang-001
    quote: 祝好，
  - message_id: hw-wang-002
    quote: 祝好，
language:
  value: Chinese
  count: 3
  total: 3
  status: learned
  evidence:
  - message_id: hw-wang-001
    quote: 我正在申请明年的博士项目
facts:
- id: wrote_recommendation_letter
  text: 王老师答应为 Mia 的博士申请写推荐信
  status: learned
  evidence:
  - message_id: hw-wang-002
    quote: 谢谢您答应帮我写推荐信！
- id: letter_deadline_dec_1
  text: 推荐信截止日期是 12 月 1 日
  status: learned
  evidence:
  - message_id: hw-wang-001
    quote: 截止日期是 12 月 1 日
- id: sent_cv_and_research_plan
  text: Mia 已把简历和研究计划作为附件发给王老师
  status: learned
  evidence:
  - message_id: hw-wang-002
    quote: 简历和研究计划已经放在附件里
- id: mia_admitted_phd
  text: Mia 收到了博士项目录取通知，并已告知王老师
  status: learned
  evidence:
  - message_id: hw-wang-003
    quote: 我收到了录取通知！
- id: long_term_mentor
  text: 王老师指导了 Mia 好几年，Mia 承诺回学校时去办公室看望
  status: learned
  evidence:
  - message_id: hw-wang-003
    quote: 真的非常感谢您的推荐信和这几年的指导。
  - message_id: hw-wang-003
    quote: 下次回学校一定去办公室看您。
edges:
- to: Mia
  type: teacher_of
  evidence:
  - message_id: hw-wang-001
    quote: 学生 Mia
- to: Mia
  type: recommender_for
  evidence:
  - message_id: hw-wang-002
    quote: 谢谢您答应帮我写推荐信！
external: []
---
Extracted from 3 sent emails by app.pipeline.extract. Dropped quotes: 0.
