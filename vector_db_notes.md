# Vector Database Comparison

| Feature | Local Vector DB (Chroma) | Cloud Vector DB (Pinecone, Weaviate Cloud, Qdrant Cloud) |
|---------|---------------------------|-----------------------------------------------------------|
| Deployment | Runs on your local machine | Hosted and managed in the cloud |
| Cost | Free | Free tier available, paid plans for production |
| Free-tier limits | Limited only by your local disk and memory | Limited storage, vectors, and API requests |
| Latency | Very low because data is stored locally | Slightly higher due to network communication |
| Ease of setup | Very easy (`pip install chromadb`) | Requires account creation, API keys, and configuration |
| Scalability | Suitable for development and small projects | Designed for large-scale production workloads |
| Persistence | Stored on local disk using `PersistentClient` | Managed by the cloud provider |
| Maintenance | User manages backups and updates | Provider manages infrastructure, backups, and scaling |
| Enterprise access control | Application must implement user authentication and metadata filtering (for example, filtering by `member_id` or `plan_id`) | Built-in authentication, API keys, RBAC, namespaces, and metadata filtering for secure multi-tenant deployments |

---

# Choice for This Project

For this insurance chatbot project, I chose **ChromaDB** because it is free, lightweight, and easy to set up. It integrates well with Python, stores embeddings persistently on disk using `PersistentClient`, and is ideal for learning Retrieval-Augmented Generation (RAG) concepts without requiring cloud infrastructure or API keys. Although cloud vector databases are better suited for large enterprise deployments with automatic scaling and built-in security features, ChromaDB provides all the functionality needed for this project while keeping development simple and cost-effective.