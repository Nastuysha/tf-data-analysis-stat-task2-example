import pandas as pd
import numpy as np

chat_id = 1141722952 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    left = (max(x) - 1 / 2) / (50**2 / 2)
    right = (-np.log(alpha) / n + max(x) - 1 / 2) / (50**2 / 2)
    return left, right

