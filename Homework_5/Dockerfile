# Start from the base image (jismein python aur pipeline_v2.bin hai)
FROM agrigorev/zoomcamp-model:2025

# Hamare server ko chalane ke liye zaroori packages install karo
# 1. fastapi: Web app banane ke liye
# 2. uvicorn: Server run karne ke liye
# 3. scikit-learn: Model (.bin file) ko load karne ke liye
RUN pip install fastapi uvicorn scikit-learn

# Apni Q6 waali Python script ko container mein copy karo
COPY main_q6.py .

# Container ka port 8000 bahar ki duniya ke liye open karo
EXPOSE 8000

# Jab container start ho, toh yeh command chalao
CMD ["uvicorn", "main_q6:app", "--host", "0.0.0.0", "--port", "8000"]