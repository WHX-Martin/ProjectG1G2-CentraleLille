import numpy as np


# 定义旋转矩阵
def rotation_matrix(alpha, beta, gamma):
    """
    绕 x, y, z 轴的旋转矩阵
    alpha: 绕 x 轴的旋转角 (roll)
    beta: 绕 y 轴的旋转角 (pitch)
    gamma: 绕 z 轴的旋转角 (yaw)
    """
    # alpha = np.radians(alpha)
    # beta = np.radians(beta)
    # gamma = np.radians(gamma)
    Rx = np.array(
        [
            [1, 0, 0],
            [0, np.cos(alpha), -np.sin(alpha)],
            [0, np.sin(alpha), np.cos(alpha)],
        ]
    )
    Ry = np.array(
        [[np.cos(beta), 0, np.sin(beta)], [0, 1, 0], [-np.sin(beta), 0, np.cos(beta)]]
    )
    Rz = np.array(
        [
            [np.cos(gamma), -np.sin(gamma), 0],
            [np.sin(gamma), np.cos(gamma), 0],
            [0, 0, 1],
        ]
    )
    return Rz @ Ry @ Rx  # 组合旋转矩阵


a = np.array([1, 0, 0])
print(a)
b = rotation_matrix(np.pi / 2, np.pi / 2, np.pi / 2) @ a
print(b)

c = np.array("[[1,0,0],[0,1,0],[0,0,1]]")
print(c)
