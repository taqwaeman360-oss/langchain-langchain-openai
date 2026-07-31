AI Email Generator with LangSmith Observability

An intelligent, modular email generation application built with **LangChain**, **Streamlit**, and fully instrumented with **LangSmith** for real-time execution tracing, debugging, and performance evaluation.

## 🌟 Features

* **Tailored Email Generation**: Specify topic, recipient role, and tone to generate custom professional drafts.
* **LangChain LCEL Pipeline**: Modular, readable chain architecture combining prompts, models, and output parsers.
* **Full Observability with LangSmith**:
  * Step-by-step execution tracing.
  * Prompt and response inspection.
  * Token usage, latency, and model parameter monitoring.
* **Streamlit UI**: Clean and intuitive web application interface.

---

## 📂 Project Structure

```text
├── .github/
│   └── workflows/          # CI/CD pipelines
├── .env                    # Local environment variables (ignored in Git)
├── .gitignore              # Ignored files
├── app.py                  # Streamlit frontend UI
├── email_generator.py      # LangChain chain implementation
├── utils.py                # Input validation and helper logic
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
