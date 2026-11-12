# Coding Benchmark Tasks

This file contains a small and varied set of coding tasks designed to test coding productivity with an AI coding assistant. Each task should take approximately 15–30 minutes to complete.

---

## Task 1 - User Registration Validation

**Requirements**:

Implement a function that validates user registration data.

The function must validate:
- `name` is present and not empty.
- `email` is present and contains a valid email format.
- `age` is provided and is at least 18.

Return validation errors when one or more fields are invalid.

**Inputs**:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 25
}
```

**Outputs**:

For valid input:

```json
{
  "valid": true,
  "errors": []
}
```

For invalid input:

```json
{
  "valid": false,
  "errors": [
    "Invalid email",
    "Age must be at least 18"
  ]
}
```

**Acceptance Criteria**:

- Returns `valid: true` for valid registration data.
- Rejects empty or missing names.
- Rejects invalid email addresses.
- Rejects users younger than 18.
- Returns clear validation error messages.
- Does not crash when required fields are missing.

---

## Task 2 - Product Price Calculator

**Requirements**:

Implement a function that calculates the final price of a product after applying a discount and tax.

The function should:
- Accept the original price.
- Accept a discount percentage.
- Accept a tax percentage.
- Apply the discount first.
- Apply tax to the discounted price.
- Return the final price rounded to two decimal places.

**Inputs**:

```json
{
  "price": 100,
  "discount": 20,
  "tax": 10
}
```

**Outputs**:

```json
{
  "originalPrice": 100,
  "discountAmount": 20,
  "taxAmount": 8,
  "finalPrice": 88
}
```

**Acceptance Criteria**:

- Correctly calculates the discount.
- Applies tax after the discount.
- Returns the final price with two decimal places.
- Rejects negative prices.
- Rejects discount or tax percentages outside the range `0–100`.
- Handles a `0%` discount correctly.
- Handles a `0%` tax correctly.

---

## Task 3 - Todo List API

**Requirements**:

Implement a small REST API for managing todo items.

The API must support:
- Creating a todo.
- Listing todos.
- Updating a todo.
- Deleting a todo.

Each todo should contain:
- `id`
- `title`
- `completed`

Required endpoints:

```text
POST   /todos
GET    /todos
PUT    /todos/:id
DELETE /todos/:id
```

**Inputs**:

Create todo:

```json
{
  "title": "Learn GitHub Copilot"
}
```

Update todo:

```json
{
  "title": "Learn GitHub Copilot",
  "completed": true
}
```

**Outputs**:

Successful creation:

```json
{
  "id": 1,
  "title": "Learn GitHub Copilot",
  "completed": false
}
```

Successful update:

```json
{
  "id": 1,
  "title": "Learn GitHub Copilot",
  "completed": true
}
```

**Acceptance Criteria**:

- `POST /todos` creates a new todo and returns `201`.
- `GET /todos` returns all todos.
- `PUT /todos/:id` updates an existing todo.
- `DELETE /todos/:id` removes an existing todo.
- Returns `404` when a requested todo does not exist.
- Rejects an empty todo title.
- Each created todo receives a unique ID.

---

## Task 4 - Log File Analyzer

**Requirements**:

Implement a function that analyzes application log entries and counts messages by log level.

Supported levels:

- `INFO`
- `WARNING`
- `ERROR`

The function should return the number of entries for each level.

**Inputs**:

```text
INFO Server started
ERROR Database connection failed
INFO User logged in
WARNING Disk usage is high
ERROR Request failed
```

**Outputs**:

```json
{
  "INFO": 2,
  "WARNING": 1,
  "ERROR": 2
}
```

**Acceptance Criteria**:

- Correctly counts `INFO` messages.
- Correctly counts `WARNING` messages.
- Correctly counts `ERROR` messages.
- Handles an empty log input.
- Ignores unsupported log levels.
- Does not modify the original input.

---

## Task 5 - String Utility Function

**Requirements**:

Implement a function that determines whether a string is a palindrome.

The comparison should:
- Ignore spaces.
- Ignore punctuation.
- Be case-insensitive.

**Inputs**:

```text
"A man, a plan, a canal: Panama"
```

**Outputs**:

```json
{
  "palindrome": true
}
```

For:

```text
"Hello World"
```

Output:

```json
{
  "palindrome": false
}
```

**Acceptance Criteria**:

- Correctly identifies valid palindromes.
- Ignores spaces.
- Ignores punctuation.
- Is case-insensitive.
- Handles empty strings.
- Handles strings containing only spaces or punctuation.

---

## Benchmark Guidelines

Each task should be completed independently.

The recommended target completion time is **15–30 minutes per task**.

The tasks cover different types of coding work:

- **Task 1:** Input validation
- **Task 2:** Business logic and calculations
- **Task 3:** REST API / CRUD operations
- **Task 4:** Data processing
- **Task 5:** String manipulation

These tasks can be used to evaluate coding speed, correctness, code quality, and the usefulness of an AI coding assistant such as GitHub Copilot.
