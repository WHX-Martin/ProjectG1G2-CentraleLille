import numpy as np
from scipy.optimize import least_squares


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


# 定义非线性方程组
def system_of_equations(
    x, positions_bouteilles, position_theorique_projecteur, Angles_réél_projecteur
):
    """
    定义非线性方程组
    x: 状态变量 [delta_x, delta_y, delta_z, delta_alpha, delta_beta, delta_gamma]
    positions_bouteilles: 瓶子的位置列表 [[x_B1, y_B1, z_B1], ...]
    position_theorique_projecteur: 投影仪的理论位置 [x_t, y_t, z_t]
    Angles_réél_projecteur: 实际测量角度 [[pan1, tilt1], ...]
    """
    delta_x, delta_y, delta_z, delta_alpha, delta_beta, delta_gamma = x
    x_t, y_t, z_t = position_theorique_projecteur

    # 计算旋转矩阵
    R = rotation_matrix(delta_alpha, delta_beta, delta_gamma)

    residuals = []
    for i, (x_B, y_B, z_B) in enumerate(positions_bouteilles):
        # 计算瓶子在投影仪坐标系中的位置
        r_global = np.array(
            [x_B - x_t - delta_x, y_B - y_t - delta_y, z_B - z_t - delta_z]
        )
        r_local = np.linalg.inv(R) @ r_global  # 转换到局部坐标系

        # 计算 pan 和 tilt 角度
        pan_measured, tilt_measured = Angles_réél_projecteur[i]
        pan_measured, tilt_measured = np.radians(pan_measured), np.radians(
            tilt_measured
        )

        # pan 角度方程
        pan_calculated = np.arctan2(r_local[1], r_local[0])
        f_pan = np.tan(pan_measured) - np.tan(pan_calculated)

        # tilt 角度方程
        tilt_calculated = np.arccos(r_local[2] / np.linalg.norm(r_local))
        f_tilt = np.cos(tilt_measured) - np.cos(tilt_calculated)

        residuals.extend([f_pan, f_tilt])

    return residuals


# 主函数
def fonction_finale4B(
    Angles_réél_projecteur, positions_bouteilles, position_theorique_projecteur
):
    """
    主函数：求解投影仪的位置和角度偏差
    Angles_réél_projecteur: 实际测量角度 [[pan1, tilt1], ...]
    positions_bouteilles: 瓶子的位置列表 [[x_B1, y_B1, z_B1], ...]
    position_theorique_projecteur: 投影仪的理论位置 [x_t, y_t, z_t]
    """
    # 初始值
    x0 = np.array(
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    )  # [delta_x, delta_y, delta_z, delta_alpha, delta_beta, delta_gamma]
    # 定义边界
    lower_bounds = [
        -1.0,
        -1.0,
        -1.0,
        -1.0,
        -1.0,
        -1.0,
    ]  # delta_x, delta_y, delta_z 的范围为 [-1, 1]
    upper_bounds = [
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
    ]  # delta_alpha, delta_beta, delta_gamma 无限制
    # 最小二乘优化（不使用雅可比矩阵）

    res = least_squares(
        system_of_equations,
        x0,
        args=(
            positions_bouteilles,
            position_theorique_projecteur,
            Angles_réél_projecteur,
        ),
        method="trf",  # Trust Region Reflective 算法
        loss="soft_l1",  # 使用 soft_l1 损失函数处理异常值
        f_scale=0.2,  # 损失函数的缩放因子
        # bounds=(lower_bounds, upper_bounds),
        xtol=1e-8,  # 提高 x 的收敛精度
        ftol=1e-8,  # 提高残差的收敛精度
        max_nfev=1000,  # 增加最大迭代次数
    )

    return res.x, res.cost, res.fun, res.message


if __name__ == "__main__":
    # # 测试数据
    # positions_bouteilles = [
    #     [-1.993, 0, 1.09],
    #     [-12.45, -0.802, 1.827],
    #     [0, -6.019, 2.418],
    #     [-5.375, -6.049, 1.402],
    # ]
    # position_theorique_projecteur = [-4.383, -0.573, 1.06]
    # Angles_réél_projecteur = [
    #     [-165, -92.13],
    #     [3.7, -87.24],
    #     [-230.7, -82.1],
    #     [79.95, -89.3],
    # ]
    # 测试数据
    position_theorique_projecteur = [0, 0, 0]  # 投影仪的理论位置
    positions_bouteilles = [
        [1.0, 2.0, 0.5],  # 瓶子 1
        [-1.0, 2.0, 0.5],  # 瓶子 2
        [1.0, -2.0, 0.5],  # 瓶子 3
        [-1.0, -2.0, 0.5],  # 瓶子 4
    ]

    # 投影仪的实际位置和角度偏差
    delta_x_true = 0.1  # 实际 x 偏差
    delta_y_true = -0.2  # 实际 y 偏差
    delta_z_true = 0.05  # 实际 z 偏差
    delta_alpha_true = 0.05  # 实际 roll 偏差（绕 x 轴）
    delta_beta_true = -0.1  # 实际 pitch 偏差（绕 y 轴）
    delta_gamma_true = 0.02  # 实际 yaw 偏差（绕 z 轴）

    # 计算测量角度
    def calculate_angles(
        position_bouteille, position_projecteur, delta_alpha, delta_beta, delta_gamma
    ):
        """
        计算瓶子的测量角度（pan 和 tilt）
        position_bouteille: 瓶子的位置 [x_B, y_B, z_B]
        position_projecteur: 投影仪的实际位置 [x_t + delta_x, y_t + delta_y, z_t + delta_z]
        delta_alpha, delta_beta, delta_gamma: 投影仪的角度偏差
        """
        x_B, y_B, z_B = position_bouteille
        x_t, y_t, z_t = position_projecteur

        # 计算瓶子在投影仪坐标系中的位置
        r_global = np.array([x_B - x_t, y_B - y_t, z_B - z_t])
        R = rotation_matrix(delta_alpha, delta_beta, delta_gamma)
        r_local = np.linalg.inv(R) @ r_global

        # 计算 pan 和 tilt 角度
        pan = np.arctan2(r_local[1], r_local[0])  # pan 角度
        tilt = np.arccos(r_local[2] / np.linalg.norm(r_local))  # tilt 角度

        return np.degrees(pan), np.degrees(tilt)  # 将弧度转换为角度

    # 投影仪的实际位置
    position_projecteur_true = [
        position_theorique_projecteur[0] + delta_x_true,
        position_theorique_projecteur[1] + delta_y_true,
        position_theorique_projecteur[2] + delta_z_true,
    ]

    # 计算每个瓶子的测量角度
    Angles_réél_projecteur = [
        calculate_angles(
            bouteille,
            position_projecteur_true,
            delta_alpha_true,
            delta_beta_true,
            delta_gamma_true,
        )
        for bouteille in positions_bouteilles
    ]

    print("测量角度:", Angles_réél_projecteur)

    # 运行优化
    result = fonction_finale4B(
        Angles_réél_projecteur, positions_bouteilles, position_theorique_projecteur
    )
    print("优化结果:", result[0])
