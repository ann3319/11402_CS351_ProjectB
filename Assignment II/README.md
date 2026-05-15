# Assignment: SDD, BDD, and TDD in AI-Assisted Software Development

## Student Information

- Name:穆姿安
- Student ID:1123319
- Course: CS351
- Date: 2026/5/14

## 1. Introduction

**1.What AI-assisted software development is.**
利用AI協助使用者完成各項任務，包括撰寫程式碼、debug、生成測試案例、系統設計……等，旨在提高開發效率和品質

**2.Why clear requirements are important when using AI tools.**
AI工具的輸出內容高度依賴輸入指令，不明確的需求會使AI產出錯誤的邏輯和幻覺，明確的指令才能引導AI產生正確且可用的結果

**3.Why SDD, BDD, and TDD are useful in the AI era.**
這三種方法為AI提供結構化的指引
．SDD提供系統化的全景藍圖，避免AI生成片段化、難以整合的代碼
．BDD透過自然語言描述行為，讓AI能根據實際使用者情境生成精準的功能
．TDD提供明確的驗證標準，讓開發者能快速檢驗AI生成的代碼是否正確，確保軟體的穩健性。

## 2. Definition of SDD

**Specification-Driven Development (SDD)** 是以明確的規格文件為基礎的開發方式。強調在程式撰寫之前，先完整定義系統的需求與行為，讓開發者、測試者與使用者都能有共同的理解
包含：
- 目標：軟體必須解決特定問題，明確的目標能避免開發過程中偏離方向
- 功能需求：系統必須提供的功能，這些需求是開發的核心
- 輸入與輸出：系統接收的資料，輸入必須定義清楚，才能避免錯誤；產生的結果必須容易被使用者理解
- 限制條件：系統必須遵守的規則或限制，這些限制確保系統穩定性
- 驗收標準：用來檢查系統是否正確的條件，驗收標準是判斷系統完成度的依據

## 3. SDD: Student Grade Calculator

### 3.1 Goal
設計一個「學生成績計算器」，用來整合多科分數，計算總分與平均分數，並依照規則判斷學生的等級。此工具能幫助老師快速評估學生表現，也能讓學生自行檢查成績。

### 3.2 Functional Requirements
．系統必須能輸入多科分數（例如：國文、英文、數學、自然、社會）
．系統必須計算總分與平均分數
．系統必須依照規則判斷等級（A/B/C/D/F）
．系統必須能處理無效輸入並回報錯誤訊息

### 3.3 Input
．學生各科分數（整數，範圍 0–100）
．科目數量至少 3 科，最多 10 科

### 3.4 Output
．總分（所有科目分數加總）
．平均分數（總分 ÷ 科目數）
．等級（依照規則判斷）
．錯誤訊息（若輸入不合法）

### 3.5 Grade Rules
．A 等級：平均分數 ≥ 90，且所有科目分數 ≥ 80
．B 等級：平均分數 ≥ 80，但至少有一科 < 80
．C 等級：平均分數 ≥ 70，但至少有一科 < 60
．D 等級：平均分數 ≥ 60，但至少有一科 < 50
．F 等級：平均分數 < 60，或有任一科分數 < 40

### 3.6 Acceptance Criteria
1.當輸入 [95, 92, 88, 90] → 總分 = 365，平均 = 91.25，等級 = A

2.當輸入 [85, 70, 80, 90] → 總分 = 325，平均 = 81.25，等級 = B

3.當輸入 [75, 60, 72, 68] → 總分 = 275，平均 = 68.75，等級 = C

4.當輸入 [60, 55, 62, 50] → 總分 = 227，平均 = 56.75，等級 = D

5.當輸入 [100, 30, 80, 90] → 總分 = 300，平均 = 75，等級 = F

6.當輸入 [105, 90, 80] → 系統回報「分數超出範圍」錯誤訊息

## 4. Definition of BDD

**Behavior-Driven Development, BDD** 是一種以使用者行為為核心的開發方法。透過具體場景來描述系統需求，讓開發者、測試者與非技術人員都能用共同的語言理解系統應該如何運作。

BDD 的常見格式是 Given–When–Then：

．Given：描述初始條件或前置狀態
．When：描述使用者或系統執行的動作
．Then：描述預期的結果

這種方式的好處是能把抽象的需求轉換成具體的行為案例，讓團隊更容易溝通，並確保系統的功能符合使用者期待。

## 5. BDD: Student Grade Calculator

### Scenario 1: 高分學生獲得 A 等級
．Given 學生的國文分數為 92
．And 英文分數為 95
．And 數學分數為 90
．And 自然分數為 88
．When 系統計算總分與平均分數
．Then 平均分數應該大於 90
．And 等級應該為 A

### Scenario 2: 無效輸入導致錯誤訊息
．Given 學生的數學分數為 105
．And 英文分數為 85
．And 國文分數為 90
．When 系統嘗試計算總分與平均分數
．Then 系統應該回報「分數超出範圍」的錯誤訊息
．And 不應產生任何等級結果

## 6. Definition of TDD
**Test-Driven Development, TDD** 是一種先寫測試，再寫程式的開發方法。它的核心流程是 Red–Green–Refactor：

．Red：先撰寫測試案例，程式尚未完成，因此測試必然失敗。
．Green：撰寫程式碼，使測試通過。
．Refactor：在測試通過後，重構程式碼以提升品質與可維護性。

TDD 的好處是能確保程式在開發過程中持續符合需求，並且降低錯誤率。它讓程式碼更容易維護，也能提升團隊合作的效率。

---

## 7. TDD: Student Grade Calculator

### Scenario 1: Normal Test Cases

#### Test Case 1:
輸入分數：[95, 92, 90, 88]
預期結果：總分 = 365，平均 = 91.25，等級 = A

#### Test Case 2:
輸入分數：[80, 78, 85, 82]
預期結果：總分 = 325，平均 = 81.25，等級 = B

### Scenario 2: Boundary Test Cases

#### Test Case 1:
輸入分數：[60, 60, 60, 60]
預期結果：總分 = 240，平均 = 60，等級 = D

#### Test Case 2:
輸入分數：[59, 61, 62, 60]
預期結果：總分 = 242，平均 = 60.5，等級 = F（因為有一科 < 60）

### Scenario 3: Invalid Input Test Cases

#### Test Case 1:
輸入分數：[105, 90, 80]
預期結果：系統回報「分數超出範圍」錯誤訊息，不產生等級。

#### Test Case 2:
輸入分數：[90, -5, 85]
預期結果：系統回報「分數不可為負數」錯誤訊息，不產生等級。

---

## 8. Comparison of SDD, BDD, and TDD
| 項目 | SDD | BDD | TDD |
| --- | --- | --- | --- |
| **全名** | Specification-Driven Development | Behavior-Driven Development | Test-Driven Development |
| **主要焦點** | 系統需求與規格 | 使用者行為與場景 | 測試案例與正確性 |
| **核心問題** | 「系統應該建什麼？」 | 「系統應該如何表現？」 | 「如何驗證系統正確？」 |
| **典型格式** | 結構化規格文件（需求、輸入、輸出、限制） | Given–When–Then 敘述 | 測試案例表格、單元測試程式 |
| **AI 時代的價值** | 幫助 AI 理解需求，避免生成偏離目標的程式 | 幫助 AI 理解使用者期望的行為，提升互動性 | 驗證 AI 生成程式是否正確，確保可靠性 |
| **優點** | 明確定義需求，減少誤解 | 案例貼近使用者語言，容易溝通 | 測試驅動，程式更穩定、可維護 |
| **缺點** | 文件撰寫耗時，需完整規格 | 案例設計需全面，否則容易遺漏情境 | 初期開發速度較慢，需要大量測試 |
| **適用情境** | 專案初期，需求尚未明確時 | 與非技術人員溝通需求時 | 開發過程中持續驗證程式正確性 |
| **團隊合作價值** | 提供共同的需求基準 | 提供共同的行為語言 | 提供共同的測試標準 |
---

## 9. Reflection
**1.Which approach is easiest for you to understand: SDD, BDD, or TDD? Why?**

我覺得最容易理解的是BDD，因為它使用Given–When–Then的格式，把需求轉換成行為場景，非技術人員也能快速理解。相比之下，SDD 偏向文件化，雖然完整但較抽象；TDD 則需要先寫測試再寫程式，對初學者來說需要更多程式經驗才能掌握。

**2.Which approach is most useful when working with AI coding tools? Why?**

最有效的方法是SDD。因為AI 需要清楚的提示才能產生正確結果，而SDD的規格能把需求拆解成目標、輸入、輸出與限制，避免模糊的指令導致AI生成錯誤或不完整的程式，確保生成方向正確。

**3.How can SDD help reduce unclear AI prompts?**

因為SDD因為它會先規劃系統架構、模組功能與資料流程。有了清楚的設計後，提供給AI的指令就會更明確，例如要實作哪些功能、輸入輸出格式是什麼，AI便能更準確地產生程式碼。

**4.How can BDD help describe user expectations?**

因為BDD強調以使用者角度撰寫需求，例如「當使用者登入時，系統應顯示歡迎訊息」。這種方式能讓開發者與使用者更容易理解需求，也能讓AI更清楚知道功能目標。

**5.How can TDD help check whether AI-generated code is correct?**

只要把 AI 生成的程式放入測試案例中，透過事先設計好的測試案例，可以驗證程式是否符合需求，避免AI生成看似正確但實際有問題的程式碼。

**6.If you use AI tools in future software projects, how would you combine SDD, BDD, and TDD?**

先用 SDD 定義需求，確保 AI 生成程式的方向正確；再用 BDD 撰寫行為場景，讓團隊與 AI 都能理解使用者的期待；最後用 TDD 撰寫測試案例，持續驗證 AI 生成的程式是否正確。

---

## 10. References / AI Tool Usage
**AI 工具**

．使用了Copilot 來整理作業結構、撰寫Markdown範本、設計原創案例（SDD、BDD、TDD）以及比較表格。
．使用了ChatGPT來理解 SDD、BDD、TDD 的定義，並提供反思部分的參考
．內容生成後，我都有審閱與修改