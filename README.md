# 簡易 GPT-3.5 模型回應輸出

[![Python](https://img.shields.io/badge/Python-3-3776AB)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Framework-092E20)](https://www.djangoproject.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991)](https://openai.com/)

## 專案描述

透過 Django 表單輸入內容，呼叫 OpenAI GPT-3.5 模型產生回應並輸出至頁面。

## 運作流程

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

## 備註

`docker-compose.yml`、`requirements.txt` 尚未應用。

## 專案結構

```
Django_GPT3.5_Forms/
├── manage.py                   # Django 管理指令
├── demo/                       # Django 專案設定
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── robot/                      # GPT 對話 App
│   ├── forms.py                # 表單定義
│   ├── views.py                # 視圖（含 GPT API 呼叫）
│   ├── urls.py
│   └── migrations/
├── templates/                  # 模板
│   ├── index.html              # 輸入頁面
│   └── result.html             # 結果頁面
├── requirements.txt
├── docker-compose.yml
├── .gitignore
└── README.md
```

## 快速開始

```bash
pip install -r requirements.txt
python manage.py runserver
```
