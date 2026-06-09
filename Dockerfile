# 1. Use the lightweight Python 3.12 image as requested
FROM python:3.12-slim

# 2. Set up permissions first so Hugging Face can run securely (UID 1000)
RUN useradd -m -u 1000 user
USER user

# 3. Configure environmental variables for the local user path
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONUNBUFFERED=1

# 4. Set the working directory inside the user's home space
WORKDIR $HOME/app

# 5. Copy requirements first and assign ownership to the user
COPY --chown=user requirements.txt $HOME/app/requirements.txt

# 6. Install dependencies safely as the non-root user
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r $HOME/app/requirements.txt

# 7. Copy all other project files and directories (src, templates, static, etc.)
# and explicitly grant ownership to the user to prevent runtime permission blocks
COPY --chown=user . $HOME/app

# 8. Run uvicorn on Hugging Face's mandatory port 7860
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]