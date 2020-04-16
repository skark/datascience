FROM mcr.microsoft.com/dotnet/core/sdk:latest as build

ENV CONDA_DIR=/condinst \
        DOTNET_CLI_TELEMETRY_OPTOUT=true \
        PATH="$PATH:$CONDA_DIR/bin:/root/.dotnet/tools"

RUN set -o xtrace \
        && apt-get update \
        && apt-get -y dist-upgrade \
        && DEBIAN_FRONTEND=noninteractive apt-get install -y wget \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* \
        && wget -nv https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
        && /bin/bash Miniconda3-latest-Linux-x86_64.sh -f -b -p $CONDA_DIR \
        && rm Miniconda3-latest-Linux-x86_64.sh \
        && $CONDA_DIR/bin/conda install -q -y jupyterlab notebook -c conda-forge        
        && $CONDA_DIR/bin/conda update -y python \
        && $CONDA_DIR/bin/conda clean -a -y \
        && find $CONDA_DIR -type f -name "*.py[co]" -delete \
        && find $CONDA_DIR -type f -name "*.js.map" -delete \
        && find $CONDA_DIR -path '*/__pycache__/*' -delete \
        && find $CONDA_DIR -type d -name "__pycache__" -delete \
        && dotnet tool install -g --add-source "https://dotnet.myget.org/F/dotnet-try/api/v3/index.json" Microsoft.dotnet-interactive \
        && export PATH="$PATH:$CONDA_DIR/bin:/root/.dotnet/tools" \
        && dotnet interactive jupyter install \
        && date >/build-date.txt \
        && set +o xtrace

FROM build
WORKDIR /work
EXPOSE 8889
ENTRYPOINT ["/condinst/bin/jupyter", "lab", "--ip=0.0.0.0", "--port=8889", "--allow-root", "--no-browser", "--NotebookApp.allow_origin='*'", "--NotebookApp.token=''"]
