
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
def variance_cal( signal_arr):
    # Tính độ lệch chuẩn của mảng
    signal_mean = np.average(signal_arr)
    print("Signal mean:",signal_mean)

    std_deviation = np.std(signal_arr/signal_mean)
    variance = np.var(signal_arr/signal_mean)
    gap = np.max(signal_arr) - np.min(signal_arr)
    print(signal_arr)
    print("std_deviation: ", std_deviation)
    print("variance: ", variance)
    print("Gap: ", gap)
    return gap

# Xác định ngưỡng để phân loại mảng là "PASS" hoặc "FAIL"
threshold = 1.0 

# Thời gian mẫu (từ 0 đến 5 giây) và tần số mẫu (Hz)
freq_max = 2
sample_rate = 50  # Số mẫu trên mỗi giây
t = np.linspace(0, 1, sample_rate, endpoint=False)

# Tạo chuỗi tín hiệu sóng sin với tần số từ 1Hz đến 5Hz
frequencies = np.linspace(1, freq_max, freq_max)  # Tần số từ 1Hz đến 5Hz
waveforms = [np.sin(2 * np.pi * f * t)*10 for f in frequencies]
# print(waveforms)
signal_full = np.concatenate(waveforms) 

# Tạo tần số bị lỗi (ví dụ: thêm nhiễu vào tần số 3Hz)
error_frequency = 3  # Tần số bị lỗi (Hz)
error_waveform =  np.sin(2 * np.pi * error_frequency * t[:len(waveforms[0])]) + 0.5 * np.random.randn(len(waveforms[0]))
# error_waveform[int(-sample_rate/2):] = 0
# print("error:", error_waveform)
print("Signal Max:", np.max(waveforms))
print("Noise  Max:", np.max(error_waveform))
print("Rate:", np.max(waveforms) / np.max(error_waveform))

# Cộng error_waveform vào phần tử thứ 3 của danh sách waveforms
# waveforms[2] += error_waveform
# waveforms[1] += error_waveform
waveforms[1] = np.full(len(waveforms[1]), 3)

# Tổng hợp tất cả các tín hiệu (bao gồm tần số bị lỗi)
# print(len(waveforms))
# print(len(error_waveform))
signal_full_noise = np.concatenate(waveforms) 
# print(len(signal_full))

t = np.linspace(0, freq_max, len(signal_full), endpoint=False)

# Thực hiện FFT
fft_result = np.fft.fft(signal_full)
fft_result_noise = np.fft.fft(signal_full_noise)
# print("fft result abs", np.abs(fft_result))
# print("len fft result", len(fft_result))
fft_freqs = np.fft.fftfreq(len(fft_result), 1/sample_rate)  # Tính tần số tương ứng với các thành phần FFT
# print("fft_freqs: \n",fft_freqs)

num_samples = len(signal_full)
y = np.abs(fft_result)
y_noise = np.abs(fft_result_noise)
# y[0] = y[num_samples - 1]  = 0
print("Signal:")
var1 = variance_cal(y[5:25])
print("Signal Noise:")
var2 = variance_cal(y_noise[5:25])
print("Var rate: ", (var2/var1))




# Vẽ biểu đồ tín hiệu và phổ tần số
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, signal_full_noise)
plt.title('Tín hiệu dạng sine (1-5 Hz)')
plt.xlabel('Thời gian (s)')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(fft_freqs, y)
plt.plot(fft_freqs, np.full(num_samples, np.average(y[5:25])), linestyle='--', color='red')
plt.title('Phổ tần số sin')
plt.xlabel('Tần số (Hz)')
# plt.xlim(0, 10)  # Giới hạn dải tần số từ -10 đến 10 Hz
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(fft_freqs, y_noise)
plt.plot(fft_freqs, np.full(num_samples, np.average(y_noise[5:25])), linestyle='--', color='red')
plt.title('Phổ tần số noise')
plt.xlabel('Tần số (Hz)')
# plt.xlim(0, 10)  # Giới hạn dải tần số từ -10 đến 10 Hz
plt.grid()

plt.tight_layout()
plt.show()
