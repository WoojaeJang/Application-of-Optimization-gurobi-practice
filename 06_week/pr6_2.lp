\ Model pr6_2
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0 X[0,0] + 702 X[0,1] + 454 X[0,2] + 842 X[0,3] + 2396 X[0,4]
   + 1196 X[0,5] + 864 X[0,6] + 772 X[0,7] + 714 X[0,8] + 554 X[0,9]
   + 2363 X[0,10] + 2679 X[0,11] + 702 X[1,0] + 0 X[1,1] + 324 X[1,2]
   + 1093 X[1,3] + 2136 X[1,4] + 764 X[1,5] + 845 X[1,6] + 764 X[1,7]
   + 459 X[1,8] + 294 X[1,9] + 2184 X[1,10] + 2187 X[1,11] + 454 X[2,0]
   + 324 X[2,1] + 0 X[2,2] + 1137 X[2,3] + 2180 X[2,4] + 798 X[2,5]
   + 664 X[2,6] + 572 X[2,7] + 284 X[2,8] + 338 X[2,9] + 2228 X[2,10]
   + 2463 X[2,11] + 842 X[3,0] + 1093 X[3,1] + 1137 X[3,2] + 0 X[3,3]
   + 1616 X[3,4] + 1857 X[3,5] + 1706 X[3,6] + 1614 X[3,7] + 1421 X[3,8]
   + 779 X[3,9] + 1521 X[3,10] + 2021 X[3,11] + 2396 X[4,0] + 2136 X[4,1]
   + 2180 X[4,2] + 1616 X[4,3] + 0 X[4,4] + 2900 X[4,5] + 2844 X[4,6]
   + 2752 X[4,7] + 2464 X[4,8] + 1842 X[4,9] + 95 X[4,10] + 405 X[4,11]
   + 1196 X[5,0] + 764 X[5,1] + 798 X[5,2] + 1857 X[5,3] + 2900 X[5,4]
   + 0 X[5,5] + 396 X[5,6] + 424 X[5,7] + 514 X[5,8] + 1058 X[5,9]
   + 2948 X[5,10] + 2951 X[5,11] + 864 X[6,0] + 845 X[6,1] + 664 X[6,2]
   + 1706 X[6,3] + 2844 X[6,4] + 396 X[6,5] + 0 X[6,6] + 92 X[6,7]
   + 386 X[6,8] + 1002 X[6,9] + 2892 X[6,10] + 3032 X[6,11] + 772 X[7,0]
   + 764 X[7,1] + 572 X[7,2] + 1614 X[7,3] + 2752 X[7,4] + 424 X[7,5]
   + 92 X[7,6] + 0 X[7,7] + 305 X[7,8] + 910 X[7,9] + 2800 X[7,10]
   + 2951 X[7,11] + 714 X[8,0] + 459 X[8,1] + 284 X[8,2] + 1421 X[8,3]
   + 2464 X[8,4] + 514 X[8,5] + 386 X[8,6] + 305 X[8,7] + 0 X[8,8]
   + 322 X[8,9] + 2512 X[8,10] + 2646 X[8,11] + 554 X[9,0] + 294 X[9,1]
   + 338 X[9,2] + 799 X[9,3] + 1842 X[9,4] + 1058 X[9,5] + 1002 X[9,6]
   + 910 X[9,7] + 622 X[9,8] + 0 X[9,9] + 1890 X[9,10] + 2125 X[9,11]
   + 2363 X[10,0] + 2184 X[10,1] + 2228 X[10,2] + 1521 X[10,3] + 95 X[10,4]
   + 2948 X[10,5] + 2892 X[10,6] + 2800 X[10,7] + 2512 X[10,8]
   + 1890 X[10,9] + 0 X[10,10] + 500 X[10,11] + 2679 X[11,0] + 2187 X[11,1]
   + 2463 X[11,2] + 2021 X[11,3] + 405 X[11,4] + 2951 X[11,5]
   + 3032 X[11,6] + 2951 X[11,7] + 2646 X[11,8] + 2125 X[11,9]
   + 500 X[11,10] + 0 X[11,11] + 0 U[0]
Subject To
 c00: X[1,0] + X[2,0] + X[3,0] + X[4,0] + X[5,0] + X[6,0] + X[7,0] + X[8,0]
   + X[9,0] + X[10,0] + X[11,0] = 1
 c01: X[0,1] + X[2,1] + X[3,1] + X[4,1] + X[5,1] + X[6,1] + X[7,1] + X[8,1]
   + X[9,1] + X[10,1] + X[11,1] = 1
 c02: X[0,2] + X[1,2] + X[3,2] + X[4,2] + X[5,2] + X[6,2] + X[7,2] + X[8,2]
   + X[9,2] + X[10,2] + X[11,2] = 1
 c03: X[0,3] + X[1,3] + X[2,3] + X[4,3] + X[5,3] + X[6,3] + X[7,3] + X[8,3]
   + X[9,3] + X[10,3] + X[11,3] = 1
 c04: X[0,4] + X[1,4] + X[2,4] + X[3,4] + X[5,4] + X[6,4] + X[7,4] + X[8,4]
   + X[9,4] + X[10,4] + X[11,4] = 1
 c05: X[0,5] + X[1,5] + X[2,5] + X[3,5] + X[4,5] + X[6,5] + X[7,5] + X[8,5]
   + X[9,5] + X[10,5] + X[11,5] = 1
 c06: X[0,6] + X[1,6] + X[2,6] + X[3,6] + X[4,6] + X[5,6] + X[7,6] + X[8,6]
   + X[9,6] + X[10,6] + X[11,6] = 1
 c07: X[0,7] + X[1,7] + X[2,7] + X[3,7] + X[4,7] + X[5,7] + X[6,7] + X[8,7]
   + X[9,7] + X[10,7] + X[11,7] = 1
 c08: X[0,8] + X[1,8] + X[2,8] + X[3,8] + X[4,8] + X[5,8] + X[6,8] + X[7,8]
   + X[9,8] + X[10,8] + X[11,8] = 1
 c09: X[0,9] + X[1,9] + X[2,9] + X[3,9] + X[4,9] + X[5,9] + X[6,9] + X[7,9]
   + X[8,9] + X[10,9] + X[11,9] = 1
 c010: X[0,10] + X[1,10] + X[2,10] + X[3,10] + X[4,10] + X[5,10] + X[6,10]
   + X[7,10] + X[8,10] + X[9,10] + X[11,10] = 1
 c011: X[0,11] + X[1,11] + X[2,11] + X[3,11] + X[4,11] + X[5,11] + X[6,11]
   + X[7,11] + X[8,11] + X[9,11] + X[10,11] = 1
 c10: X[0,1] + X[0,2] + X[0,3] + X[0,4] + X[0,5] + X[0,6] + X[0,7] + X[0,8]
   + X[0,9] + X[0,10] + X[0,11] = 1
 c11: X[1,0] + X[1,2] + X[1,3] + X[1,4] + X[1,5] + X[1,6] + X[1,7] + X[1,8]
   + X[1,9] + X[1,10] + X[1,11] = 1
 c12: X[2,0] + X[2,1] + X[2,3] + X[2,4] + X[2,5] + X[2,6] + X[2,7] + X[2,8]
   + X[2,9] + X[2,10] + X[2,11] = 1
 c13: X[3,0] + X[3,1] + X[3,2] + X[3,4] + X[3,5] + X[3,6] + X[3,7] + X[3,8]
   + X[3,9] + X[3,10] + X[3,11] = 1
 c14: X[4,0] + X[4,1] + X[4,2] + X[4,3] + X[4,5] + X[4,6] + X[4,7] + X[4,8]
   + X[4,9] + X[4,10] + X[4,11] = 1
 c15: X[5,0] + X[5,1] + X[5,2] + X[5,3] + X[5,4] + X[5,6] + X[5,7] + X[5,8]
   + X[5,9] + X[5,10] + X[5,11] = 1
 c16: X[6,0] + X[6,1] + X[6,2] + X[6,3] + X[6,4] + X[6,5] + X[6,7] + X[6,8]
   + X[6,9] + X[6,10] + X[6,11] = 1
 c17: X[7,0] + X[7,1] + X[7,2] + X[7,3] + X[7,4] + X[7,5] + X[7,6] + X[7,8]
   + X[7,9] + X[7,10] + X[7,11] = 1
 c18: X[8,0] + X[8,1] + X[8,2] + X[8,3] + X[8,4] + X[8,5] + X[8,6] + X[8,7]
   + X[8,9] + X[8,10] + X[8,11] = 1
 c19: X[9,0] + X[9,1] + X[9,2] + X[9,3] + X[9,4] + X[9,5] + X[9,6] + X[9,7]
   + X[9,8] + X[9,10] + X[9,11] = 1
 c110: X[10,0] + X[10,1] + X[10,2] + X[10,3] + X[10,4] + X[10,5] + X[10,6]
   + X[10,7] + X[10,8] + X[10,9] + X[10,11] = 1
 c111: X[11,0] + X[11,1] + X[11,2] + X[11,3] + X[11,4] + X[11,5] + X[11,6]
   + X[11,7] + X[11,8] + X[11,9] + X[11,10] = 1
 c2102: - 9 X[1,2] - 11 X[2,1] + U[1] - U[2] >= -10
 c2103: - 9 X[1,3] - 11 X[3,1] + U[1] - U[3] >= -10
 c2104: - 9 X[1,4] - 11 X[4,1] + U[1] - U[4] >= -10
 c2105: - 9 X[1,5] - 11 X[5,1] + U[1] - U[5] >= -10
 c2106: - 9 X[1,6] - 11 X[6,1] + U[1] - U[6] >= -10
 c2107: - 9 X[1,7] - 11 X[7,1] + U[1] - U[7] >= -10
 c2108: - 9 X[1,8] - 11 X[8,1] + U[1] - U[8] >= -10
 c2109: - 9 X[1,9] - 11 X[9,1] + U[1] - U[9] >= -10
 c21010: - 9 X[1,10] - 11 X[10,1] + U[1] - U[10] >= -10
 c21011: - 9 X[1,11] - 11 X[11,1] + U[1] - U[11] >= -10
 c2201: - 11 X[1,2] - 9 X[2,1] - U[1] + U[2] >= -10
 c2203: - 9 X[2,3] - 11 X[3,2] + U[2] - U[3] >= -10
 c2204: - 9 X[2,4] - 11 X[4,2] + U[2] - U[4] >= -10
 c2205: - 9 X[2,5] - 11 X[5,2] + U[2] - U[5] >= -10
 c2206: - 9 X[2,6] - 11 X[6,2] + U[2] - U[6] >= -10
 c2207: - 9 X[2,7] - 11 X[7,2] + U[2] - U[7] >= -10
 c2208: - 9 X[2,8] - 11 X[8,2] + U[2] - U[8] >= -10
 c2209: - 9 X[2,9] - 11 X[9,2] + U[2] - U[9] >= -10
 c22010: - 9 X[2,10] - 11 X[10,2] + U[2] - U[10] >= -10
 c22011: - 9 X[2,11] - 11 X[11,2] + U[2] - U[11] >= -10
 c2301: - 11 X[1,3] - 9 X[3,1] - U[1] + U[3] >= -10
 c2302: - 11 X[2,3] - 9 X[3,2] - U[2] + U[3] >= -10
 c2304: - 9 X[3,4] - 11 X[4,3] + U[3] - U[4] >= -10
 c2305: - 9 X[3,5] - 11 X[5,3] + U[3] - U[5] >= -10
 c2306: - 9 X[3,6] - 11 X[6,3] + U[3] - U[6] >= -10
 c2307: - 9 X[3,7] - 11 X[7,3] + U[3] - U[7] >= -10
 c2308: - 9 X[3,8] - 11 X[8,3] + U[3] - U[8] >= -10
 c2309: - 9 X[3,9] - 11 X[9,3] + U[3] - U[9] >= -10
 c23010: - 9 X[3,10] - 11 X[10,3] + U[3] - U[10] >= -10
 c23011: - 9 X[3,11] - 11 X[11,3] + U[3] - U[11] >= -10
 c2401: - 11 X[1,4] - 9 X[4,1] - U[1] + U[4] >= -10
 c2402: - 11 X[2,4] - 9 X[4,2] - U[2] + U[4] >= -10
 c2403: - 11 X[3,4] - 9 X[4,3] - U[3] + U[4] >= -10
 c2405: - 9 X[4,5] - 11 X[5,4] + U[4] - U[5] >= -10
 c2406: - 9 X[4,6] - 11 X[6,4] + U[4] - U[6] >= -10
 c2407: - 9 X[4,7] - 11 X[7,4] + U[4] - U[7] >= -10
 c2408: - 9 X[4,8] - 11 X[8,4] + U[4] - U[8] >= -10
 c2409: - 9 X[4,9] - 11 X[9,4] + U[4] - U[9] >= -10
 c24010: - 9 X[4,10] - 11 X[10,4] + U[4] - U[10] >= -10
 c24011: - 9 X[4,11] - 11 X[11,4] + U[4] - U[11] >= -10
 c2501: - 11 X[1,5] - 9 X[5,1] - U[1] + U[5] >= -10
 c2502: - 11 X[2,5] - 9 X[5,2] - U[2] + U[5] >= -10
 c2503: - 11 X[3,5] - 9 X[5,3] - U[3] + U[5] >= -10
 c2504: - 11 X[4,5] - 9 X[5,4] - U[4] + U[5] >= -10
 c2506: - 9 X[5,6] - 11 X[6,5] + U[5] - U[6] >= -10
 c2507: - 9 X[5,7] - 11 X[7,5] + U[5] - U[7] >= -10
 c2508: - 9 X[5,8] - 11 X[8,5] + U[5] - U[8] >= -10
 c2509: - 9 X[5,9] - 11 X[9,5] + U[5] - U[9] >= -10
 c25010: - 9 X[5,10] - 11 X[10,5] + U[5] - U[10] >= -10
 c25011: - 9 X[5,11] - 11 X[11,5] + U[5] - U[11] >= -10
 c2601: - 11 X[1,6] - 9 X[6,1] - U[1] + U[6] >= -10
 c2602: - 11 X[2,6] - 9 X[6,2] - U[2] + U[6] >= -10
 c2603: - 11 X[3,6] - 9 X[6,3] - U[3] + U[6] >= -10
 c2604: - 11 X[4,6] - 9 X[6,4] - U[4] + U[6] >= -10
 c2605: - 11 X[5,6] - 9 X[6,5] - U[5] + U[6] >= -10
 c2607: - 9 X[6,7] - 11 X[7,6] + U[6] - U[7] >= -10
 c2608: - 9 X[6,8] - 11 X[8,6] + U[6] - U[8] >= -10
 c2609: - 9 X[6,9] - 11 X[9,6] + U[6] - U[9] >= -10
 c26010: - 9 X[6,10] - 11 X[10,6] + U[6] - U[10] >= -10
 c26011: - 9 X[6,11] - 11 X[11,6] + U[6] - U[11] >= -10
 c2701: - 11 X[1,7] - 9 X[7,1] - U[1] + U[7] >= -10
 c2702: - 11 X[2,7] - 9 X[7,2] - U[2] + U[7] >= -10
 c2703: - 11 X[3,7] - 9 X[7,3] - U[3] + U[7] >= -10
 c2704: - 11 X[4,7] - 9 X[7,4] - U[4] + U[7] >= -10
 c2705: - 11 X[5,7] - 9 X[7,5] - U[5] + U[7] >= -10
 c2706: - 11 X[6,7] - 9 X[7,6] - U[6] + U[7] >= -10
 c2708: - 9 X[7,8] - 11 X[8,7] + U[7] - U[8] >= -10
 c2709: - 9 X[7,9] - 11 X[9,7] + U[7] - U[9] >= -10
 c27010: - 9 X[7,10] - 11 X[10,7] + U[7] - U[10] >= -10
 c27011: - 9 X[7,11] - 11 X[11,7] + U[7] - U[11] >= -10
 c2801: - 11 X[1,8] - 9 X[8,1] - U[1] + U[8] >= -10
 c2802: - 11 X[2,8] - 9 X[8,2] - U[2] + U[8] >= -10
 c2803: - 11 X[3,8] - 9 X[8,3] - U[3] + U[8] >= -10
 c2804: - 11 X[4,8] - 9 X[8,4] - U[4] + U[8] >= -10
 c2805: - 11 X[5,8] - 9 X[8,5] - U[5] + U[8] >= -10
 c2806: - 11 X[6,8] - 9 X[8,6] - U[6] + U[8] >= -10
 c2807: - 11 X[7,8] - 9 X[8,7] - U[7] + U[8] >= -10
 c2809: - 9 X[8,9] - 11 X[9,8] + U[8] - U[9] >= -10
 c28010: - 9 X[8,10] - 11 X[10,8] + U[8] - U[10] >= -10
 c28011: - 9 X[8,11] - 11 X[11,8] + U[8] - U[11] >= -10
 c2901: - 11 X[1,9] - 9 X[9,1] - U[1] + U[9] >= -10
 c2902: - 11 X[2,9] - 9 X[9,2] - U[2] + U[9] >= -10
 c2903: - 11 X[3,9] - 9 X[9,3] - U[3] + U[9] >= -10
 c2904: - 11 X[4,9] - 9 X[9,4] - U[4] + U[9] >= -10
 c2905: - 11 X[5,9] - 9 X[9,5] - U[5] + U[9] >= -10
 c2906: - 11 X[6,9] - 9 X[9,6] - U[6] + U[9] >= -10
 c2907: - 11 X[7,9] - 9 X[9,7] - U[7] + U[9] >= -10
 c2908: - 11 X[8,9] - 9 X[9,8] - U[8] + U[9] >= -10
 c29010: - 9 X[9,10] - 11 X[10,9] + U[9] - U[10] >= -10
 c29011: - 9 X[9,11] - 11 X[11,9] + U[9] - U[11] >= -10
 c21001: - 11 X[1,10] - 9 X[10,1] - U[1] + U[10] >= -10
 c21002: - 11 X[2,10] - 9 X[10,2] - U[2] + U[10] >= -10
 c21003: - 11 X[3,10] - 9 X[10,3] - U[3] + U[10] >= -10
 c21004: - 11 X[4,10] - 9 X[10,4] - U[4] + U[10] >= -10
 c21005: - 11 X[5,10] - 9 X[10,5] - U[5] + U[10] >= -10
 c21006: - 11 X[6,10] - 9 X[10,6] - U[6] + U[10] >= -10
 c21007: - 11 X[7,10] - 9 X[10,7] - U[7] + U[10] >= -10
 c21008: - 11 X[8,10] - 9 X[10,8] - U[8] + U[10] >= -10
 c21009: - 11 X[9,10] - 9 X[10,9] - U[9] + U[10] >= -10
 c210011: - 9 X[10,11] - 11 X[11,10] + U[10] - U[11] >= -10
 c21101: - 11 X[1,11] - 9 X[11,1] - U[1] + U[11] >= -10
 c21102: - 11 X[2,11] - 9 X[11,2] - U[2] + U[11] >= -10
 c21103: - 11 X[3,11] - 9 X[11,3] - U[3] + U[11] >= -10
 c21104: - 11 X[4,11] - 9 X[11,4] - U[4] + U[11] >= -10
 c21105: - 11 X[5,11] - 9 X[11,5] - U[5] + U[11] >= -10
 c21106: - 11 X[6,11] - 9 X[11,6] - U[6] + U[11] >= -10
 c21107: - 11 X[7,11] - 9 X[11,7] - U[7] + U[11] >= -10
 c21108: - 11 X[8,11] - 9 X[11,8] - U[8] + U[11] >= -10
 c21109: - 11 X[9,11] - 9 X[11,9] - U[9] + U[11] >= -10
 c211010: - 11 X[10,11] - 9 X[11,10] - U[10] + U[11] >= -10
 c31: 10 X[0,1] + U[1] <= 11
 c41: - 10 X[1,0] + U[1] >= 1
 c32: 10 X[0,2] + U[2] <= 11
 c42: - 10 X[2,0] + U[2] >= 1
 c33: 10 X[0,3] + U[3] <= 11
 c43: - 10 X[3,0] + U[3] >= 1
 c34: 10 X[0,4] + U[4] <= 11
 c44: - 10 X[4,0] + U[4] >= 1
 c35: 10 X[0,5] + U[5] <= 11
 c45: - 10 X[5,0] + U[5] >= 1
 c36: 10 X[0,6] + U[6] <= 11
 c46: - 10 X[6,0] + U[6] >= 1
 c37: 10 X[0,7] + U[7] <= 11
 c47: - 10 X[7,0] + U[7] >= 1
 c38: 10 X[0,8] + U[8] <= 11
 c48: - 10 X[8,0] + U[8] >= 1
 c39: 10 X[0,9] + U[9] <= 11
 c49: - 10 X[9,0] + U[9] >= 1
 c310: 10 X[0,10] + U[10] <= 11
 c410: - 10 X[10,0] + U[10] >= 1
 c311: 10 X[0,11] + U[11] <= 11
 c411: - 10 X[11,0] + U[11] >= 1
Bounds
Binaries
 X[0,0] X[0,1] X[0,2] X[0,3] X[0,4] X[0,5] X[0,6] X[0,7] X[0,8] X[0,9]
 X[0,10] X[0,11] X[1,0] X[1,1] X[1,2] X[1,3] X[1,4] X[1,5] X[1,6] X[1,7]
 X[1,8] X[1,9] X[1,10] X[1,11] X[2,0] X[2,1] X[2,2] X[2,3] X[2,4] X[2,5]
 X[2,6] X[2,7] X[2,8] X[2,9] X[2,10] X[2,11] X[3,0] X[3,1] X[3,2] X[3,3]
 X[3,4] X[3,5] X[3,6] X[3,7] X[3,8] X[3,9] X[3,10] X[3,11] X[4,0] X[4,1]
 X[4,2] X[4,3] X[4,4] X[4,5] X[4,6] X[4,7] X[4,8] X[4,9] X[4,10] X[4,11]
 X[5,0] X[5,1] X[5,2] X[5,3] X[5,4] X[5,5] X[5,6] X[5,7] X[5,8] X[5,9]
 X[5,10] X[5,11] X[6,0] X[6,1] X[6,2] X[6,3] X[6,4] X[6,5] X[6,6] X[6,7]
 X[6,8] X[6,9] X[6,10] X[6,11] X[7,0] X[7,1] X[7,2] X[7,3] X[7,4] X[7,5]
 X[7,6] X[7,7] X[7,8] X[7,9] X[7,10] X[7,11] X[8,0] X[8,1] X[8,2] X[8,3]
 X[8,4] X[8,5] X[8,6] X[8,7] X[8,8] X[8,9] X[8,10] X[8,11] X[9,0] X[9,1]
 X[9,2] X[9,3] X[9,4] X[9,5] X[9,6] X[9,7] X[9,8] X[9,9] X[9,10] X[9,11]
 X[10,0] X[10,1] X[10,2] X[10,3] X[10,4] X[10,5] X[10,6] X[10,7] X[10,8]
 X[10,9] X[10,10] X[10,11] X[11,0] X[11,1] X[11,2] X[11,3] X[11,4] X[11,5]
 X[11,6] X[11,7] X[11,8] X[11,9] X[11,10] X[11,11]
Generals
 U[0] U[1] U[2] U[3] U[4] U[5] U[6] U[7] U[8] U[9] U[10] U[11]
End
