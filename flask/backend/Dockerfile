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

# Install .NET SDK
RUN wget https://dot.net/v1/dotnet-install.sh -O dotnet-install.sh \
    && bash dotnet-install.sh --channel 6.0 --install-dir /usr/share/dotnet \
    && ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet \
    && rm dotnet-install.sh

COPY . /app

# Build frontend
WORKDIR /app/flask/frontend
RUN npm install
RUN npm run build

# Install backend Python deps
WORKDIR /app/flask/backend
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.runtime.txt

# Restore and build Roslyn during image build
WORKDIR /app/Roslyn
RUN dotnet restore
RUN dotnet build -c Release

WORKDIR /app/flask/backend

EXPOSE 5000

CMD ["python", "app.py"]