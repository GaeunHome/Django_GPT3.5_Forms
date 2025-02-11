# 簡易 GPT-3.5 模型回應輸出

### forms.py
建立 Django 內建表單。

### views.py - `robot_view`
1. 在 `index.html` 中輸入內容，將 `descriptions` 交由 `ChatGPT_conversation` 處理。
2. 結果會跳轉至 `result.html`（**網址不會更動**）。

### views.py - `ChatGPT_conversation`
1. 呼叫 GPT-3.5 模型。
2. 需填入個人 API KEY 與 system 的 prompt。
3. system、user 的關係可參照 OpenAI 的 Playground。
4. 回傳 `response.choices[0].message.content`，即 GPT-3.5 的回答。
---
### 備註
`docker-compose.yml`、`requirements.txt` 尚未應用。
