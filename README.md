# FastAPI Mock Data 範例

這是一個使用 FastAPI 框架和 Python 編寫的範例應用程式。此應用程式展示了如何在開發環境中使用 mock 資料，並在生產環境中動態切換至實際資料。

## 目錄

- [FastAPI Mock Data 範例](#fastapi-mock-data-範例)
  - [目錄](#目錄)
  - [快速開始](#快速開始)
  - [環境變數](#環境變數)
  - [API Endpoint](#api-endpoint)
    - [範例](#範例)
      - [`GET /teacher`](#get-teacher)
      - [`GET /student`](#get-student)
    - [使用 Mock 資料](#使用-mock-資料)
    - [製作 Mock 資料](#製作-mock-資料)
  - [貢獻](#貢獻)
  - [授權](#授權)

## 快速開始

1. Clone 此倉庫：

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. 建立並啟動虛擬環境：

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. 安裝依賴：

   ```bash
   pip install -r requirements.txt
   ```

4. 啟動應用程式：
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8080 --reload
   ```

## 環境變數

應用程式使用以下環境變數來控制行為：

- `API_ENV`：設定參數為 `production` 或 `develop` 來控制應用程式的運行模式。預設為 `develop`。
- `PORT`：指定應用程式運行的 port。預設為 `8000`。

在開發環境中，應用程式會自動加載 `.env` 文件中的環境變數。

## API Endpoint

應用程式提供兩個 API Endpoint：

- `GET /teacher`：回傳教師資料。
- `GET /student`：根據 `student_id` 回傳學生資料。

### 範例

#### `GET /teacher`

```json
{
  "_id": "w12345",
  "name": "Nijia"
}
```

#### `GET /student`

```json
{
  "_id": "student_id",
  "total_member": 3,
  "rating": 1,
  "query_list": [{ "a": 1 }, { "b": 2 }]
}
```

### 使用 Mock 資料

在開發環境中，應用程式會從 mock.json 文件中加載 mock 資料。這些 mock 資料會在 API 呼叫時回傳，而不會進行實際呼叫第三方 API 。

### 製作 Mock 資料

建立一個 mock.json 文件，內容如下：

```json
{
  "read_teacher": {
    "_id": "mock_teacher_id",
    "name": "Mock Teacher"
  },
  "read_student": {
    "_id": "mock_student_id",
    "total_member": 2,
    "rating": 5,
    "query_list": [{ "mock_a": 1 }, { "mock_b": 2 }]
  }
}
```

## 貢獻

歡迎任何形式的貢獻！請提交 pull request 或建立 issue 來提供回饋。

## 授權

此專案使用 MIT 授權。詳情請參閱 LICENSE 文件。
