import numpy as np
from scipy.optimize import least_squares


# define the rotation matrix
def rotation_matrix(alpha, beta, gamma):
    """
    rotation axis x, y, z
    alpha: rotation angle around axis x (roll)
    beta: rotation angle around axis y (pitch)
    gamma: rotation angle around axis z (yaw)
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
    return Rz @ Ry @ Rx


# define the equations
def system_of_equations(
    x,
    positions_bouteilles,
    position_theorique_projecteur,
    Angles_réél_projecteur,
    rotation_matrix_theo,
):
    """
    x: variable of the stats [delta_x, delta_y, delta_z, delta_alpha, delta_beta, delta_gamma]
    positions_bouteilles: list of the positions of the "bouteilles" [[x_B1, y_B1, z_B1], ...]
    position_theorique_projecteur: theoretic positions of spotlight [x_t, y_t, z_t]
    Angles_réél_projecteur: actual mesured angles [[pan1, tilt1], ...]
    """
    delta_x, delta_y, delta_z, delta_alpha, delta_beta, delta_gamma = x
    x_t, y_t, z_t = position_theorique_projecteur

    # rotation matrix
    R = rotation_matrix(delta_alpha, delta_beta, delta_gamma)

    residuals = []
    for i, (x_B, y_B, z_B) in enumerate(positions_bouteilles):
        # calcul the position of the "bouteilles" in the spotlight's coordinates
        r_global = np.array(
            [x_B - x_t - delta_x, y_B - y_t - delta_y, z_B - z_t - delta_z]
        )
        # do the initialization of the rotation initial
        r_global = np.linalg.inv(rotation_matrix_theo) @ r_global
        r_local = np.linalg.inv(R) @ r_global  # turn to the local coordinates

        # calcul pan and tilt
        pan_measured, tilt_measured = Angles_réél_projecteur[i]
        pan_measured, tilt_measured = np.radians(pan_measured), np.radians(
            tilt_measured
        )

        # pan equation
        pan_calculated = np.arctan2(r_local[1], r_local[0])
        f_pan = np.tan(pan_measured) - np.tan(pan_calculated)

        # tilt equation
        tilt_calculated = np.arccos(r_local[2] / np.linalg.norm(r_local))
        f_tilt = np.cos(tilt_measured) - np.cos(tilt_calculated)

        residuals.extend([f_pan, f_tilt])

    return residuals


# main function
def fonction_finale(
    Angles_réél_projecteur,
    positions_bouteilles,
    position_theorique_projecteur,
    rotation_matrix_theo,
):
    """
    main function : calculate the errors of the theoretic angles and the calculated angles
    Angles_réél_projecteur: actual mesured angles [[pan1, tilt1], ...]
    positions_bouteilles: list of the positions of the "bouteilles"  [[x_B1, y_B1, z_B1], ...]
    position_theorique_projecteur: theoretic positions of spotlight [x_t, y_t, z_t]
    """
    # initial values(no error)
    x0 = np.array(
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    )  # [delta_x, delta_y, delta_z, delta_alpha, delta_beta, delta_gamma]
    # define bounds
    lower_bounds = [
        -1.0,
        -1.0,
        -1.0,
        -1.0,
        -1.0,
        -1.0,
    ]
    upper_bounds = [
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
    ]
    # optimisation with least square method

    res = least_squares(
        system_of_equations,
        x0,
        args=(
            positions_bouteilles,
            position_theorique_projecteur,
            Angles_réél_projecteur,
            rotation_matrix_theo,
        ),
        method="trf",  # Trust Region Reflective algorithm
        loss="soft_l1",  # soft_l1 lost function
        f_scale=0.2,  # scale of the lost function
        # bounds=(lower_bounds, upper_bounds),
        xtol=1e-8,
        ftol=1e-8,
        max_nfev=1000,
    )

    return res.x, res.cost, res.fun, res.message
