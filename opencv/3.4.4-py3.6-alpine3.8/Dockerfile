FROM            python:3.6.7-alpine3.8

ENV             VERSION="3.4.4"

RUN             mkdir -p /usr/src/app && \
                wget -q -O - https://github.com/opencv/opencv/archive/${VERSION}.tar.gz | tar xz -C /usr/src/app && \
                wget -q -O - https://github.com/opencv/opencv_contrib/archive/${VERSION}.tar.gz | tar xz -C /usr/src/app && \

                apk add --no-cache --virtual .build-deps \
                    build-base \
                    ninja \
                    linux-headers \
                    # yasm \
                    # pkg-config \
                    # libswscale-dev \
                    # libtbb2 \
                    # libavformat-dev \
                    # libpq-dev
                    jpeg-dev \
                    libjpeg-turbo-dev \
                    libpng-dev \
                    tiff-dev && \
                apk add --no-cache --virtual .build-deps -X http://dl-cdn.alpinelinux.org/alpine/edge/main -X http://dl-cdn.alpinelinux.org/alpine/edge/testing \
                    cmake \
                    libtbb-dev && \
                pip -v install numpy && \

                mkdir -p /usr/src/app/opencv-${VERSION}/build && \
                cd /usr/src/app/opencv-${VERSION}/build && \
                cmake -GNinja -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=/usr/local \
                    # -DBUILD_opencv_python=ON \
                    # -DBUILD_opencv_python2=OFF \
                    # -DBUILD_opencv_python3=ON \
                    -DPYTHON_EXECUTABLE=$(which python) \
                    -DPYTHON3_EXECUTABLE=$(which python3) \
                    -DPYTHON_INCLUDE_DIR=$(python -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
                    -DPYTHON_PACKAGES_PATH=$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \
                    -DPYTHON_LIBRARY=/usr/local/libpython3.so \

                    # -DPYTHON3_NUMPY_INCLUDE_DIRS = /usr/lib/python<version>/dist-packages/numpy/core/include/

                    # -DBUILD_opencv_java=OFF \

                    -DBUILD_DOCS=OFF \
                    -DBUILD_EXAMPLES=OFF \
                    -DBUILD_TESTS=OFF \
                    -DBUILD_PERF_TESTS=OFF \

                    # -DOPENCV_EXTRA_MODULES_PATH=/usr/src/app/opencv_contrib-${VERSION}/modules \

                    # -DBUILD_SHARED_LIBS=OFF \

                    # -DENABLE_AVX=ON \
                    # -DWITH_OPENGL=ON \
                    # -DWITH_OPENCL=ON \
                    -DBUILD_TIFF=ON \
                    # -DWITH_IPP=ON \
                    # -DWITH_CUDA=OFF \
                    # -DWITH_IPP=ON \
                    # -DWITH_TBB=ON \
                    # -DWITH_EIGEN=ON \
                    # -DWITH_V4L=ON \
                    -DBUILD_SHARED_LIBS=OFF \
                .. && \
                ninja && \
                ninja install && \
                ninja clean && \
                # apk add --no-cache .virtual .run-deps \
                #     libtbb \
                #     jpeg \
                #     libjpeg-turbo \
                #     libpng \
                #     tiff && \
                apk del .build-deps

RUN             ln /usr/local/python/cv2/python-3.6/cv2.cpython-36m-x86_64-linux-gnu.so /usr/local/lib/python3.6/site-packages/cv2.so
