#1. gerar o vetor aleatorio
#2. guardar uma copia

def seleção(v):
  resp = []
  while v:
    m = min(v)
    resp.append(m)
    v.remove(m)
  return resp
print (seleção([653, 119, 973, 429, 436, 983, 1864, 1780, 555, 1364, 620, 1746, 1649, 1007, 1767, 489, 1028, 861, 621, 202, 1049, 785, 627, 733, 943, 1044, 513, 761, 932, 124, 1887, 219, 1134, 647, 1419, 402, 1816, 1115, 179, 1491, 833, 917, 292, 371, 463, 552, 614, 1294, 561, 1830, 1490, 987, 731, 871, 214, 1687, 1405, 200, 173, 1246, 660, 544, 1848, 769, 1063, 1439, 1229, 1434, 1813, 1743, 228, 722, 1740, 109, 397, 1048, 1538, 862, 719, 1806, 316, 1509, 83, 1025, 26, 563, 1055, 1962, 760, 1284, 187, 1047, 901, 582, 1702, 106, 95, 1685, 1986, 1752, 1992, 387, 1160, 343, 386, 1893, 669, 1098, 517, 966, 14, 846, 1334, 1219, 1306, 515, 764, 1857, 1839, 98, 829, 1445, 216, 468, 969, 1721, 1937, 953, 54, 1889, 1761, 1908, 276, 108, 723, 1789, 1835, 617, 1844, 503, 22, 175, 853, 1286, 1486, 1975, 1035, 824, 1914, 1154, 260, 148, 838, 232, 1974, 1390, 1395, 1972, 142, 1512, 1958, 594, 100, 954, 1855, 1586, 1332, 1373, 483, 4, 1127, 771, 596, 1800, 1359, 299, 1228, 147, 1187, 1298, 357, 1758, 1227, 1101, 289, 883, 1561, 293, 313, 1680, 1124, 1473, 1075, 1613, 36, 1956, 1401, 1014, 1065, 934, 1995, 1588, 1383, 1764, 1015, 597, 325, 1537, 1462, 1287, 919, 251, 73, 1837, 496, 1671, 1933, 900, 1136, 6, 445, 803, 428, 1636, 1854, 1525, 1372, 1261, 1891, 893, 1808, 1245, 725, 1161, 1731, 27, 1102, 1156, 1400, 721, 454, 709, 1530, 904, 425, 1832, 835, 782, 1528, 1703, 1335, 1355, 1904, 799, 221, 1590, 1959, 1254, 888, 1863, 550, 474, 1531, 924, 1283, 17, 637, 1091, 1967, 795, 351, 577, 1776, 307, 662, 266, 1019, 243, 1510, 1542, 615, 298, 1577, 604, 890, 1069, 913, 1384, 69, 1214, 1905, 1032, 146, 982, 702, 1952, 67, 1683, 1539, 1890, 1480, 818, 107, 1083, 993, 1763, 399, 285, 1300, 1640, 1250, 1669, 845, 19, 1766, 1167, 1879, 457, 546, 1238, 1993, 751, 265, 1323, 828, 635, 1920, 438, 626, 1342, 1635, 1791, 557, 1701, 249, 1496, 950, 1987, 989, 988, 1354, 1621, 1182, 1010, 1950, 1452, 284, 1899, 1040, 1843, 1031, 1798, 729, 412, 1062, 1448, 522, 850, 203, 991, 1906, 376, 1809, 916, 1078, 444, 1714, 190, 1996, 1546, 1875, 1924, 1536, 297, 1426, 612, 1492, 952, 1750, 1605, 321, 1141, 1818, 1197, 1946, 1722, 1684, 1812, 1980, 1282, 1805, 352, 933, 465, 122, 874, 770, 493, 248, 318, 931, 1916, 999, 628, 43, 1070, 127, 1625, 551, 937, 1256, 458, 1624, 1432, 524, 245, 863, 273, 1180, 1943, 74, 207, 1871, 1628, 533, 11, 1381, 1162, 1748, 1527, 304, 24, 126, 1200, 892, 755, 60, 281, 695, 712, 1500, 717, 1697, 1688, 1460, 1626, 1608, 1782, 529, 1913, 1544, 1954, 980, 941, 519, 1478, 1243, 1689, 1922, 1670, 506, 421, 1775, 990, 1202, 589, 1311, 1604, 308, 1437, 1505, 706, 1965, 1568, 160, 1847, 1052, 32, 218, 683, 1146, 413, 1398, 306, 156, 1173, 603, 1345, 1465, 757, 213, 704, 759, 1295, 1185, 40, 1792, 1698, 1915, 12, 491, 752, 854, 1289, 112, 1988, 758, 81, 416, 135, 47, 92, 997, 1903, 327, 1213, 1425, 1216, 1600, 964, 1352, 1869, 586, 1118, 1567, 1596, 167, 435, 1783, 784, 486, 390, 1273, 1280, 1205, 1211, 1076, 447, 1315, 856, 977, 1239, 1941, 41, 75, 881, 1316, 516, 370, 1960, 1866, 870, 1990, 1963, 300, 1244, 353, 372, 1729, 1508, 58, 482, 1945, 1711, 1616, 656, 155, 1519, 578, 1087, 237, 256, 388, 545, 86, 1534, 1234, 1255, 72, 624, 1918, 1222, 1321, 312, 979, 1598, 481, 267, 1073, 676, 480, 963, 689, 1771, 1304, 1386, 663, 1634, 1260, 280, 1690, 896, 355, 1926, 640, 42, 1991, 585, 1247, 691, 254, 1081, 1328, 63, 471, 1139, 1797, 71, 1271, 638, 1885, 94, 1094, 1420, 823, 334, 271, 1569, 736, 962, 230, 1178, 505, 1633, 226, 433, 895, 580, 422, 710, 1375, 192, 1935, 1566, 700, 664, 820, 1240, 1573, 1925, 426, 1005, 339, 633, 1446, 837, 497, 680, 111, 1732, 182, 844, 78, 796, 884, 1801, 1957, 302, 797, 749, 235, 341, 151, 1189, 866, 180, 381, 1451, 1562, 283, 382, 65, 894, 956, 1266, 1674, 1034, 1263, 1449, 1882, 1936, 450, 1119, 140, 295, 1393, 601, 538, 494, 843, 1485, 632, 1607, 1706, 819, 1513, 1108, 1012, 259, 1867, 521, 1454, 1, 739, 798, 955, 1171, 1655, 358, 1646, 1609, 1464, 1175, 745, 13, 542, 3, 1461, 808, 678, 247, 157, 1944, 1724, 1148, 346, 1720, 1363, 686, 1026, 1318, 1111, 184, 1560, 1402, 1495, 1207, 1317, 502, 1231, 791, 263, 1221, 378, 150, 650, 687, 1132, 1479, 677, 1529, 1194, 383, 1796, 1290, 1939, 1371, 1468, 49, 419, 1204, 1650, 1549, 1152, 711, 880, 51, 1251, 1747, 976, 1225, 1705, 921, 1658, 1343, 1274, 965, 564, 1966, 1872, 1874, 1181, 734, 1053, 623, 479, 666, 554, 571, 509, 1054, 434, 87, 1601, 1066, 1117, 744, 1347, 1215, 737, 1281, 1029, 1828, 504, 1592, 792, 1272, 625, 804, 282, 149, 79, 556, 144, 1516, 224, 1900, 1368, 1046, 61, 467, 62, 776, 1097, 1074, 864, 958, 608, 1817, 333, 1253, 34, 852, 10, 1557, 317, 1526, 154, 1397, 909, 1692, 1517, 466, 1896, 1503, 1672, 446, 1374, 1275, 1267, 748, 1440, 891, 970, 659, 1533, 806, 1953, 1862, 1973, 1686, 1772, 940, 392, 1968, 1378, 1765, 753, 959, 1998, 1336, 1351, 668, 877, 1024, 2, 141, 631, 1760, 424, 929, 1145, 696, 768, 1000, 1909, 1522, 1322, 1982, 1540, 1619, 1929, 1120, 1350, 384, 1749, 133, 1482, 9, 1859, 1845, 451, 540, 1971, 847, 469, 113, 648, 1707, 817, 1594, 1417, 1218, 1654, 1907, 822, 1033, 406, 1071, 512, 442, 777, 1970, 787, 1339, 1571, 520, 1113, 1142, 1129, 1288, 671, 1541, 1741, 584, 319, 1781, 1514, 762, 1810, 728, 250, 340, 1376, 363, 110, 651, 1470, 922, 1677, 673, 153, 860, 1143, 85, 30, 579, 1768, 1059, 241, 1297, 35, 1814, 1394, 197, 215, 46, 1807, 169, 172, 1602, 763, 675, 1438, 1825, 773, 174, 1411, 1307, 1778, 826, 1582, 487, 642, 1662, 1084, 1293, 1068, 1656, 629, 1565, 946, 1704, 349, 1564, 718, 395, 1036, 878, 159, 1637, 128, 223, 1691, 778, 573, 1794, 701, 523, 805, 1123, 1366, 1276, 1994, 1212, 1681, 576, 1020, 971, 1421, 510, 287, 1523, 1418, 255, 1130, 1831, 1663, 619, 1017, 201, 420, 1450, 1630, 1581, 1191, 1700, 1103, 1133, 821, 101, 766, 472, 244, 1976, 211, 1615, 44, 570, 841, 657, 164, 592, 1365, 1037, 217, 944, 77, 1803, 68, 23, 756, 1370, 972, 1597]))
import time

inicio = time.time()
seleção([653, 119, 973, 429, 436, 983, 1864, 1780, 555, 1364, 620, 1746, 1649, 1007, 1767, 489, 1028, 861, 621, 202, 1049, 785, 627, 733, 943, 1044, 513, 761, 932, 124, 1887, 219, 1134, 647, 1419, 402, 1816, 1115, 179, 1491, 833, 917, 292, 371, 463, 552, 614, 1294, 561, 1830, 1490, 987, 731, 871, 214, 1687, 1405, 200, 173, 1246, 660, 544, 1848, 769, 1063, 1439, 1229, 1434, 1813, 1743, 228, 722, 1740, 109, 397, 1048, 1538, 862, 719, 1806, 316, 1509, 83, 1025, 26, 563, 1055, 1962, 760, 1284, 187, 1047, 901, 582, 1702, 106, 95, 1685, 1986, 1752, 1992, 387, 1160, 343, 386, 1893, 669, 1098, 517, 966, 14, 846, 1334, 1219, 1306, 515, 764, 1857, 1839, 98, 829, 1445, 216, 468, 969, 1721, 1937, 953, 54, 1889, 1761, 1908, 276, 108, 723, 1789, 1835, 617, 1844, 503, 22, 175, 853, 1286, 1486, 1975, 1035, 824, 1914, 1154, 260, 148, 838, 232, 1974, 1390, 1395, 1972, 142, 1512, 1958, 594, 100, 954, 1855, 1586, 1332, 1373, 483, 4, 1127, 771, 596, 1800, 1359, 299, 1228, 147, 1187, 1298, 357, 1758, 1227, 1101, 289, 883, 1561, 293, 313, 1680, 1124, 1473, 1075, 1613, 36, 1956, 1401, 1014, 1065, 934, 1995, 1588, 1383, 1764, 1015, 597, 325, 1537, 1462, 1287, 919, 251, 73, 1837, 496, 1671, 1933, 900, 1136, 6, 445, 803, 428, 1636, 1854, 1525, 1372, 1261, 1891, 893, 1808, 1245, 725, 1161, 1731, 27, 1102, 1156, 1400, 721, 454, 709, 1530, 904, 425, 1832, 835, 782, 1528, 1703, 1335, 1355, 1904, 799, 221, 1590, 1959, 1254, 888, 1863, 550, 474, 1531, 924, 1283, 17, 637, 1091, 1967, 795, 351, 577, 1776, 307, 662, 266, 1019, 243, 1510, 1542, 615, 298, 1577, 604, 890, 1069, 913, 1384, 69, 1214, 1905, 1032, 146, 982, 702, 1952, 67, 1683, 1539, 1890, 1480, 818, 107, 1083, 993, 1763, 399, 285, 1300, 1640, 1250, 1669, 845, 19, 1766, 1167, 1879, 457, 546, 1238, 1993, 751, 265, 1323, 828, 635, 1920, 438, 626, 1342, 1635, 1791, 557, 1701, 249, 1496, 950, 1987, 989, 988, 1354, 1621, 1182, 1010, 1950, 1452, 284, 1899, 1040, 1843, 1031, 1798, 729, 412, 1062, 1448, 522, 850, 203, 991, 1906, 376, 1809, 916, 1078, 444, 1714, 190, 1996, 1546, 1875, 1924, 1536, 297, 1426, 612, 1492, 952, 1750, 1605, 321, 1141, 1818, 1197, 1946, 1722, 1684, 1812, 1980, 1282, 1805, 352, 933, 465, 122, 874, 770, 493, 248, 318, 931, 1916, 999, 628, 43, 1070, 127, 1625, 551, 937, 1256, 458, 1624, 1432, 524, 245, 863, 273, 1180, 1943, 74, 207, 1871, 1628, 533, 11, 1381, 1162, 1748, 1527, 304, 24, 126, 1200, 892, 755, 60, 281, 695, 712, 1500, 717, 1697, 1688, 1460, 1626, 1608, 1782, 529, 1913, 1544, 1954, 980, 941, 519, 1478, 1243, 1689, 1922, 1670, 506, 421, 1775, 990, 1202, 589, 1311, 1604, 308, 1437, 1505, 706, 1965, 1568, 160, 1847, 1052, 32, 218, 683, 1146, 413, 1398, 306, 156, 1173, 603, 1345, 1465, 757, 213, 704, 759, 1295, 1185, 40, 1792, 1698, 1915, 12, 491, 752, 854, 1289, 112, 1988, 758, 81, 416, 135, 47, 92, 997, 1903, 327, 1213, 1425, 1216, 1600, 964, 1352, 1869, 586, 1118, 1567, 1596, 167, 435, 1783, 784, 486, 390, 1273, 1280, 1205, 1211, 1076, 447, 1315, 856, 977, 1239, 1941, 41, 75, 881, 1316, 516, 370, 1960, 1866, 870, 1990, 1963, 300, 1244, 353, 372, 1729, 1508, 58, 482, 1945, 1711, 1616, 656, 155, 1519, 578, 1087, 237, 256, 388, 545, 86, 1534, 1234, 1255, 72, 624, 1918, 1222, 1321, 312, 979, 1598, 481, 267, 1073, 676, 480, 963, 689, 1771, 1304, 1386, 663, 1634, 1260, 280, 1690, 896, 355, 1926, 640, 42, 1991, 585, 1247, 691, 254, 1081, 1328, 63, 471, 1139, 1797, 71, 1271, 638, 1885, 94, 1094, 1420, 823, 334, 271, 1569, 736, 962, 230, 1178, 505, 1633, 226, 433, 895, 580, 422, 710, 1375, 192, 1935, 1566, 700, 664, 820, 1240, 1573, 1925, 426, 1005, 339, 633, 1446, 837, 497, 680, 111, 1732, 182, 844, 78, 796, 884, 1801, 1957, 302, 797, 749, 235, 341, 151, 1189, 866, 180, 381, 1451, 1562, 283, 382, 65, 894, 956, 1266, 1674, 1034, 1263, 1449, 1882, 1936, 450, 1119, 140, 295, 1393, 601, 538, 494, 843, 1485, 632, 1607, 1706, 819, 1513, 1108, 1012, 259, 1867, 521, 1454, 1, 739, 798, 955, 1171, 1655, 358, 1646, 1609, 1464, 1175, 745, 13, 542, 3, 1461, 808, 678, 247, 157, 1944, 1724, 1148, 346, 1720, 1363, 686, 1026, 1318, 1111, 184, 1560, 1402, 1495, 1207, 1317, 502, 1231, 791, 263, 1221, 378, 150, 650, 687, 1132, 1479, 677, 1529, 1194, 383, 1796, 1290, 1939, 1371, 1468, 49, 419, 1204, 1650, 1549, 1152, 711, 880, 51, 1251, 1747, 976, 1225, 1705, 921, 1658, 1343, 1274, 965, 564, 1966, 1872, 1874, 1181, 734, 1053, 623, 479, 666, 554, 571, 509, 1054, 434, 87, 1601, 1066, 1117, 744, 1347, 1215, 737, 1281, 1029, 1828, 504, 1592, 792, 1272, 625, 804, 282, 149, 79, 556, 144, 1516, 224, 1900, 1368, 1046, 61, 467, 62, 776, 1097, 1074, 864, 958, 608, 1817, 333, 1253, 34, 852, 10, 1557, 317, 1526, 154, 1397, 909, 1692, 1517, 466, 1896, 1503, 1672, 446, 1374, 1275, 1267, 748, 1440, 891, 970, 659, 1533, 806, 1953, 1862, 1973, 1686, 1772, 940, 392, 1968, 1378, 1765, 753, 959, 1998, 1336, 1351, 668, 877, 1024, 2, 141, 631, 1760, 424, 929, 1145, 696, 768, 1000, 1909, 1522, 1322, 1982, 1540, 1619, 1929, 1120, 1350, 384, 1749, 133, 1482, 9, 1859, 1845, 451, 540, 1971, 847, 469, 113, 648, 1707, 817, 1594, 1417, 1218, 1654, 1907, 822, 1033, 406, 1071, 512, 442, 777, 1970, 787, 1339, 1571, 520, 1113, 1142, 1129, 1288, 671, 1541, 1741, 584, 319, 1781, 1514, 762, 1810, 728, 250, 340, 1376, 363, 110, 651, 1470, 922, 1677, 673, 153, 860, 1143, 85, 30, 579, 1768, 1059, 241, 1297, 35, 1814, 1394, 197, 215, 46, 1807, 169, 172, 1602, 763, 675, 1438, 1825, 773, 174, 1411, 1307, 1778, 826, 1582, 487, 642, 1662, 1084, 1293, 1068, 1656, 629, 1565, 946, 1704, 349, 1564, 718, 395, 1036, 878, 159, 1637, 128, 223, 1691, 778, 573, 1794, 701, 523, 805, 1123, 1366, 1276, 1994, 1212, 1681, 576, 1020, 971, 1421, 510, 287, 1523, 1418, 255, 1130, 1831, 1663, 619, 1017, 201, 420, 1450, 1630, 1581, 1191, 1700, 1103, 1133, 821, 101, 766, 472, 244, 1976, 211, 1615, 44, 570, 841, 657, 164, 592, 1365, 1037, 217, 944, 77, 1803, 68, 23, 756, 1370, 972, 1597])
fim = time.time()
print(fim - inicio)
