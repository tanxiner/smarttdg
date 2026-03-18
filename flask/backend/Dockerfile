FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    wget \
    nodejs \
    npm \
    libreoffice-writer \
    libreoffice-core \
    libreoffice-common \
    && rm -rf /var/lib/apt/lists/*

# Install .NET SDK (safe method)
RUN wget https://dot.net/v1/dotnet-install.sh -O dotnet-install.sh \
    && bash dotnet-install.sh --channel 6.0 --install-dir /usr/share/dotnet \
    && ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet \
    && rm dotnet-install.sh

COPY . .

WORKDIR /app/flask/frontend
RUN npm install
RUN npm run build

WORKDIR /app/flask/backend
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]