from intervals import Gamma
from coloring import color

bs = [24, 66, 108, 150, 192, 234, 276, 318, 360, 402, 444, 486, 528, 570, 612, 654, 696, 738, 780, 822, 864, 906, 948, 990, 1032, 1074, 1116, 1158, 1200, 1242, 1284, 1326, 1368, 1410, 1452, 1494, 1536, 1578, 1620, 1662, 1704, 1746, 1788, 1830, 1872, 1914, 1956, 1998, 2040, 2082]
user = [4, 6, 11, 12, 14, 15, 21, 23, 25, 27, 28, 29, 31, 32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 46, 47, 53, 54, 59, 60, 62, 71, 72, 78, 83, 84, 86, 87, 91, 92, 93, 97, 100, 102, 105, 106, 110, 111, 112, 115, 117, 120, 130, 132, 135, 136, 139, 140, 141, 144, 146, 147, 148, 149, 151, 152, 155, 156, 158, 159, 165, 166, 168, 170, 171, 174, 181, 182, 186, 187, 188, 190, 191, 194, 196, 197, 198, 199, 200, 203, 205, 207, 210, 211, 212, 215, 223, 225, 226, 227, 229, 232, 233, 236, 241, 245, 246, 247, 248, 251, 255, 256, 257, 260, 265, 267, 269, 271, 272, 273, 275, 279, 280, 283, 287, 288, 289, 291, 295, 296, 300, 301, 302, 310, 311, 313, 314, 315, 317, 319, 320, 325, 326, 329, 331, 333, 335, 339, 342, 343, 345, 346, 351, 354, 355, 356, 358, 365, 366, 369, 371, 372, 379, 381, 384, 385, 389, 393, 394, 395, 396, 397, 399, 400, 401, 405, 407, 410, 411, 413, 414, 416, 418, 420, 422, 424, 426, 435, 436, 437, 439, 445, 446, 449, 450, 452, 453, 455, 458, 459, 460, 461, 464, 466, 468, 470, 472, 474, 476, 477, 481, 483, 484, 485, 489, 490, 492, 494, 496, 498, 499, 500, 501, 502, 505, 507, 508, 509, 510, 511, 514, 516, 520, 521, 522, 523, 524, 525, 526, 527, 531, 536, 537, 538, 539, 542, 544, 547, 552, 553, 554, 557, 560, 561, 564, 565, 566, 569, 571, 572, 574, 576, 579, 580, 581, 583, 585, 587, 588, 591, 596, 597, 598, 599, 601, 602, 603, 605, 609, 613, 614, 616, 617, 618, 619, 620, 621, 625, 626, 628, 629, 631, 632, 633, 637, 638, 641, 642, 643, 645, 647, 648, 649, 651, 653, 655, 656, 657, 658, 659, 660, 664, 665, 667, 671, 674, 680, 681, 685, 689, 692, 693, 694, 695, 700, 704, 705, 706, 708, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 721, 722, 726, 728, 730, 733, 735, 737, 740, 742, 743, 744, 746, 747, 748, 750, 753, 755, 756, 757, 758, 759, 763, 764, 766, 770, 771, 774, 777, 778, 781, 782, 783, 784, 785, 786, 787, 790, 792, 793, 796, 797, 798, 800, 802, 804, 809, 812, 813, 814, 815, 816, 817, 818, 821, 825, 829, 830, 833, 834, 835, 836, 838, 840, 843, 847, 849, 850, 851, 852, 853, 854, 856, 857, 858, 860, 863, 865, 866, 869, 870, 871, 872, 875, 876, 878, 879, 880, 881, 885, 887, 891, 892, 894, 895, 896, 897, 899, 903, 907, 908, 910, 911, 912, 913, 915, 916, 920, 922, 923, 928, 933, 942, 943, 947, 950, 951, 952, 953, 954, 955, 957, 958, 960, 961, 964, 967, 969, 971, 973, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 988, 989, 993, 996, 998, 1000, 1002, 1006, 1008, 1009, 1010, 1011, 1012, 1014, 1015, 1017, 1019, 1020, 1022, 1023, 1024, 1025, 1026, 1029, 1030, 1031, 1033, 1035, 1036, 1042, 1045, 1046, 1048, 1053, 1055, 1056, 1057, 1059, 1060, 1062, 1065, 1067, 1069, 1070, 1071, 1072, 1073, 1075, 1076, 1077, 1080, 1081, 1082, 1083, 1084, 1086, 1087, 1091, 1093, 1094, 1096, 1097, 1100, 1103, 1108, 1109, 1111, 1112, 1113, 1118, 1119, 1121, 1125, 1126, 1127, 1128, 1130, 1132, 1133, 1134, 1137, 1139, 1144, 1145, 1147, 1151, 1154, 1157, 1162, 1164, 1165, 1166, 1167, 1168, 1169, 1173, 1175, 1177, 1182, 1183, 1184, 1186, 1188, 1191, 1193, 1196, 1202, 1203, 1205, 1208, 1210, 1213, 1214, 1217, 1219, 1223, 1224, 1225, 1226, 1227, 1228, 1230, 1233, 1235, 1237, 1238, 1243, 1244, 1245, 1246, 1249, 1250, 1252, 1255, 1256, 1258, 1260, 1261, 1264, 1266, 1268, 1276, 1281, 1283, 1285, 1286, 1287, 1292, 1293, 1296, 1300, 1301, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1311, 1313, 1316, 1318, 1320, 1321, 1324, 1325, 1328, 1329, 1330, 1334, 1338, 1340, 1343, 1344, 1345, 1346, 1347, 1349, 1353, 1357, 1361, 1362, 1363, 1364, 1373, 1375, 1376, 1379, 1385, 1388, 1389, 1390, 1394, 1397, 1400, 1405, 1406, 1407, 1408, 1411, 1415, 1416, 1419, 1420, 1422, 1423, 1424, 1426, 1427, 1437, 1441, 1443, 1447, 1448, 1450, 1451, 1460, 1461, 1463, 1466, 1471, 1473, 1475, 1476, 1477, 1479, 1481, 1482, 1483, 1484, 1490, 1492, 1493, 1496, 1498, 1500, 1507, 1511, 1512, 1514, 1517, 1518, 1521, 1526, 1527, 1531, 1533, 1535, 1537, 1541, 1543, 1544, 1545, 1546, 1550, 1553, 1554, 1556, 1557, 1560, 1561, 1562, 1563, 1564, 1565, 1567, 1568, 1569, 1576, 1577, 1580, 1581, 1582, 1584, 1587, 1589, 1592, 1594, 1595, 1596, 1597, 1598, 1601, 1602, 1604, 1606, 1610, 1611, 1613, 1614, 1617, 1618, 1619, 1621, 1622, 1624, 1625, 1628, 1630, 1632, 1634, 1635, 1636, 1637, 1640, 1641, 1642, 1644, 1645, 1648, 1651, 1652, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1665, 1666, 1668, 1671, 1673, 1676, 1678, 1682, 1683, 1684, 1687, 1690, 1692, 1697, 1699, 1701, 1702, 1705, 1707, 1708, 1710, 1711, 1715, 1718, 1720, 1723, 1724, 1725, 1726, 1734, 1736, 1737, 1738, 1739, 1740, 1742, 1749, 1751, 1754, 1755, 1757, 1758, 1759, 1761, 1765, 1767, 1771, 1772, 1773, 1778, 1781, 1783, 1785, 1786, 1790, 1791, 1792, 1796, 1797, 1798, 1801, 1803, 1805, 1808, 1809, 1810, 1811, 1813, 1814, 1816, 1817, 1818, 1820, 1823, 1825, 1826, 1827, 1829, 1831, 1835, 1838, 1841, 1842, 1843, 1845, 1846, 1847, 1849, 1854, 1856, 1857, 1859, 1861, 1862, 1866, 1867, 1874, 1876, 1878, 1879, 1880, 1881, 1883, 1886, 1889, 1896, 1901, 1904, 1905, 1907, 1908, 1911, 1915, 1916, 1917, 1919, 1923, 1924, 1926, 1928, 1929, 1932, 1935, 1939, 1941, 1948, 1949, 1952, 1954, 1959, 1960, 1961, 1963, 1965, 1968, 1970, 1972, 1976, 1980, 1989, 1990, 1991, 1992, 1993, 1994, 1999, 2000, 2001, 2004, 2006, 2007, 2010, 2013, 2014, 2016, 2028, 2029, 2031, 2033, 2034, 2035, 2038, 2039, 2041, 2042, 2047, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2058, 2059, 2061, 2062, 2067, 2068, 2070, 2074, 2076, 2077, 2078, 2089, 2090, 2091, 2092, 2093, 2096, 2097, 2102, 2104, 2106, 2107, 2109, 2114, 2115, 2116, 2117]

intervals = Gamma(user, bs)
n = len(user)
m = len(bs)

def u(i):
    return user[i - 1]

def b(i):
    return bs[i - 1]

def G(i):
    return intervals[i]

def arrow(bsp, usp):
    head = usp
    tail = 2 * bsp - usp
    return (tail, head)

# Theoretical check done - working correctly
def C(i, x, y, z):
    arrows = [arrow(b(i), u(j)) for j in range(x+1, y+1)]
    arrows.extend([arrow(b(i+1), u(j)) for j in range(y+1, z+1)])
    return color(arrows)

M = {}
D = {}
def X(a, b, c):
    ans = None
    if a == 1 and b == 0:
        ans = c
    elif a == 1 and b != 0:
        print("Error!")
        import sys
        sys.exit(0)
    elif (a, b, c) in M:
        ans = M[a, b, c]
    else:
        # M[a, b, c] = min([max(X(a-1, x, b), C(a-1, x, b, c)) for x in G(a-2)])

        minx = 10000
        minVal = 10000
        for x in G(a-2):
            X_val = X(a-1, x, b)
            cols = C(a-1, x, b, c)
            if max(X_val, cols) < minVal:
                minVal = max(X_val, cols)
                minx = x
        D[a-2] = minx
        M[a, b, c] = minVal

        ans = M[a, b, c]

    # print("a", a, "b", b, "c", c, "X", ans)
    return ans

def solve():
    # ans = min([X(m, x, n) for x in G(m-1)])

    minx = 10000
    minX = 10000
    for x in G(m-1):
        X_val = X(m, x, n)
        if X_val < minX:
            # do something
            minX = X_val
            minx = x
    D[m-1] = minx

    ans = minX
    print("colors: " + str(ans))
    print("DPs: " + str(D))
    for i in range(1, m):
        print("BS at posn", b(i), "serves users at", [u(i) for i in range(D[i-1]+1, D[i]+1)])
    print("BS at posn", b(m), "serves users at", [u(i) for i in range(D[m-1]+1, n+1)])

if __name__ == '__main__':
    # print(C(1, 0, 1, 4))
    solve()
