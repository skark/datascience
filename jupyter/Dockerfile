FROM ubuntu:latest

ENV CONDA_DIR=/condinst

RUN apt-get update \
	&& apt-get -y dist-upgrade \
	&& apt-get install -y wget keychain libsm6 libxext6 libxrender1 \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
	&& /bin/bash Miniconda3-latest-Linux-x86_64.sh -f -b -p $CONDA_DIR \
	&& rm Miniconda3-latest-Linux-x86_64.sh \
	&& $CONDA_DIR/bin/conda update -y python \
	&& $CONDA_DIR/bin/conda install -y  \
		keras \
		matplotlib \
		notebook \
		numpy \
		opencv \
		pandas \
		scikit-image \
		scikit-learn \
		scipy \
		seaborn \
		sympy \
		tensorflow \
		bcolz \
		spacy \
	&& $CONDA_DIR/bin/conda install -y pytorch-cpu torchvision-cpu -c pytorch \
	&& $CONDA_DIR/bin/conda install -y feather-format -c conda-forge \
	&& $CONDA_DIR/bin/conda update --all -y  \
	&& $CONDA_DIR/bin/conda clean -a -y \
	&& pip install sklearn-pandas isoweek pandas_summary torchtext

WORKDIR /work

EXPOSE 8888

ENTRYPOINT ["/condinst/bin/jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''"]
