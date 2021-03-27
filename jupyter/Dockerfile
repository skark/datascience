FROM ubuntu:latest as build

ENV CONDA_DIR=/condinst
ENV PATH=$PATH:$CONDA_DIR/bin

COPY startup/*.py /root/.ipython/profile_default/startup/

RUN set -o xtrace \ 
	&& apt-get update \
	&& apt-get -y full-upgrade \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y git wget keychain libsm6 libxext6 libxrender1 dvipng cm-super texlive-latex-extra texlive-fonts-recommended \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& wget -nv https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
	&& /bin/bash Miniconda3-latest-Linux-x86_64.sh -f -b -p $CONDA_DIR \
	&& rm Miniconda3-latest-Linux-x86_64.sh \
	&& $CONDA_DIR/bin/conda install -q -y  \
		numpy \
		pandas \
		scikit-learn \
		seaborn \
		sympy \
		bcolz \
		ipywidgets \
		tensorflow-mkl">=2.2.0" \	
	&& $CONDA_DIR/bin/conda install -q -y pytorch torchvision torchtext cpuonly -c pytorch \
	&& $CONDA_DIR/bin/conda install -q -y feather-format -c conda-forge \
	&& $CONDA_DIR/bin/conda install -q -y scipy -c conda-forge \
	&& $CONDA_DIR/bin/conda install -q -y matplotlib -c conda-forge \
	&& $CONDA_DIR/bin/conda install -q -y scikit-image -c conda-forge \
	&& $CONDA_DIR/bin/conda install -q -y spacy -c conda-forge \
	&& $CONDA_DIR/bin/conda install -q -y statsmodels -c conda-forge \
	&& $CONDA_DIR/bin/conda install -q -y nodejs">=12.4.0" -c conda-forge \
	&& $CONDA_DIR/bin/conda install -q -y ipympl">=0.5.6" -c conda-forge \
	&& $CONDA_DIR/bin/conda install -q -y jupyterlab -c conda-forge \	
	&& $CONDA_DIR/bin/conda install -q -y notebook -c conda-forge \	
	&& $CONDA_DIR/bin/jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib \
	&& $CONDA_DIR/bin/conda update -y python \
	&& $CONDA_DIR/bin/conda clean -a -y \
	&& $CONDA_DIR/bin/pip install --no-cache-dir sklearn-pandas isoweek pandas_summary \
	&& find $CONDA_DIR -type f -name "*.py[co]" -delete \
	&& find $CONDA_DIR -type f -name "*.js.map" -delete \
	&& find $CONDA_DIR -path '*/__pycache__/*' -delete \
	&& find $CONDA_DIR -type d -name "__pycache__" -delete \
	&& date >/build-date.txt \
	&& set +o xtrace

# apt-get install -y rdfind 
#	&& for n in {1..20}; do rdfind -checksum sha1 -makehardlinks true -makeresultsfile false /usr /root $CONDA_DIR; done \
#	&& apt remove -y rdfind \	
#		opencv \	
#	&& $CONDA_DIR/bin/conda update --all -y  \
#	&& $CONDA_DIR/bin/conda install -q -y opencv -c conda-forge \

#FROM scratch as final
#COPY --from=build / /

FROM build
COPY unittest.py /work/tx.py
RUN $CONDA_DIR/bin/python /work/tx.py

FROM build
WORKDIR /work
EXPOSE 8888
ENTRYPOINT ["/condinst/bin/jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.allow_origin='*'", "--NotebookApp.token=''"]
