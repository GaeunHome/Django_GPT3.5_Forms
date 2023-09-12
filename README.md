# 簡易GPT3.5模型回應輸出
<h4>forms.py</h4>
<p>建立Django內建表單。</p>

<h4>views.py - robot_view</h4>
<p>1. 於index.html將內容輸入完畢會將descriptions交由ChatGPT_conversation處理</p>
<p>2. 結果會跳轉至result.html（<b>網址不會更動</b>）</p>

<h4>views.py - ChatGPT_conversation</h4>
<p>1. 呼叫GPT3.5模型。</p>
<p>2. 需填入個人API KEY與system之prompt。</p>
<p>3. system、user的關係可參照OpenAI的Playground。</p>
<p>4. 回傳response.choices[0].message.content，即GPT3.5的回答。</p>
