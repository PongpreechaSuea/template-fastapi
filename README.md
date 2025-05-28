# template-fastapi

**A starter template for building FastAPI-based backend applications.**  
This template helps you quickly spin up a new FastAPI project with sensible defaults, project structure, and ready-to-use configurations.

## 🚀 Features

- FastAPI framework
- Built-in project structure for scalability
- Uvicorn for ASGI server
- Example endpoints included
- Docker-ready
- `.env` support for environment configuration
- Pre-configured linting and formatting (optional)

## 📁 Project Structure

```
template-fastapi/
├── app/
│ ├── main.py # Entry point
│ ├── api/ # API routes
│ ├── core/ # Core configurations
│ ├── models/ # Data models
│ └── services/ # Business logic
├── .env # Environment variables
├── requirements.txt # Dependencies
├── Dockerfile # Docker configuration
└── README.md # Project info
```

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/PongpreechaSuea/template-fastapi.git
cd template-fastapi
```

### 2. Create a virtual environment and install dependencies

#### Installation

##### **1. ติดตั้ง Miniconda บน macOS**

หากคุณยังไม่มี Miniconda สามารถติดตั้งได้ตามขั้นตอนนี้:

1. **ดาวน์โหลด Miniconda**  
   เปิด Terminal และใช้คำสั่งนี้เพื่อดาวน์โหลด Miniconda:

```bash
curl -o Miniconda3-latest-MacOSX-x86_64.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
```

2. **ติดตั้ง Miniconda**  
   หลังจากดาวน์โหลดเสร็จแล้ว ติดตั้งด้วยคำสั่งนี้:

```bash
bash Miniconda3-latest-MacOSX-x86_64.sh
```

- เมื่อระบบถามให้กด **Enter** เพื่อดูข้อตกลงการใช้งาน
- กด **'yes'** เพื่อยอมรับข้อตกลง
- กด **Enter** เพื่อเลือกตำแหน่งติดตั้ง (สามารถใช้ค่า default ได้)

3. **Activate Conda Environment**  
   หลังจากติดตั้งเสร็จ ให้เปิดใช้งาน Miniconda ด้วยคำสั่งนี้:

```bash
source ~/.bashrc
```

หรือถ้าใช้ `zsh` ให้ใช้คำสั่งนี้แทน:

```bash
source ~/.zshrc
```

4. **ตรวจสอบว่าติดตั้งสำเร็จหรือไม่**  
   ใช้คำสั่งนี้เพื่อตรวจสอบว่า Conda ติดตั้งสำเร็จหรือไม่:

```bash
conda --version
```

---

#### **2. ตั้งค่า Environment และติดตั้ง Dependencies**

หลังจากติดตั้ง Miniconda สำเร็จ ให้ทำตามขั้นตอนต่อไปนี้:

1. **Set up environment variables in the `.env` file.**

2. **ให้สิทธิ์ไฟล์ setup.sh**

```bash
chmod +x setup.sh
```

3. **รันไฟล์ setup.sh เพื่อสร้าง Environment**

```bash
./setup.sh
```

4. **Activate Environment**

```bash
conda activate file-service
```

5. **ตรวจสอบ Python เวอร์ชัน**

```bash
python --version    # Python 3.9.16
```

### 3. Run the app locally

```bash
uvicorn app.main:app --reload
```

### 4. Access your app

Open your browser and navigate to: http://localhost:8000

### 5. API Documentation

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## 🐳 Docker (Optional)

To run the project using Docker:

```bash
docker build -t template-fastapi .
docker run -d -p 8000:8000 template-fastapi
```

## 🛠️ Customize This Template

When starting a new project:

Rename the project folder

Update module names, routes, and configs

Replace or extend the structure as needed
