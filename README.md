# README.md

# Resume Analyzer + LinkedIn/Naukri Job Fetcher + MCP Server

This project allows you to:

- Upload a Resume (PDF)
- Analyze Resume Summary, Skill Gaps, and Future Roadmap using EURI AI
- Auto-fetch matching jobs from LinkedIn and Naukri using Apify
- Wrap the job fetch functions into a FastMCP Server for integration with external tools like Claude Desktop, MCP Inspector, etc.

# 💪 Full Setup Instructions

## 1. Clone the Repository

```bash
git clone <your-repo-link>
cd resume_job_fetcher_project
```

## 2. Create Conda Virtual Environment (Recommended)

```bash
conda create -n resume_fetcher_env python=3.10
conda activate resume_fetcher_env
```

## 3. Install Required Packages

Using pip:

```bash
pip install -r requirements.txt
```

requirements.txt contains:

- streamlit
- pymupdf
- euriai
- python-dotenv
- apify-client
- fastmcp

Alternatively, using UV:

Install UV on Windows Powershell:

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Install requirements:

```bash
uv pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file:

```plaintext
EURI_API_KEY=your_real_euri_api_key_here
APIFY_API_TOKEN=your_real_apify_api_token_here
```

## 5. Run the Streamlit App

```bash
streamlit run app.py
```

## 6. Run MCP Server (FastMCP)

```bash
python mcp_server.py
```

## 7. Test MCP Server (Optional)

Install MCP Inspector:

```bash
npm install -g @modelcontextprotocol/inspector
```

Run the Inspector:

```bash
npx @modelcontextprotocol/inspector python mcp_server.py
```

# 🚀 UV-Based Project Setup (Optional)

```bash
uv init mcp-server-demo
cd mcp-server-demo
uv add "mcp[cli]"
```

To manually install MCP CLI:

```bash
pip install "mcp[cli]"
```

Running standalone MCP locally:

```bash
uv run mcp
```

# 📆 Project Structure

```plaintext
resume_job_fetcher_project/
├── app.py          # Streamlit frontend app
├── mcp_server.py   # FastMCP server exposing job fetchers
├── requirements.txt
├── README.md
└── .env            # API keys configuration
```

# 🌟 Technology Stack

| Component              | Technology                       |
| :--------------------- | :------------------------------- |
| Resume Analysis        | EURI AI (GPT-4.1-nano)           |
| Job Fetching           | Apify (LinkedIn + Naukri Actors) |
| Frontend               | Streamlit                        |
| MCP Server             | FastMCP                          |
| Environment Management | Conda / UV                       |
| Inspector Tool         | MCP Inspector                    |

# 📃 Important Links

- [EURI API Documentation](https://api.euron.one/docs)
- [Apify API Documentation](https://docs.apify.com/)
- [FastMCP GitHub](https://github.com/modelcontextprotocol/fastmcp)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [UV Installation Guide](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)
- [MCP Inspector GitHub](https://github.com/modelcontextprotocol/inspector)

# 🔫 Quick Commands Summary

| Task                 | Command                                                                       |
| :------------------- | :---------------------------------------------------------------------------- |
| Create Conda Env     | `conda create -n resume_fetcher_env python=3.10`                            |
| Activate Env         | `conda activate resume_fetcher_env`                                         |
| Install Packages     | `pip install -r requirements.txt` or `uv pip install -r requirements.txt` |
| Run App              | `streamlit run app.py`                                                      |
| Run MCP Server       | `python mcp_server.py`                                                      |
| Launch MCP Inspector | `npx @modelcontextprotocol/inspector python mcp_server.py`                  |

# 💪 Conclusion

- Resume Analyzer + Live Job Fetcher using AI 🚀
- Fully ready MCP tool server integration
- Modular, scalable, and professional setup

# 🚀 Let's Build Smarter Applications Faster with AI, Apify, MCP & Streamlit!
