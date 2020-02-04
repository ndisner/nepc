"""Constants for use in nepc"""
import numpy as np
from scipy.constants import Avogadro as AVOGADRO

N2_DIATOMIC_CONSTANTS = {
        'N2(X1Sigmag+)': {'To': np.float64(0.0),
            'we': np.float64(2358.57),
            'wexe': np.float64(14.324),
            'Be': np.float64(1.99824),
            're': np.float64(1.097688),
            'De': np.float64(79890.0)},
        'N2(A3Sigmau+)': {'To': np.float64(49754.8),
            'we': np.float64(1460.48),
            'wexe': np.float64(13.775),
            'Be': np.float64(1.45499),
            're': np.float64(1.286390),
            'De': np.float64(29686.0)},
        'N2(B3Pig)': {'To': np.float64(59306.8),
            'we': np.float64(1734.38),
            'wexe': np.float64(14.558),
            'Be': np.float64(1.63802),
            're': np.float64(1.212392),
            'De': np.float64(39495.0)},
        'N2(W3Deltau)': {'To': np.float64(59380.2),
            'we': np.float64(1506.53),
            'wexe': np.float64(12.575),
            'Be': np.float64(1.47021),
            're': np.float64(1.279714),
            'De': np.float64(39308.0)},
        'N2(Bp3Sigmau-)': {'To': np.float64(65851.3),
            'we': np.float64(1516.88),
            'wexe': np.float64(12.181),
            'Be': np.float64(1.4731),
            're': np.float64(1.278458),
            'De': np.float64(42457.0)},
        'N2(ap1Sigmau-)': {'To': np.float64(67739.3),
            'we': np.float64(1530.25),
            'wexe': np.float64(12.075),
            'Be': np.float64(1.4799),
            're': np.float64(1.275518),
            'De': np.float64(50186.0)},
        'N2(a1Pig)': {'To': np.float64(68951.2),
            'we': np.float64(1694.21),
            'wexe': np.float64(13.949),
            'Be': np.float64(1.61690),
            're': np.float64(1.220285),
            'De': np.float64(49055.0)},
        'N2(w1Deltau)': {'To': np.float64(71698.4),
            'we': np.float64(1559.50),
            'wexe': np.float64(12.008),
            'Be': np.float64(1.4963),
            're': np.float64(1.268509),
            'De': np.float64(46241.0)},
        'N2(C3Piu)': {'To': np.float64(88977.9),
            'we': np.float64(2047.18),
            'wexe': np.float64(28.445),
            'Be': np.float64(1.8247),
            're': np.float64(1.148701),
            'De': np.float64(78889.0)},
        'N2+(X2Sigmag+)':{'To': np.float64(125667.5),
            'we': np.float64(2207.37),
            'wexe': np.float64(16.302),
            'Be': np.float64(1.93176),
            're': np.float64(1.116413),
            'De': np.float64(71373.0)},
        'N2+(A2Piu)':{'To': np.float64(134683.1),
            'we': np.float(1903.51),
            'wexe': np.float(15.029),
            'Be': np.float64(1.7442),
            're': np.float64(1.174910),
            'De': np.float64(62206.0)},
        'N2+(B2Sigmau+)':{'To': np.float64(151233.5),
            'we': np.float64(2420.83),
            'wexe': np.float64(23.851),
            'Be': np.float64(2.0845),
            're': np.float64(1.074736),
            'De': np.float64(45912.0)},
        'N2+(C2Sigmau+)':{'To': np.float64(190209.5),
            'we': np.float64(2071.5),
            'wexe': np.float64(9.29),
            'Be': np.float64(1.51140),
            're': np.float64(1.262156),
            'De': np.float64(53549.0)}
        }

"""Number of identical electrons possible for excitation"""
N2_VALENCE = {'N2(X1Sigmag+)': {'N2+(X2Sigmag+)': 2, 'N2+(A2Piu)': 4, 'N2+(B2Sigmau+)': 2, 'N2+(C2Sigmau+)': 0},
             'N2(A3Sigmau+)': {'N2+(X2Sigmag+)': 0, 'N2+(A2Piu)': 1, 'N2+(B2Sigmau+)': 0, 'N2+(C2Sigmau+)': 2},
             'N2(B3Pig)': {'N2+(X2Sigmag+)': 1, 'N2+(A2Piu)': 0, 'N2+(B2Sigmau+)': 0, 'N2+(C2Sigmau+)': 4},
             'N2(W3Deltau)': {'N2+(X2Sigmag+)': 0, 'N2+(A2Piu)': 1, 'N2+(B2Sigmau+)': 0, 'N2+(C2Sigmau+)': 2},
             'N2(Bp3Sigmau-)': {'N2+(X2Sigmag+)': 0, 'N2+(A2Piu)': 1, 'N2+(B2Sigmau+)': 0, 'N2+(C2Sigmau+)': 2},
             'N2(ap1Sigmau-)': {'N2+(X2Sigmag+)': 0, 'N2+(A2Piu)': 1, 'N2+(B2Sigmau+)': 0, 'N2+(C2Sigmau+)': 2},
             'N2(a1Pig)': {'N2+(X2Sigmag+)': 1, 'N2+(A2Piu)': 0, 'N2+(B2Sigmau+)': 0, 'N2+(C2Sigmau+)': 4},
             'N2(w1Deltau)': {'N2+(X2Sigmag+)': 0, 'N2+(A2Piu)': 1, 'N2+(B2Sigmau+)': 0, 'N2+(C2Sigmau+)': 2},
             'N2(C3Piu)': {'N2+(X2Sigmag+)': 0, 'N2+(A2Piu)': 0, 'N2+(B2Sigmau+)': 1, 'N2+(C2Sigmau+)': 0}}

"""reduced mass of nitrogen"""
MU_NITROGEN_KG = 1.16294E-26 # kg

"""ionization potential for nitrogen: NIST eval."""
J_IONIZATION_N2 = 15.581 # eV

"""coulomb force constant: calculated from 1/(4*pi*epsilon_naught)"""
K_E = 8987551787 # N*m^2/C^2

"""conversion value for eV to wavenumber"""
WAVENUMBER_PER_EV = 8065.6 #cm^-1/eV

# from Laher & Gilmore (1991)
states_N2 = ["N2(X1Sigmag+)",
        "N2(A3Sigmau+)",
        "N2(B3Pig)",
        "N2(W3Deltau)",
        "N2(Bp3Sigmau-)",
        "N2(ap1Sigmau-)",
        "N2(a1Pig)",
        "N2(w1Deltau)",
        "N2(C3Piu)",
        "N2(E3Sigmag+)",
        "N2(D3Sigmau+)"]

states_N2p = ["N2+(X2Sigmag+)",
        "N2+(A2Piu)",
        "N2+(B2Sigmau+)",
        "N2+(C2Sigmau+)"]


vib_constants_N2 = [[0.0, 2358.57, 14.324, -2.26E-3, -2.4E-4, 0],
        [49754.8, 1460.48, 13.775, -1.175E-2, 1.41E-4, -7.29E-5],
        [59306.8, 1734.38, 14.558, 1.40E-2, -1.13E-3, 0],
        [59380.2, 1506.53, 12.575, 3.09E-2, -7.1E-4, 0],
        [65851.3, 1516.88, 12.181, 4.19E-2, -7.3E-4, 0],
        [67739.3, 1530.25, 12.075, 4.13E-2, -2.9E-4, 0],
        [68951.2, 1694.21, 13.949, 7.94E-3, 2.9E-4, 0],
        [71698.4, 1559.50, 12.008, 4.54E-2, 0, 0],
        [88977.9, 2047.18, 28.445, 2.0883, -5.350E-1, 0],
        [95774.5, 2218, 16.3, -2.7E-2, -2.6E-3, 0],
        [103570.9, 2207, 16.3, -2.7E-2, -2.6E-3, 0]]

vib_constants_N2p = [[125667.5, 2207.37, 16.302, -2.67E-3, -2.61E-3, 3.7E-5],
        [134683.1, 1903.51, 15.029, 2.03E-3, 0, 0],
        [151233.5, 2420.83, 23.851, -0.3587, -6.192E-2, 0],
        [190209.5, 2071.5, 9.29, -0.43, 0, 0]]

vib_constants_N2_dict = {"N2(X1Sigmag+)": [0.0, 2358.57, 14.324, -2.26E-3, -2.4E-4, 0],
        "N2(A3Sigmau+)": [49754.8, 1460.48, 13.775, -1.175E-2, 1.41E-4, -7.29E-5],
        "N2(B3Pig)": [59306.8, 1734.38, 14.558, 1.40E-2, -1.13E-3, 0],
        "N2(W3Deltau)": [59380.2, 1506.53, 12.575, 3.09E-2, -7.1E-4, 0],
        "N2(Bp3Sigmau-)": [65851.3, 1516.88, 12.181, 4.19E-2, -7.3E-4, 0],
        "N2(ap1Sigmau-)": [67739.3, 1530.25, 12.075, 4.13E-2, -2.9E-4, 0],
        "N2(a1Pig)": [68951.2, 1694.21, 13.949, 7.94E-3, 2.9E-4, 0],
        "N2(w1Deltau)": [71698.4, 1559.50, 12.008, 4.54E-2, 0, 0],
        "N2(C3Piu)": [88977.9, 2047.18, 28.445, 2.0883, -5.350E-1, 0],
        "N2(E3Sigmag+)": [95774.5, 2218, 16.3, -2.7E-2, -2.6E-3, 0],
        "N2(D3Sigmau+)": [103570.9, 2207, 16.3, -2.7E-2, -2.6E-3, 0]}

vib_constants_N2p_dict = {"N2+(X2Sigmag+)": [125667.5, 2207.37, 16.302, -2.67E-3, -2.61E-3, 3.7E-5],
        "N2+(A2Piu)": [134683.1, 1903.51, 15.029, 2.03E-3, 0, 0],
        "N2+(B2Sigmau+)": [151233.5, 2420.83, 23.851, -0.3587, -6.192E-2, 0],
        "N2+(C2Sigmau+)": [190209.5, 2071.5, 9.29, -0.43, 0, 0]}

rot_constants_N2 = [[1.99824, 1.7318E-2, -3.3E-5, 0, 0],
        [1.45499, 1.8385E-2, 1.24E-5, -6.7E-6, 0],
        [1.63802, 1.8302E-2, -8.4E-6, -3.4E-6, 0],
        [1.47021, 1.6997E-2, -1.01E-5, 3.3E-7, 0],
        [1.4731, 1.668E-2, 1.84E-5, -4.5E-7, 0],
        [1.4799, 1.657E-2, 2.41E-5, 0, 0],
        [1.6169, 1.793E-2, -2.93E-5, 0, 0],
        [1.4963, 1.63E-2, 0, 0, 0],
        [1.8247, 1.868E-2, -2.28E-3, 7.33E-4, -1.5E-4],
        [1.9368, 1.90E-2, -1.9E-4, 0, 0],
        [1.9705, 1.90E-2, -1.9E-4, 0, 0]]

rot_constants_N2p = [[1.93177, 1.900E-2, -1.91E-5, -5.00E-6, 4.6E-8],
        [1.7442, 1.838E-2, -1.76E-4, 4.4E-6, 0],
        [2.0845, 2.132E-2, -8.5E-4, 0, 0],
        [1.5114, 1.10E-3, -8.2E-4, 0, 0]]

rot_constants_N2_dict = {"N2(X1Sigmag+)": [1.99824, 1.7318E-2, -3.3E-5, 0, 0],
        "N2(A3Sigmau+)": [1.45499, 1.8385E-2, 1.24E-5, -6.7E-6, 0],
        "N2(B3Pig)": [1.63802, 1.8302E-2, -8.4E-6, -3.4E-6, 0],
        "N2(W3Deltau)": [1.47021, 1.6997E-2, -1.01E-5, 3.3E-7, 0],
        "N2(Bp3Sigmau-)": [1.4731, 1.668E-2, 1.84E-5, -4.5E-7, 0],
        "N2(ap1Sigmau-)": [1.4799, 1.657E-2, 2.41E-5, 0, 0],
        "N2(a1Pig)": [1.6169, 1.793E-2, -2.93E-5, 0, 0],
        "N2(w1Deltau)": [1.4963, 1.63E-2, 0, 0, 0],
        "N2(C3Piu)": [1.8247, 1.868E-2, -2.28E-3, 7.33E-4, -1.5E-4],
        "N2(E3Sigmag+)": [1.9368, 1.90E-2, -1.9E-4, 0, 0],
        "N2(D3Sigmau+)": [1.9705, 1.90E-2, -1.9E-4, 0, 0]}

rot_constants_N2p_dict = {"N2+(X2Sigmag+)": [1.93177, 1.900E-2, -1.91E-5, -5.00E-6, 4.6E-8],
        "N2+(A2Piu)": [1.7442, 1.838E-2, -1.76E-4, 4.4E-6, 0],
        "N2+(B2Sigmau+)": [2.0845, 2.132E-2, -8.5E-4, 0, 0],
        "N2+(C2Sigmau+)": [1.5114, 1.10E-3, -8.2E-4, 0, 0]}


"""reduced mass of oxygen"""
MU_OXYGEN = 7.9995 # amu
MU_OXYGEN_KG = 1.32838E-26 # kg

states_O2 = ["O2(X3Sigmag-)"]
states_O2p = ["O2+(X2Pig)", "O2+(a4Piu)", "O2+(A2Piu)", "O2+(b4Sigmag-)"]

vib_constants_O2 = [[0.0, 1580.39, 12.112, 7.54E-2, -4.09E-3, 1.30E-4]]

vib_constants_O2p = [[97365.0, 1906.07, 16.512, 2.11E-2, -7.1E-4, 0],
        [129889.3, 1035.13, 10.115, -3.31E-2, 2.1E-4, 0],
        [137433.1, 899.0, 13.726, 1.0E-2, 0, 0],
        [146556.0, 1197.02, 17.172, 1.18E-2, -1.0E-3, 0]]

vib_constants_O2_dict = {"O2(X3Sigmag-)": [0.0, 1580.39, 12.112, 7.54E-2, -4.09E-3, 1.30E-4]}

vib_constants_O2p_dict = {"O2+(X2Pig)": [97365.0, 1906.07, 16.512, 2.11E-2, -7.1E-4, 0],
        "O2+(a4Piu)": [129889.3, 1035.13, 10.115, -3.31E-2, 2.1E-4, 0],
        "O2+(A2Piu)": [137433.1, 899.0, 13.726, 1.0E-2, 0, 0],
        "O2+(b4Sigmag-)": [146556.0, 1197.02, 17.172, 1.18E-2, -1.0E-3, 0]}

rot_constants_O2 = [[1.4451, 1.523E-2, 8.25E-5, 7.25E-6, -2.09E-7]]

rot_constants_O2p = [[1.6896, 1.930E-2, -1.9E-5, -1.6E-6, 0],
        [1.10476, 1.548E-2, 1.2E-5, -5.0E-6, 0],
        [1.0617, 1.941E-2, -1.27E-4, 0, 0],
        [1.28766, 2.192E-2, -1.28E-4, 0, 0]]

rot_constants_O2_dict = {"O2(X3Sigmag-)": [1.4451, 1.523E-2, 8.25E-5, 7.25E-6, -2.09E-7]}

rot_constants_O2p_dict = {"O2+(X2Pig)": [1.6896, 1.930E-2, -1.9E-5, -1.6E-6, 0],
        "O2+(a4Piu)": [1.10476, 1.548E-2, 1.2E-5, -5.0E-6, 0],
        "O2+(A2Piu)": [1.0617, 1.941E-2, -1.27E-4, 0, 0],
        "O2+(b4Sigmag-)": [1.28766, 2.192E-2, -1.28E-4, 0, 0]}
