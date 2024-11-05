import numpy as np
def rotation_matrix(axis, theta):
    """
    calculate the rotation matrix by the axis given
    :param axis: rotation axis
    :param theta: rotation angle
    :return: rotation matrix
    """
    # normalize
    axis = axis / np.linalg.norm(axis)
    u_x, u_y, u_z = axis

    # rotation matrix
    R = np.array([
        [np.cos(theta) + u_x**2 * (1 - np.cos(theta)), u_x * u_y * (1 - np.cos(theta)) - u_z * np.sin(theta), u_x * u_z * (1 - np.cos(theta)) + u_y * np.sin(theta)],
        [u_y * u_x * (1 - np.cos(theta)) + u_z * np.sin(theta), np.cos(theta) + u_y**2 * (1 - np.cos(theta)), u_y * u_z * (1 - np.cos(theta)) - u_x * np.sin(theta)],
        [u_z * u_x * (1 - np.cos(theta)) - u_y * np.sin(theta), u_z * u_y * (1 - np.cos(theta)) + u_x * np.sin(theta), np.cos(theta) + u_z**2 * (1 - np.cos(theta))]
    ])

    return R

# input : alpha : l'angle décalé selon axe Z
#         beta  : l'angle décalé selon axe Y'(nouvelle Y après le changement selon Z)
#         pan   : l'angle preset
#         tilt  : l'angle preset
#output : [deta_pan,deta_tilt]
def change_angle(alpha,beta,pan,tilt):
    # alpha = np.pi/4
    # beta = np.pi/4
    Rz = np.array([[np.cos(alpha),-np.sin(alpha),0],[np.sin(alpha),np.cos(alpha),0],[0,0,1]])
    Ry_ = np.array([[np.cos(beta),0,np.sin(beta)],[0,1,0],[-np.sin(beta),0,np.cos(beta)]])

    len_xy = np.cos(np.radians(tilt))
    x_origin = np.array([len_xy*np.cos(np.radians(pan)),len_xy*np.sin(np.radians(pan)),-np.sin(np.radians(tilt))])

    x_change = np.linalg.inv(Rz @ Ry_) @ x_origin

    #print(x_origin)

    #print(x_change)

    P1 = x_origin  # ordonnee de point 1
    P2 = x_change  # ordonnee de point 2

    # normaliser deux veteurs
    v1 = P1 / np.linalg.norm(P1)
    v2 = P2 / np.linalg.norm(P2)

    alpha1 = np.arctan2(v1[1],v1[0])
    #print('alpha1d: ',np.degrees(alpha1))
    #print('alpha1: ',alpha1)
    alpha2 = np.arctan2(v2[1],v2[0])
    #print('alpha2d: ',np.degrees(alpha2))
    #print('alpha2: ',alpha2)
    alpha = alpha2-alpha1
    #print('alpha-angle: ',np.degrees(alpha))

    beta1 = np.arctan2(v1[2],np.linalg.norm([v1[0],v1[1]]))
    #print('beta1d: ',np.degrees(beta1))
    beta2 = np.arctan2(v2[2],np.linalg.norm([v2[0],v2[1]]))
    #print('beta2d: ',np.degrees(beta2))
    beta = beta1-beta2
    #print('beta-angle: ',np.degrees(beta))

    #print('alpha: ',alpha)
    #print('beta: ',beta)

    Rz = np.array([[np.cos(alpha),-np.sin(alpha),0],[np.sin(alpha),np.cos(alpha),0],[0,0,1]])
    #print("Rz*v1: ",Rz @ v1)

    Ry_ = rotation_matrix(np.array([[np.cos(alpha2),-np.sin(alpha2),0],[np.sin(alpha2),np.cos(alpha2),0],[0,0,1]])@[0,1,0],beta)

    #print('v1: ',v1)
    #print('v2: ',v2)
    v_change_f = Ry_ @ Rz @ v1

    #print('v_change: ',v_change_f)
    return [np.degrees(alpha),np.degrees(beta)]

if __name__ == "__main__":
    change_angle(np.pi/4,np.pi/4)