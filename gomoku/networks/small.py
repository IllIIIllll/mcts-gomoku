# © 2020 지성. all rights reserved.
# <llllllllll@kakao.com>
# Apache License 2.0

from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.layers import Conv2D, ZeroPadding2D

# 오목 수 예측용 작은 합성곱 신경망 층 정의
def layers(input_shape):
    return [
        # 층에 제로패딩을 사용하여 입력 이미지 크기 증가
        ZeroPadding2D(padding=3, input_shape=input_shape, data_format='channels_first'),
        Conv2D(48, (7, 7), data_format='channels_first'),
        Activation('relu'),

        ZeroPadding2D(padding=2, data_format='channels_first'),
        Conv2D(32, (5, 5), data_format='channels_first'),
        Activation('relu'),

        ZeroPadding2D(padding=2, data_format='channels_first'),
        Conv2D(32, (5, 5), data_format='channels_first'),
        Activation('relu'),

        ZeroPadding2D(padding=2,data_format='channels_first'),
        Conv2D(32, (5, 5), data_format='channels_first'),
        Activation('relu'),

        Flatten(),
        Dense(512),
        Activation('relu'),
    ]