# Align-Nexus | 戰略對準協議 (The Nexus Protocol)

> **「戰略對準不是過濾資料，而是重新合成意圖。」**

`Align-Nexus` 是 Castle Studio AAA 生態系的核心戰略引擎。它抽象化了所有「對準」任務的邏輯，透過 **知識池 (Pool)** 與 **目標 (Target)** 的動態匹配，產生具有高說服力與「好品味」的 **產出 (Outcome)**。

---

## 核心協議 (The Protocol)

本專案遵循 **Pool ➔ Target ➔ Outcome** 的三位一體協議：

1.  **知識池 (Pool)**: 原始事實的來源（例如個人經歷、專案日誌、企業資料）。它是我們唯一的真實來源 (Source of Truth)。
2.  **目標 (Target)**: 我們要滿足的具體需求（例如職缺描述、提案企劃、內容簡報）。它定義了對準的方向。
3.  **情資 (Intelligence)**: 額外的語境參考（例如公司術語、市場研究、避雷指南）。它負責微調對準的精確度。
4.  **產出 (Outcome)**: 最終生成的戰略文件。

---

## 目錄結構

### 📂 `packages/align-nexus` (核心引擎)
- **`engine/`**: 基於 Go 與 Gemini API 的對準引擎。
- **`pool/`**: 通用的事實池模板。
- **`targets/`**: 通用的目標模板。

### 📂 `apps/` (應用實例)
- **`nexus-resume/`**: 個人履歷與職業發展的超對準系統。
- **`nexus-marketing/`**: 品牌內容與社群媒體的戰略對準矩陣。
- **`nexus-agent/`**: (New) 自主代理工作區，用於執行自動化任務對準。

### 📂 `archive/` (封存空間)
- 存放舊版的 `marketing_hub` 與 `resume_builder` 實驗程式碼，與核心協議隔離。

---

## 快速啟動

要執行任何對準任務，請進入對應應用的 `engine` 資料夾：

```bash
cd apps/nexus-resume/engine
go run . -id <目標ID> -pool <事實池ID>
```

**參數說明：**
- `-id`: 對應 `targets/` 下的 JSON 檔名。
- `-pool`: 對應 `pool/` 下的 JSON 檔名（預設為 `profile`）。

---

## 「好品味 (Good Taste)」標準

Align-Nexus 的產出必須符合以下準則：
- **零冗餘 (Zero Fluff)**: 如果一項事實無法解決目標需求，就不應該出現在產出中。
- **術語回響 (Terminology Echo)**: 精確採用目標對象的詞彙與語境。
- **Persona 變色龍**: 根據目標動態調整專業形象與語氣 (Tone)。

---

*Part of the Castle Studio AAA Project.*
