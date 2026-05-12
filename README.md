## Weekly Sprint logs

### Sprint 2: Gateway service designing skeleton (Week 1 - May 2026)
- **Jira Epic:** RAG-1 gateway notebook
**Sprint Summary Wins:**
- [to be filled by weekend]
**Sprint Summary Blockages:**
- [to be filled by weekend]
---
#### Daily Standup Records (Click to expand)
<details>
<summary><b>Day 2 (12 May 2026)</b></summary>
* <b>Objective:</b><br>resolving 404 exception<br> 
* <b>Wins:</b><br>the basic skeleton is ready<br>
* <b>Blockages:</b><br>the ingestion api already accepts param of type UploadFile<br>
While passing the payload i am wrapping around a pydantic schema due to which i am facing json serializable error<br>i should have converted the pydantic object to json string first before passing it using AsyncClient.post()
</details>
<details>
<summary><b>Day 1 (11 May 2026)</b></summary>
* <b>Objective:</b><br>creation of gateway skeleton in notebook<br> 
* <b>Wins:</b><br>designed a pipelines<br>to connect gateway to ingestion service<br>jupyter notebook has its own server running, so uvicorn.config(), nested_asyncio.apply() were used. asyncio.get_event_loop() tells uvicorn to use the same server as jupyter notebook<br> 
* <b>Blockages:</b><br>recieving http exception for it is not able to return vector embedding ids of the doc chunks while calling ingestion service to gateway
</details>

### Sprint 1: Core Ingestion Testing (Week 1 - May 2026)
**Sprint Summary Wins:**
- successully tested and executed ingestion pipeline 
**Sprint Summary Blockages:**
- need to connect ingestion service to gateway service
---
#### Daily Standup Records (Click to expand)
<details>
<summary><b>Day 2 (8th May 2026)</b></summary>
* <b>Objective:</b><br>deciding the structure and request-response flow between gateway service and ingestion service<br> 
* <b>Wins:</b><br>Finished finalizing the core flow between the services (made a rough plan)<br>
* <b>Blockages:</b><br>need to implement in the jupyter notebook in a monolithic manner just to analyze the mechanism between the services
</details>
<details>
<summary><b>Day 1 (7th May 2026)</b></summary>
* <b>Objective:</b><br>Resolved error code number 422 in Postman<br> 
* <b>Wins:</b><br>successfully implemented the Ingestion Service by copying the cURL section mentioned in response field in Swagger UI and importing into Postman<br>
* <b>Blockages:</b><br>Went through the form data, checking the keys and uploaded file size,
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