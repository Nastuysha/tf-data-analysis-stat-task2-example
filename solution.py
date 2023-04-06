import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 1141722952

def solution(p: float, x: np.array) -> tuple:
    alpha = p
    time = 50
    return (2 * np.mean(x) / time ** 2 -  norm.ppf(1 - alpha / 2, scale=2) / time ** 2, 2 * np.mean(x) / time ** 2 - norm.ppf(alpha / 2, scale=2) / time ** 2)
