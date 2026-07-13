# GoalBreaker

An independent FastAPI microservice that uses Google's Gemini API to decompose high-level business or technical objectives into structured Agile artifacts (Epics, User Stories, and Technical Subtasks).

Built to demonstrate clean architecture, strict schema control over LLM outputs, and modern Python tooling.

## Tech Stack & Architecture

- **Backend Framework:** FastAPI (Asynchronous)
- **Package Management:** uv by Astral (Fast dependency and environment orchestration)
- **Validation & Serialization:** Pydantic v2 (Strict schema validation for structural safety)
- **LLM Provider:** Google GenAI SDK (gemini-3.5-flash)

---

## Quick Start

This project utilizes `uv` for dependency management, removing the friction of manual virtual environment activation.

### 1. Clone the repository

```bash
git clone https://github.com/LizetCh/goalbreaker
cd goalbreaker

```

### 2. Configure Environment Variables

Rename `.env.example` file to `.env` and paste your gemini api key:

```env
GEMINI_API_KEY=your_gemini_api_key_here

```

### 3. Run the Server

Execute the following command. The `uv` tool automatically builds the environment and syncs dependencies on launch:

```bash
uv run uvicorn main:app --reload

```

The server will start at `http://127.0.0.1:8000`.

---

## API Specification

### POST /breakdown

Accepts a raw text objective and utilizes structured outputs to guarantee the response strictly conforms to the defined Pydantic validation schema before returning data to the client.

**Request Body (application/json):**

```json
{
  "goal": "Build a secure and scalable shopping cart system for an e-commerce platform."
}
```

**Response (200 OK - Structured JSON):**

```json
{
  "epic_title": "E-commerce Secure Shopping Cart Implementation",
  "user_stories": [
    {
      "title": "As a customer, I want to add items to my cart so that I can purchase them later.",
      "story_points": 3,
      "subtasks": [
        {
          "title": "Design Database schema for Cart and CartItems",
          "estimated_hours": 2.5
        },
        {
          "title": "Create POST /cart endpoint to add items",
          "estimated_hours": 4.0
        }
      ]
    }
  ]
}
```

### Error Handling

The application handles edge cases cleanly without server crashes:

- **400 Bad Request:** Triggered if the objective field is empty, missing, or contains only whitespace.
- **500 Internal Server Error:** Triggered if downstream communication with the Gemini API fails or returns invalid schemas.

### Interactive Documentation

Test the validation layers and successful AI requests directly via the native Swagger UI at:
`http://127.0.0.1:8000/docs`

---

## Next Steps

To expand this microservice into a full-stack product, the following building blocks can be implemented next:

- **Frontend UI:** Build a simple Single Page Application (SPA) using React or Vue.js with a single input field to submit the goal and an interactive, clean tree/accordion view to display the generated Agile hierarchy.
- **Direct Jira Integration:** Implement an exporter module using the Jira Cloud REST API to automatically convert the generated JSON payload into active Epics and Issues within a specified Jira project.
- **Export to CSV/Markdown:** Add utility endpoints (`GET /export/csv`, `GET /export/md`) to allow users to instantly download the breakdown structure for documentation or manual project management imports.
- **Persistence Layer:** Introduce a lightweight database (such as PostgreSQL or SQLite) to store past breakdowns, enabling project history tracking and tracking modifications over time.

---

## License

This project is open-source and available under the MIT License.

```

```
