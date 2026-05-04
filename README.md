## Weekly Sprint logs
### Sprint 1: 
- **Jira Epic:** INGEST-1 Ingestion Service Architecture
**Sprint Summary Wins:**
- [To be filled at the end of the week]
**Sprint Summary Blockages:**
- [To be filled at the end of the week]
---
#### Daily Standup Records (Click to expand)
<details>
<summary><b>Day 1 (4 May 2026)</b></summary>
* **Objective:** resolve error code number 422 in Postman 
* **Wins:** successfully implemented the Ingestion Service by copying the cURL section mentioned in response field in Swagger UI and importing into Postman
* **Blockages:** went through the form data, checking the keys and uploaded file size,
made sure path is correct, tested the complete ingestion pipeline in Swagger UI
</details>


## Project History & Evolution
### Sprint 0: The Architectural Pivot (mid-March to early May 2026)
- **Status:** Completed
- **The evolution:**
  This project began as a standard, monolithic Jupyter Notebook to parse and ingest a PDF. As the limitation of single-threaded python scripts became clear, I shifted the paradigm. I spent weeks tranforming a simple POC into a decoupled, production-grade microservice architecture.

**Key Milestones Achieved:**
- **Notebook to Modular Structure:** Implmented in '.ipynb' file to get skeleton ready and scaffolded pure, modular Python packages with custom folder layouts.
- **System Design:** Sketched UML diagrams mapping out a 5-service decoupled system (Gateway, Ingestion, Retrieval, Generation, Evaluation).
- **Asynchronous Planning:** Identified heavy parsing bottlenecks and mapped out the integration of Celery, RabbitMQ, and Jenkins into my wishlist.

**Major Blockages Overcome:**
- **The monolithic Mindset:** Resisted the urge to write easy, synchronous code. Spent time researching destributed communications (FastAPI Gateway to down-stream Ingestion router via HTTPX)