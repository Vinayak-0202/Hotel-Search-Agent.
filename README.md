# 🏠 Airbnb Search Agent

An AI-powered Airbnb Search Agent built using **LangChain**, **Google Gemini**, and the **Airbnb MCP Server (Model Context Protocol)**. The agent allows users to search for Airbnb accommodations using natural language queries and receive intelligent responses powered by Large Language Models (LLMs).

---

## 🚀 Project Overview

This project demonstrates how to integrate an LLM with external tools using the **Model Context Protocol (MCP)**. The agent leverages the Airbnb MCP server to retrieve Airbnb listing information and combines it with additional utility tools such as web search and weather information.

Users can interact with the system through a simple command-line chat interface and ask questions such as:

* Find Airbnb stays in Bangalore for next weekend.
* Show affordable apartments in Goa under ₹5000 per night.
* Suggest Airbnb properties near tourist attractions.
* Find family-friendly accommodations with Wi-Fi and parking.
* What is the weather like in the destination before booking?

---

## 🎯 Use Case

Travel planning often requires searching across multiple platforms for accommodation details, pricing, location information, and travel conditions.

This AI Agent simplifies the process by:

* Understanding natural language travel requests.
* Searching Airbnb listings using MCP tools.
* Providing intelligent recommendations.
* Enhancing travel decisions with additional weather and web search capabilities.
* Delivering a conversational user experience.

---

## 🏗️ Architecture

```text
+------------------+
|      User        |
+--------+---------+
         |
         v
+------------------+
| LangChain Agent  |
+--------+---------+
         |
         v
+--------------------------+
| Google Gemini 2.5 Flash  |
+------------+-------------+
             |
     -------------------
     |        |        |
     v        v        v
+---------+ +---------+ +---------+
| Airbnb  | | Weather | |   Web   |
| MCP     | |  Tool   | | Search  |
| Server  | |         | |  Tool   |
+---------+ +---------+ +---------+
```

### Workflow

1. User enters a natural language query.
2. LangChain Agent receives the query.
3. Gemini LLM analyzes the request.
4. Agent selects the appropriate tool(s).
5. Airbnb MCP Server retrieves accommodation information.
6. Additional tools provide weather and web information if needed.
7. Agent generates a final response for the user.

---

## 🛠️ Technologies Used

### Frameworks

* LangChain
* Model Context Protocol (MCP)

### LLM

* Google Gemini 2.5 Flash

### MCP Integration

* Airbnb MCP Server (`@openbnb/mcp-server-airbnb`)

### Programming Language

* Python 3.10+

### Async Processing

* Asyncio

---

## 📚 Major Libraries Used

| Library                    | Purpose                         |
| -------------------------- | ------------------------------- |
| langchain                  | Agent orchestration             |
| langchain-google-genai     | Gemini model integration        |
| langchain-mcp-adapters     | MCP tool integration            |
| python-dotenv              | Environment variable management |
| asyncio                    | Asynchronous execution          |
| @openbnb/mcp-server-airbnb | Airbnb MCP Server               |

---

## 📂 Project Structure

```text
project/
│
├── airbnb_mcp.py
├── scripts/
│   ├── base_tools.py
│   └── prompts.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

Before running the project, ensure you have:

* Python 3.10+
* Node.js
* npm
* Google Gemini API Key

---

## 🔧 Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd airbnb-search-agent
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## 🔌 Airbnb MCP Configuration

```json
{
  "airbnb": {
    "command": "npx",
    "args": [
      "-y",
      "@openbnb/mcp-server-airbnb",
      "--ignore-robots-txt"
    ],
    "transport": "stdio"
  }
}
```

---

## ▶️ Running the Application

```bash
python airbnb_mcp.py
```

Example:

```text
You: Find Airbnb stays in Goa under ₹5000 per night.
```

---

## 💡 Sample Queries

* Find Airbnb listings in Bangalore near Electronic City.
* Show family-friendly stays in Goa.
* Find budget accommodations in Mumbai.
* Suggest luxury Airbnb properties in Jaipur.
* What is the weather in Goa this weekend?
* Find accommodations near popular tourist attractions.

---

## 🔑 Key Features

* Natural language travel search.
* Airbnb MCP integration.
* LangChain Agent architecture.
* Google Gemini powered reasoning.
* Multi-tool orchestration.
* Weather information support.
* Web search capability.
* Interactive CLI chat experience.
* Asynchronous execution.

---

## 🔮 Future Enhancements

* Streamlit Web UI.
* Voice-based travel assistant.
* Multi-provider hotel search.
* Booking recommendation engine.
* Cost comparison across platforms.
* User preference memory.
* Travel itinerary generation.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit changes.
4. Push to your branch.
5. Create a Pull Request.

---

## 📜 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

Developed as a hands-on AI Agent project using LangChain, Google Gemini, and Airbnb MCP Server.
