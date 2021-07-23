FROM rapid7/insightconnect-python-3-38-plugin:4
# The three supported python parent images are:
# - komand/python-2-plugin
# - komand/python-3-plugin
# - komand/python-pypy3-plugin
#
LABEL organization=komand

# Add any custom package dependencies here
# NOTE: Add pip packages to requirements.txt

# End package dependencies

RUN apt-get update && apt-get install -y g++ wget autoconf make libtool libtool-bin && rm -rf /var/lib/apt/lists/*
RUN wget -O cmake-install https://github.com/Kitware/CMake/releases/download/v3.13.0/cmake-3.13.0-Linux-x86_64.sh; /bin/sh cmake-install --skip-license --prefix=/usr --exclude-subdirectory;

# Add source code
WORKDIR /python/src
ADD ./plugin.spec.yaml /plugin.spec.yaml
ADD . /python/src

# Install pip dependencies
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Install plugin
RUN python setup.py build && python setup.py install

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]

CMD ["app.handler"]