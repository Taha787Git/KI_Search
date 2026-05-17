FROM mcr.microsoft.com/devcontainers/python:3.11

ENV DEBIAN_FRONTEND=noninteractive

# Install OS-level dependencies
RUN apt-get update && apt-get install -y \
    unzip \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Switch to the non-root user before installing Python packages
USER vscode

# Create the alias.
# We remove the cd command because devcontainer.json already puts them in the right folder.
RUN echo 'alias check="check50 ai50/projects/2024/x/tictactoe --local"' >> /home/vscode/.bashrc

# Install Harvard's check50 tool and pygame (needed for runner.py UI) for the vscode user
RUN pip install --no-cache-dir check50 pygame

ENV DEBIAN_FRONTEND=dialog
