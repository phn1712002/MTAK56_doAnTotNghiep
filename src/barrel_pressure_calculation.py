from solve_ivp import rk4_1step

class BattleCannon:

    def __init__(self):
        self.t_value = None
        self.p_value = None
        self.v_value = None
        self.l_value = None
        self.psi_value = None
        self.z_value = None
    
    # def load_from_json(self, path_file_json):
    #     parameter = read_json_to_dict(path_file_json)
    #     self.set_value(**parameter)

    # def create_json(self, path_file_json):
    #     parameter = {
    #         "p_0": 0,
    #         "psi_0": 0,  
    #         "f": 0,  
    #         "chi": 0, 
    #         "lamda": 0,              
    #         "mu": 0,  
    #         "theta": 0,  
    #         "Ik": 0,  
    #         "delta": 0,  
    #         "alpha": 0,  
    #         "q": 0,  
    #         "w": 0,  
    #         "S": 0,  
    #         "l_barrel": 0,  
    #         "W_0": 0,  
    #         "phi": 0,  
    #         "g": 0,  
    #     }
    #     create_sample_json(path_file_json, parameter)
    
    def set_value(self, p_0, psi_0, f, chi, lamda, mu, theta, Ik, delta, alpha, q, w, S, l_barrel, W_0, phi, g):
        self.p_0 = p_0
        self.psi_0 = psi_0
        self.f = f
        self.chi = chi
        self.lamda = lamda
        self.mu = mu
        self.theta = theta
        self.Ik = Ik
        self.delta = delta
        self.alpha = alpha
        self.q = q
        self.w = w
        self.S = S
        self.l_barrel = l_barrel
        self.W_0 = W_0
        self.phi = phi
        self.g = g

    def dz_dt(self, s1, p, Ik):
        return s1*(p/Ik)

    def dpsi_dt(self, s1, chi, lamda, mu, z, value_dz_dt):
        return s1*chi*(1+2*lamda*z+3*mu*z*z)*value_dz_dt

    def dv_dt(self, s2, S, p, g, phi, q):
        return s2*((S*p*g)/(phi*q))

    def dl_dt(self, v):
        return v

    def calc_p(self, f, w, psi, theta, g, phi, q, v, W_0, delta, alpha, S, l):
        return (f*w*psi - (theta/(2*g))*phi*q*v*v)/(W_0-(1-psi)*(w/delta)-alpha*w*psi+S*l)

    def get_local_m(self, t_value, l_value, p_value, v_value, psi_value, z_value):
        max_p = max(p_value)
        index_max_p = p_value.index(max_p)

        return (t_value[index_max_p], l_value[index_max_p], p_value[index_max_p], v_value[index_max_p], psi_value[index_max_p], z_value[index_max_p])
    
    def get_local_k(self, t_value, l_value, p_value, v_value, psi_value, z_value):
        max_z = max(z_value)
        index_max_z = min(p_value.index(max_z))

        return (t_value[index_max_z], l_value[index_max_z], p_value[index_max_z], v_value[index_max_z], psi_value[index_max_z], z_value[index_max_z])
    
    def calculation(self, h_step):
        # Tham số súng pháo
        p_0 = self.p_0
        psi_0 = psi_0
        f = self.f
        chi = self.chi
        lamda = self.lamda
        mu = self.mu
        theta = self.theta
        Ik = self.Ik
        delta = self.delta
        alpha = self.alpha
        q = self.q
        w = self.w
        S = self.S
        l_barrel = self.l_barrel
        W_0 = self.W_0
        phi = self.phi
        g = self.g
        
        # Tham số điều khiển
        s1 = 0
        s2 = 0

        # Giá trị khởi đầu
        h = 0
        t = 0
        psi = psi_0
        p = p_0
        z = 0
        v = 0
        l = 0

        # Lưu trữ giá trị của 
        self.t_value = [t]
        self.p_value = [p]
        self.v_value = [v]
        self.l_value = [l]
        self.psi_value = [psi]
        self.z_value = [z]
        
        # Tính toán đường cong thuật phóng
        while (l >= l_barrel):

            if (z >= 1): # Thời kì thứ nhất
                z = 1
                s1 = 1
                s2 = 0
            else: # Thời kì thứ hai
                s1 = 0
                s2 = 1

            # Tính toán các giá trị mới
            h = h + h_step
            t = h

            # Tính z
            lambda_dz_dt = lambda _, p_current : self.dz_dt(s1, p_current, Ik)
            z = rk4_1step(lambda_dz_dt, 0, p, h)

            # Tính psi
            value_dz_dt = self.dz_dt(s1, p, Ik)
            lambda_dpsi_dt = lambda _, z_current : self.dpsi_dt(s1, chi, lamda, mu, z_current, value_dz_dt)
            psi = rk4_1step(lambda_dpsi_dt, 0, z, h)

            # Tính lamda
            lambda_dv_dt = lambda _, p_current : self.dv_dt(s2, S, p_current, g, phi, q)
            v = rk4_1step(lambda_dv_dt, 0, p, h)

            # Tính l
            lambda_dl_dt = lambda _, v_current : self.dl_dt(v_current)
            l = rk4_1step(lambda_dl_dt, 0, v, h)

            # Tính p
            p = self.calc_p(f, w, psi, theta, g, phi, q, v, W_0, delta, alpha, S, l)

            # Lưu các giá trị
            self.p_value.append(p)
            self.t_value.append(t)
            self.v_value.append(v)
            self.l_value.append(l)
            self.psi_value.append(psi)
            self.z_value.append(z)
            
            return self.t_value, self.l_value, self.p_value, self.v_value, self.psi_value, self.z_value