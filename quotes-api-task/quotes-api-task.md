# 📌 Random Quotes Python API

## 🧾 Overview

Build a REST API in Python that returns a random quote along with its author, based on two data sources: `quotes.json` and `authors.json`.

---

## 📁 Data Files

### `quotes.json`

Contains a list of quotes. Each entry includes:

* `id`: unique identifier for the quote
* `quote`: the quote text

**Example:**

```json
{
  "id": 23,
  "quote": "I am not a product of my circumstances. I am a product of my decisions."
}
```

---

### `authors.json`

Contains a list of authors and their associated quote IDs.

* `id`: unique identifier for the author
* `author`: author name
* `quoteIds`: list of quote IDs written by the author

**Example:**

```json
{
  "id": 21,
  "author": "Stephen Covey",
  "quoteIds": [23]
}
```

---

## ⚙️ Requirements

### 1. Authentication

* Protect the API using a Bearer token passed in the `Authorization` header.

* Expected format:

  ```
  Authorization: Bearer DEMO_AUTH@2022
  ```

* Implement authentication using a **custom decorator** (or equivalent mechanism depending on the framework).

* **Unauthorized response**

  * Status: `403 Forbidden`
  * Body:

    ```json
    {
      "message": "You are not authorized to use this API!"
    }
    ```

---

### 2. Endpoint

* Implement a **GET** endpoint at:

  ```
  /quote/random
  ```

* The endpoint should:

  1. Select a random quote from `quotes.json`
  2. Resolve and include the corresponding author using `authors.json`

> 🔎 Note: Each quote is linked to an author via `quoteIds`.

---

### 3. Response

* **Status:** `200 OK`

* **Response body:**

```json
{
  "quoteId": 23,
  "quote": "I am not a product of my circumstances. I am a product of my decisions.",
  "author": "Stephen Covey"
}
```

---

### 4. Usage Tracking & Reporting

* Track how many times each quote is returned.

* Maintain:

  * `Quote ID`
  * `Count` (number of times the quote was returned)

* After every **100 total API calls**, generate an Excel report with:

  * **Sheet name:** `Quotes Report`
  * **Columns:**

    * `Quote ID`
    * `Count`

**Example:**

| Quote ID | Count |
| -------- | ----- |
| 23       | 4     |
| 10       | 21    |

---

### 5. Report File Naming

* Use the following filename format:

```
quotes_api_report_<YYYY_MM_DD_HH_MM_SS>.xlsx
```

**Example:**

```
quotes_api_report_2022_07_15_13_53_20.xlsx
```

---

## 🌐 Optional (Bonus)

### Simple UI

* Build a minimal UI that calls your API and displays:

  * Quote text
  * Author name

* You may use any tools (plain HTML/JS, or frameworks like React, etc.).

---

## 🛠️ Technical Guidelines

* Use Python.
* You may use any framework or libraries. Common options include:

  * FastAPI, Flask, or Django (API)
  * Pandas (data handling)
  * openpyxl or xlsxwriter (Excel export)

---

## 📎 Notes & Clarifications

* You may use **in-memory data structures** (no database required).
* Ensure your code is:

  * Clean
  * Readable
  * Well-structured
* Handle edge cases where appropriate (e.g., missing author for a quote).

> ⚠️ Clarification: GET requests do not require a request body.

---

## 🚀 Possible Extensions (Follow-up Tasks)

You may be asked to extend your solution with:

### 1. Get Quote by ID

* Endpoint:

  ```
  /quote/{quoteId}
  ```

* Requirements:

  * Return quote + author
  * Return `404 Not Found` if the quote does not exist

---

### 2. UI Integration

* Connect your API to a frontend
* Use:

  * `fetch` API or
  * jQuery AJAX

---

## 📤 Submission

* Create a GitHub repository
* Include:

  * Full source code
  * Commit history (showing your development process)

