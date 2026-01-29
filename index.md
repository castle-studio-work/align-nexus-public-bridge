---
title: Align Nexus 匯入控制台
---

# 🛰️ Align Nexus 數據匯入控制台

這是為 NotebookLM 優化的數據中轉站。請勾選您需要的文件，系統將自動生成匯入清單。

---

## 🔗 1. 所有文件直連清單 (裸露格式)
```text
https://castle-studio-work.github.io/align-nexus-public-bridge/2026-01-27-iii-dai-review.md
https://castle-studio-work.github.io/align-nexus-public-bridge/2026-01-27-iii-dtri.md
https://castle-studio-work.github.io/align-nexus-public-bridge/2026-01-27-invent-ai.md
https://castle-studio-work.github.io/align-nexus-public-bridge/2026-01-28-kuen-yu-review.md
https://castle-studio-work.github.io/align-nexus-public-bridge/ISSUE_TEMPLATE.md
https://castle-studio-work.github.io/align-nexus-public-bridge/PAUL_CHEN_BIO.md
https://castle-studio-work.github.io/align-nexus-public-bridge/README.md
https://castle-studio-work.github.io/align-nexus-public-bridge/SKILL.md
https://castle-studio-work.github.io/align-nexus-public-bridge/_data.md
https://castle-studio-work.github.io/align-nexus-public-bridge/batch_2_research.md
https://castle-studio-work.github.io/align-nexus-public-bridge/batch_3_research.md
https://castle-studio-work.github.io/align-nexus-public-bridge/cloudflare-deploy.md
https://castle-studio-work.github.io/align-nexus-public-bridge/consolidated_resumes.md
https://castle-studio-work.github.io/align-nexus-public-bridge/cover_letter.md
https://castle-studio-work.github.io/align-nexus-public-bridge/general-issue-template.md
https://castle-studio-work.github.io/align-nexus-public-bridge/interview_prep.md
https://castle-studio-work.github.io/align-nexus-public-bridge/intro.md
https://castle-studio-work.github.io/align-nexus-public-bridge/job_description.md
https://castle-studio-work.github.io/align-nexus-public-bridge/n8n_vs_agent_architecture.md
https://castle-studio-work.github.io/align-nexus-public-bridge/prep.md
https://castle-studio-work.github.io/align-nexus-public-bridge/pull_request_template.md
https://castle-studio-work.github.io/align-nexus-public-bridge/research.md
https://castle-studio-work.github.io/align-nexus-public-bridge/resume.md
https://castle-studio-work.github.io/align-nexus-public-bridge/self_intro_article.md
https://castle-studio-work.github.io/align-nexus-public-bridge/self_intro_speech.md
https://castle-studio-work.github.io/align-nexus-public-bridge/social_media_recruitment.md
```

---

## 🛠️ 2. 交互式選取工具

<div style="background: #f4f4f4; padding: 20px; border-radius: 8px; border: 1px solid #ddd;">
    <button onclick="selectAll(true)" style="padding: 8px 15px; cursor:pointer;">全部勾選</button>
    <button onclick="selectAll(false)" style="padding: 8px 15px; cursor:pointer;">取消全選</button>
    <hr>
    <div id="file-list" style="max-height: 400px; overflow-y: auto; margin-bottom: 20px;">
        <!-- JS 動態生成 -->
    </div>
    <button onclick="generateImportList()" style="padding: 10px 20px; background: #2ea44f; color: white; border: none; border-radius: 6px; cursor:pointer; font-weight: bold;">生成匯入清單 (Import List)</button>
</div>

### 📥 3. 生成結果 (複製貼上至 NotebookLM)
<textarea id="import-result" style="width: 100%; height: 150px; font-family: monospace; padding: 10px; margin-top: 10px;" placeholder="選取後點擊生成..."></textarea>

<script>
const files = ];
const baseUrl = "https://castle-studio-work.github.io/align-nexus-public-bridge/";

// 初始化列表
const listContainer = document.getElementById('file-list');
files.forEach(file => {
    const div = document.createElement('div');
    div.style.marginBottom = "5px";
    div.innerHTML = `
        <label style="cursor:pointer;">
            <input type="checkbox" class="file-check" value="${baseUrl}${file}"> 
            <strong>${file}</strong> 
            <span style="font-size: 0.8em; color: #666;"> - ${baseUrl}${file}</span>
        </label>
    `;
    listContainer.appendChild(div);
});

function selectAll(val) {
    document.querySelectorAll('.file-check').forEach(cb => cb.checked = val);
}

function generateImportList() {
    const selected = Array.from(document.querySelectorAll('.file-check:checked')).map(cb => cb.value);
    document.getElementById('import-result').value = selected.join('\n');
}
</script>

---
*由自主員工 Adam 自動整理發佈*
