# 🏭 FastAPI Factory API

A lightweight REST API for managing factory machines and orders, built with FastAPI. Designed for local setup on your own machine.

---

## 🔧 Quick Start

1. **Clone this repo**
   ```bash
   git clone https://github.com/your-username/factory-api.git
   cd factory-api

    Install dependencies

pip install -r requirements.txt

Run the server

    uvicorn main:app --host 127.0.0.1 --port 8000 --reload

📘 API Docs

    Swagger UI: http://127.0.0.1:8000/docs

    ReDoc: http://127.0.0.1:8000/redoc

📡 Endpoints
Method	Endpoint	Description
GET	/machines	List all machines
GET	/machines/{machine_id}/orders	Get orders for a machine
POST	/orders	Create a new order
PUT	/orders/{order_id}	Update an order
DELETE	/orders/{order_id}	Delete an order
🧾 Sample POST /orders

{
  "machine_id": 1,
  "order_name": "Test Order",
  "status": "pending"
}

💡 Requirements

    Python 3.9+

    MySQL (with configured DB)

    Uvicorn / FastAPI / Pydantic

👤 Author

Maintained by Your Name
📧 your.email@example.com


---

✅ Just paste this into your `README.md` and replace:
- `your-username` with your GitHub username
- `Your Name` and `your.email@example.com` with your info

Let me know if you want me to fill those in too!

