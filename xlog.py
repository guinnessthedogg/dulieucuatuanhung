import binascii  # line:1
import codecs  # line:2
import ctypes  # line:3
import json  # line:4
import struct  # line:5


class XLEncrypt:  # line:8
    def encrypt(O00O00OO0OOO0O0O0, OO0O0OOOO0OOOO000):  # line:9
        OO0O0OOOO0OOOO000 = list(OO0O0OOOO0OOOO000.encode())  # line:10
        O0OO000OOOOOOOO00 = len(OO0O0OOOO0OOOO000)  # line:11
        OO0000O00O0000OO0 = 4 - O0OO000OOOOOOOO00 % 4  # line:13
        O000O000O000O00OO = 8 - O0OO000OOOOOOOO00 % 8  # line:15
        if O000O000O000O00OO == 8:  # line:17
            O000O000O000O00OO = 0  # line:18
        O0OO0O000O0OOO0OO = []  # line:20
        # line:21
        for O00OOO0OOOOO0OOOO in range(O0OO000OOOOOOOO00 + O000O000O000O00OO + 8):
            O0OO0O000O0OOO0OO.append(0)  # line:22
        O00000OOO0000OO0O = [0x78, 0x46, 0x8E, 0xC4, 0x74, 0x4C, 0x00, 0x00]  # line:23
        O0OO0O000O0OOO0OO[0] = 0x80 | O000O000O000O00OO - 256  # line:24
        O0OO0O000O0OOO0OO[1] = 0x30  # line:25
        O0OO0O000O0OOO0OO[2] = 0x22  # line:26
        O0OO0O000O0OOO0OO[3] = 0x24  # line:27
        OOO00OOO00000OOOO = "02"  # line:29
        for O00OOO0OOOOO0OOOO in range(len(OO0O0OOOO0OOOO000)):  # line:31
            O0OO0O000O0OOO0OO[
                OO0000O00O0000OO0 + O00OOO0OOOOO0OOOO
            ] = OO0O0OOOO0OOOO000[
                O00OOO0OOOOO0OOOO
            ]  # line:32
        for O00OOO0OOOOO0OOOO in range(len(O0OO0O000O0OOO0OO) // 8):  # line:34
            O0O000O0OOO00O000 = ""  # line:36
            for OO0OOOOO0000O0OOO in range(8):  # line:37
                # line:39
                O0O0OOOO0O0OO0O00 = O0OO0O000O0OOO0OO[
                    OO0OOOOO0000O0OOO + 8 * O00OOO0OOOOO0OOOO
                ]
                # line:41
                O0O000O0000O0000O = O00000OOO0000OO0O[OO0OOOOO0000O0OOO]
                if O0O000O0000O0000O < 0:  # line:43
                    O0O000O0000O0000O = O0O000O0000O0000O + 256  # line:44
                if O0O0OOOO0O0OO0O00 < 0:  # line:45
                    O0O0OOOO0O0OO0O00 = O0O0OOOO0O0OO0O00 + 256  # line:46
                OOOO00000OO0O00O0 = O0O0OOOO0O0OO0O00 ^ O0O000O0000O0000O  # line:48
                if OOOO00000OO0O00O0 == 0:  # line:50
                    O0O000O0OOO00O000 += "00"  # line:51
                else:  # line:53
                    # line:54
                    O0O000O0OOO00O000 += O00O00OO0OOO0O0O0.hex2string(OOOO00000OO0O00O0)
            O0O0000OO0O0O0O00 = O00O00OO0OOO0O0O0.getHandleCount("78468ec4")  # line:56
            O0OO0OO0O0O00000O = O00O00OO0OOO0O0O0.calculateRev(
                O0O000O0OOO00O000, O0O0000OO0O0O0O00
            )  # line:57
            for O000OOOOOOOOOO0OO in range(8):  # line:59
                # line:60
                O0OOO0O0O0OOO0OOO = O0OO0OO0O0O00000O[
                    2 * O000OOOOOOOOOO0OO : 2 * O000OOOOOOOOOO0OO + 2
                ]
                O00000OOO0000OO0O[O000OOOOOOOOOO0OO] = int(
                    O0OOO0O0O0OOO0OOO, 16
                )  # line:61
            OOO00OOO00000OOOO += O0OO0OO0O0O00000O  # line:63
        OOO00OOO00000OOOO += "78468ec4"  # line:65
        return OOO00OOO00000OOOO  # line:67

    def decrypt(O0OO0O0O00OO00O00, O0O0O00O000O00O0O):  # line:69
        OOO00O0O00O0000O0 = O0O0O00O000O00O0O[2:]  # line:70
        O000O0O0O0O0O00OO = []  # line:71
        for O0000OO0OOOO0000O in range(int(len(OOO00O0O00O0000O0) / 16)):  # line:72
            # line:73
            O0OO0O0OOO0OO00O0 = OOO00O0O00O0000O0[
                O0000OO0OOOO0000O * 16 : O0000OO0OOOO0000O * 16 + 16
            ]
            O000O0O0O0O0O00OO.append(O0OO0O0OOO0OO00O0)  # line:74
        O000O0O00OO00OOOO = OOO00O0O00O0000O0[
            (int(len(OOO00O0O00O0000O0) / 16) * 16) :
        ]  # line:75
        O000O0O0O0O0O00OO.append(O000O0O00OO00OOOO)  # line:76
        OO0O0OO0O0OOOOO00 = O0OO0O0O00OO00O00.getHandleCount(
            O000O0O00OO00OOOO
        )  # line:77
        _O00O000OO0OOO00OO = ""  # line:78
        for O0000OO0OOOO0000O in range(len(O000O0O0O0O0O00OO) - 1):  # line:79
            OO000OOOO0000O0OO = O0OO0O0O00OO00O00.calculate(
                O000O0O0O0O0O00OO[O0000OO0OOOO0000O], OO0O0OO0O0OOOOO00
            )  # line:80
            if O0000OO0OOOO0000O == 0:  # line:82
                O0O00OOOO0O00O00O = O000O0O00OO00OOOO + "744c0000"  # line:83
                for OO0OOO00OOOO0OOO0 in range(8):  # line:84
                    OOO0O0O0OOOO0O000 = O0OO0O0O00OO00O00.xor(
                        OO000OOOO0000O0OO[
                            OO0OOO00OOOO0OOO0 * 2 : OO0OOO00OOOO0OOO0 * 2 + 2
                        ],
                        O0O00OOOO0O00O00O[
                            OO0OOO00OOOO0OOO0 * 2 : OO0OOO00OOOO0OOO0 * 2 + 2
                        ],
                    )  # line:85
                    if len(OOO0O0O0OOOO0O000) < 2:  # line:86
                        OOO0O0O0OOOO0O000 = "0" + OOO0O0O0OOOO0O000  # line:87
                    _O00O000OO0OOO00OO += OOO0O0O0OOOO0O000  # line:88
            if O0000OO0OOOO0000O >= 1:  # line:89
                # line:90
                O0O00OOOO0O00O00O = O000O0O0O0O0O00OO[O0000OO0OOOO0000O - 1]
                for OO0OOO00OOOO0OOO0 in range(8):  # line:91
                    OOO0O0O0OOOO0O000 = O0OO0O0O00OO00O00.xor(
                        OO000OOOO0000O0OO[
                            OO0OOO00OOOO0OOO0 * 2 : OO0OOO00OOOO0OOO0 * 2 + 2
                        ],
                        O0O00OOOO0O00O00O[
                            OO0OOO00OOOO0OOO0 * 2 : OO0OOO00OOOO0OOO0 * 2 + 2
                        ],
                    )  # line:92
                    if len(OOO0O0O0OOOO0O000) < 2:  # line:93
                        OOO0O0O0OOOO0O000 = "0" + OOO0O0O0OOOO0O000  # line:94
                    _O00O000OO0OOO00OO += OOO0O0O0OOOO0O000  # line:95
        OO0O000000O0000OO = codecs.decode(_O00O000OO0OOO00OO, "hex_codec")  # line:96
        O0O00OOO0000000O0 = int(OO0O000000O0000OO[0]) & 7  # line:98
        OOO0O0OOOOO00O0O0 = (
            (len(O0O0O00O000O00O0O) // 2) - 13 - O0O00OOO0000000O0
        )  # line:100
        O0O00OOO0000000O0 = O0O00OOO0000000O0 % 4  # line:101
        if O0O00OOO0000000O0 == 0:  # line:102
            O0O00OOO0000000O0 = 4  # line:103
        OO00O00000O0O00O0 = bytearray(OOO0O0OOOOO00O0O0)  # line:104
        for O0000OO0OOOO0000O in range(OOO0O0OOOOO00O0O0):  # line:105
            # line:106
            OO00O00000O0O00O0[O0000OO0OOOO0000O] = OO0O000000O0000OO[
                O0O00OOO0000000O0 + O0000OO0OOOO0000O
            ]
        return OO00O00000O0O00O0.decode()  # line:108

    def calculate(O0O00O000OOOO0O0O, OOO0OO0OO0OOO000O, O0OO000OOOO0O0OO0):  # line:110
        if len(OOO0OO0OO0OOO000O) != 16:  # line:111
            return ""  # line:112
        OOO00O0O0OO0OOOO0 = ctypes.c_int(0xBFFFE920 << 0).value  # line:113
        O0O00OO0O0O00O00O = ctypes.c_int(
            (0x9E3779B9 * O0OO000OOOO0O0OO0) << 0
        ).value  # line:114
        OO0OO00OO0OOOOO0O = (
            int(OOO0OO0OO0OOO000O[0:8], 16) << 0 & 0xFFFFFFFF
        )  # line:115
        OOO00O0O0OOO00OO0 = (
            int(OOO0OO0OO0OOO000O[8:16], 16) << 0 & 0xFFFFFFFF
        )  # line:116
        for OOO000O0OOOO0OO0O in range(O0OO000OOOO0O0OO0):  # line:118
            OO000O000OOOO000O = OO0OO00OO0OOOOO0O  # line:119
            O0O0O00OO0O0000O0 = OO0OO00OO0OOOOO0O  # line:120
            OO000OOOO0OO00OOO = OO0OO00OO0OOOOO0O  # line:121
            OOO000O0O000OO00O = O0O00OO0O0O00O00O  # line:122
            OO00OOOOOOO00OO00 = OOO00O0O0OO0OOOO0  # line:123
            OO0OOOO0OO0000O00 = format(
                O0O00O000OOOO0O0O.rshift(OOO000O0O000OO00O >> 0xB, 0) >> 0, "b"
            )  # line:124
            if len(OO0OOOO0OO0000O00) < 3:  # line:125
                OO0OOOO0OO0000O00 = "0"  # line:126
            else:  # line:127
                OO0OOOO0OO0000O00 = OO0OOOO0OO0000O00[
                    len(OO0OOOO0OO0000O00) - 2 :
                ]  # line:128
            OOO000O0O000OO00O = int(OO0OOOO0OO0000O00, 2)  # line:130
            OO000O000OOOO000O = ctypes.c_int(
                (
                    (
                        O0O00O000OOOO0O0O.rshift(O0O0O00OO0O0000O0, 5)
                        ^ OO000O000OOOO000O << 4
                    )
                    + OO000OOOO0OO00OOO
                )
                << 0
            ).value  # line:131
            OO00OOOOOOO00OO00 = ctypes.c_int(
                O0O00O000OOOO0O0O.getShifting(
                    OO00OOOOOOO00OO00 + (OOO000O0O000OO00O << 2)
                )
            ).value  # line:132
            OOO000O0O000OO00O = 0x61C88647 << 0 & 0xFFFFFFFF  # line:133
            O0O0O00OO0O0000O0 = (
                O0O00OO0O0O00O00O + OO00OOOOOOO00OO00
            ) << 0 & 0xFFFFFFFF  # line:134
            OO00OOOOOOO00OO00 = O0O00OO0O0O00O00O  # line:136
            OO000O000OOOO000O = OO000O000OOOO000O ^ O0O0O00OO0O0000O0  # line:137
            O0O0O00OO0O0000O0 = OOO00O0O0OO0OOOO0  # line:138
            OOO000O0O000OO00O = (
                OOO000O0O000OO00O + OO00OOOOOOO00OO00
            ) << 0 & 0xFFFFFFFF  # line:140
            OO000OOOO0OO00OOO = (
                OOO00O0O0OOO00OO0 - OO000O000OOOO000O
            ) << 0 & 0xFFFFFFFF  # line:141
            OO00OOOOOOO00OO00 = OOO000O0O000OO00O & 3  # line:143
            OO000O000OOOO000O = OO000OOOO0OO00OOO << 4  # line:144
            O0O0O00OO0O0000O0 = O0O00O000OOOO0O0O.getShifting(
                O0O0O00OO0O0000O0 + (OO00OOOOOOO00OO00 << 2) & 0xFFFFFFFF
            )  # line:145
            OO000O000OOOO000O = (
                (OO000O000OOOO000O ^ (O0O00O000OOOO0O0O.rshift(OO000OOOO0OO00OOO, 5)))
                + OO000OOOO0OO00OOO
            ) << 0  # line:146
            O0O0O00OO0O0000O0 = (
                O0O0O00OO0O0000O0 + OOO000O0O000OO00O
            ) << 0 & 0xFFFFFFFF  # line:147
            OO000O000OOOO000O = OO000O000OOOO000O ^ O0O0O00OO0O0000O0  # line:148
            OO0OO00OO0OOOOO0O = (
                OO0OO00OO0OOOOO0O - OO000O000OOOO000O
            ) << 0 & 0xFFFFFFFF  # line:149
            O0O00OO0O0O00O00O = OOO000O0O000OO00O & 0xFFFFFFFF  # line:150
            OOO00O0O0OOO00OO0 = OO000OOOO0OO00OOO & 0xFFFFFFFF  # line:151
        OOOO0000O00OOOOOO = format(
            O0O00O000OOOO0O0O.rshift(OO0OO00OO0OOOOO0O, 0), "x"
        )  # line:152
        OO0000OO0O0O00OOO = format(
            O0O00O000OOOO0O0O.rshift(OOO00O0O0OOO00OO0, 0), "x"
        )  # line:154
        if len(OOOO0000O00OOOOOO) < 8:  # line:156
            OO000000000O0OO00 = 8 - len(OOOO0000O00OOOOOO)  # line:157
            for OOO000O0OOOO0OO0O in range(OO000000000O0OO00):  # line:159
                OOOO0000O00OOOOOO = "0" + OOOO0000O00OOOOOO  # line:160
        if len(OO0000OO0O0O00OOO) < 8:  # line:162
            OO000000000O0OO00 = 8 - len(OO0000OO0O0O00OOO)  # line:163
            for OOO000O0OOOO0OO0O in range(OO000000000O0OO00):  # line:164
                OO0000OO0O0O00OOO = "0" + OO0000OO0O0O00OOO  # line:165
        return OOOO0000O00OOOOOO + OO0000OO0O0O00OOO  # line:167

    def xor(O0OO0OOOOOOO0OOOO, O000O00OO0OOO0O00, OO000OO000OOO0OO0):  # line:169
        O00OOOO00OOOO0OO0 = format(int(O000O00OO0OOO0O00, 16), "b")  # line:170
        O0OO00O00OOOOO000 = format(int(OO000OO000OOO0OO0, 16), "b")  # line:171
        O0O0OO0OOOO000O0O = ""  # line:172
        if len(O00OOOO00OOOO0OO0) != 8:  # line:173
            for O000OO0OO0OOO0OOO in range(len(O00OOOO00OOOO0OO0), 8):  # line:174
                O00OOOO00OOOO0OO0 = "0" + O00OOOO00OOOO0OO0  # line:175
        if len(O0OO00O00OOOOO000) != 8:  # line:177
            for O000OO0OO0OOO0OOO in range(len(O0OO00O00OOOOO000), 8):  # line:178
                O0OO00O00OOOOO000 = "0" + O0OO00O00OOOOO000  # line:179
        for O000OO0OO0OOO0OOO in range(len(O00OOOO00OOOO0OO0)):  # line:180
            # line:181
            if (
                O0OO00O00OOOOO000[O000OO0OO0OOO0OOO]
                == O00OOOO00OOOO0OO0[O000OO0OO0OOO0OOO]
            ):
                O0O0OO0OOOO000O0O += "0"  # line:182
            else:  # line:183
                O0O0OO0OOOO000O0O += "1"  # line:184
        return format((int(O0O0OO0OOOO000O0O, 2)), "x")  # line:186

    def getHandleCount(OOOO00OOO0O000OOO, OO0000OOO00OO00O0):  # line:188
        OO0000OOOOOOO0O0O = OOOO00OOO0O000OOO.reverse(OO0000OOO00OO00O0)  # line:189
        O0O0O00OOO0O0OOO0 = 0xCCCCCCCD  # line:190
        OOO000O0OO0O0O0O0 = int(OO0000OOOOOOO0O0O, 16)  # line:191
        O0OOOOO0O00OOO0O0 = OOOO00OOO0O000OOO.getUmullHigh(
            OOO000O0OO0O0O0O0, O0O0O00OOO0O0OOO0
        )  # line:192
        O0OOOOO0O00OOO0O0 = ctypes.c_int(O0OOOOO0O00OOO0O0 >> 2).value  # line:193
        O0OOOOO0O00OOO0O0 = (
            O0OOOOO0O00OOO0O0 + ctypes.c_int((O0OOOOO0O00OOO0O0 << 2)).value
        )  # line:194
        OOO000O0OO0O0O0O0 = OOO000O0OO0O0O0O0 - O0OOOOO0O00OOO0O0  # line:195
        O0OOOOO0O00OOO0O0 = 0x20  # line:196
        OOO000O0OO0O0O0O0 = (
            O0OOOOO0O00OOO0O0 + ctypes.c_int(OOO000O0OO0O0O0O0 << 3).value
        )  # line:197
        return OOO000O0OO0O0O0O0  # line:198

    def getShifting(O00OOO0OO00O0OOO0, OO00O00OOO0OO00O0):  # line:200
        O0OOOO0O00OOO0000 = ctypes.c_int(OO00O00OOO0OO00O0 << 0).value  # line:201
        # line:203
        if O0OOOO0O00OOO0000 == ctypes.c_int(0xBFFFE920 << 0).value:
            return ctypes.c_int(0x477001DE << 0).value  # line:204
        # line:205
        if O0OOOO0O00OOO0000 == ctypes.c_int(0xBFFFE924 << 0).value:
            return ctypes.c_int(0xFACEDEAD << 0).value  # line:206
        # line:207
        if O0OOOO0O00OOO0000 == ctypes.c_int(0xBFFFE928 << 0).value:
            return ctypes.c_int(0x30303030 << 0).value  # line:208
        # line:209
        if O0OOOO0O00OOO0000 == ctypes.c_int(0xBFFFE92C << 0).value:
            return ctypes.c_int(0x39353237 << 0).value  # line:210
        return 0x00000000  # line:211

    def calculateRev(
        OO0O000OO0O00O000, OOOO00O00OOO000O0, OO00O0OO0OO00O000
    ):  # line:213
        O0000OOOO0O00O00O = 0xBFFFE920 << 0 & 0xFFFFFFFF  # line:214
        OO0OOOO00000O000O = 0x0  # line:215
        OO00O00000OO0O00O = (
            int(OOOO00O00OOO000O0[0:8], 16) << 0 & 0xFFFFFFFF
        )  # line:216
        O0O0O0O00O00000OO = (
            int(OOOO00O00OOO000O0[8:16], 16) << 0 & 0xFFFFFFFF
        )  # line:217
        for O00O00O00OOOO0OO0 in range(OO00O0OO0OO00O000):  # line:219
            O0O0O0OO0OOOO0OOO = O0000OOOO0O00O00O  # line:220
            O0OO000OO00000OOO = OO0OOOO00000O000O  # line:221
            OO0OO00OO0OO0OO0O = O0O0O0O00O00000OO  # line:222
            OOOOO0OOOOOOOOO0O = O0OO000OO00000OOO & 3 & 0xFFFFFFFF  # line:223
            O0O0000OOOOO00OOO = OO0OO00OO0OO0OO0O << 4 & 0xFFFFFFFF  # line:224
            O0O0O0OO0OOOO0OOO = OO0O000OO0O00O000.getShifting(
                O0O0O0OO0OOOO0OOO + (OOOOO0OOOOOOOOO0O << 2) & 0xFFFFFFFF
            )  # line:225
            O0O0000OOOOO00OOO = (
                (O0O0000OOOOO00OOO ^ (OO0O000OO0O00O000.rshift(OO0OO00OO0OO0OO0O, 5)))
                + OO0OO00OO0OO0OO0O
            ) << 0  # line:226
            O0O0O0OO0OOOO0OOO = ctypes.c_int(
                (O0O0O0OO0OOOO0OOO + O0OO000OO00000OOO) << 0 ^ 0
            ).value  # line:227
            O0O0000OOOOO00OOO = O0O0000OOOOO00OOO ^ O0O0O0OO0OOOO0OOO  # line:228
            OO00O00000OO0O00O = ctypes.c_int(
                (OO00O00000OO0O00O + O0O0000OOOOO00OOO) << 0 ^ 0
            ).value  # line:229
            OO0OOOO00000O000O = ctypes.c_int(
                (OO0OOOO00000O000O - 0x61C88647) << 0 ^ 0
            ).value  # line:230
            OOOOO0OOOOOOOOO0O = O0000OOOO0O00O00O  # line:232
            OO0OO00OO0OO0OO0O = OO00O00000OO0O00O  # line:233
            O0O0O0OO0OOOO0OOO = OO00O00000OO0O00O  # line:234
            O0O0000OOOOO00OOO = OO00O00000OO0O00O  # line:235
            O0OO000OO00000OOO = OO0OOOO00000O000O  # line:236
            O000OOOO00OOOO0O0 = format(
                OO0O000OO0O00O000.rshift((O0OO000OO00000OOO >> 0xB), 0), "b"
            )  # line:237
            if len(O000OOOO00OOOO0O0) < 3:  # line:238
                O000OOOO00OOOO0O0 = "0"  # line:239
            else:  # line:240
                O000OOOO00OOOO0O0 = O000OOOO00OOOO0O0[
                    len(O000OOOO00OOOO0O0) - 2 :
                ]  # line:241
            O0OO000OO00000OOO = int(O000OOOO00OOOO0O0, 2)  # line:243
            O0O0000OOOOO00OOO = ctypes.c_int(
                (
                    (
                        OO0O000OO0O00O000.rshift(O0O0O0OO0OOOO0OOO, 5)
                        ^ O0O0000OOOOO00OOO << 4
                    )
                    + OO0OO00OO0OO0OO0O
                )
                << 0
            ).value  # line:244
            OOOOO0OOOOOOOOO0O = OO0O000OO0O00O000.getShifting(
                OOOOO0OOOOOOOOO0O + (O0OO000OO00000OOO << 2)
            )  # line:245
            O0O0O0OO0OOOO0OOO = ctypes.c_int(
                (OO0OOOO00000O000O + OOOOO0OOOOOOOOO0O) << 0 ^ 0
            ).value  # line:246
            O0O0000OOOOO00OOO = O0O0000OOOOO00OOO ^ O0O0O0OO0OOOO0OOO  # line:247
            O0O0O0O00O00000OO = ctypes.c_int(
                (O0O0O0O00O00000OO + O0O0000OOOOO00OOO) << 0 ^ 0
            ).value  # line:248
        OO0O0OO00O0000OOO = format(
            OO0O000OO0O00O000.rshift(OO00O00000OO0O00O, 0), "x"
        )  # line:250
        O0O000O00O00O0OOO = format(
            OO0O000OO0O00O000.rshift(O0O0O0O00O00000OO, 0), "x"
        )  # line:252
        if len(OO0O0OO00O0000OOO) < 8:  # line:254
            O00000O0OOOOO00OO = 8 - len(OO0O0OO00O0000OOO)  # line:255
            for O00O00O00OOOO0OO0 in range(O00000O0OOOOO00OO):  # line:256
                OO0O0OO00O0000OOO = "0" + OO0O0OO00O0000OOO  # line:257
        if len(O0O000O00O00O0OOO) < 8:  # line:259
            O00000O0OOOOO00OO = 8 - len(O0O000O00O00O0OOO)  # line:260
            for O00O00O00OOOO0OO0 in range(O00000O0OOOOO00OO):  # line:261
                O0O000O00O00O0OOO = "0" + O0O000O00O00O0OOO  # line:262
        return OO0O0OO00O0000OOO + O0O000O00O00O0OOO  # line:264

    def reverse(O0O0OOOO00OO0O000, O000OO0OO00OO0000: str):  # line:266
        # line:267
        return (
            O000OO0OO00OO0000[6:8]
            + O000OO0OO00OO0000[4:6]
            + O000OO0OO00OO0000[2:4]
            + O000OO0OO00OO0000[0:2]
        )

    def rshift(OO00O0OOOOO00OOO0, OO0O000OOOOO00OOO, O00OOOOO0OOOO0OO0):  # line:269
        return (OO0O000OOOOO00OOO % 0x100000000) >> O00OOOOO0OOOO0OO0  # line:270

    def getUmullHigh(
        OOO0O000O0OO00000, O0OO0OOOO000OOOOO, O00O00O00OO00000O
    ):  # line:272
        O0O0OOOOO000OO000 = O0OO0OOOO000OOOOO  # line:273
        OOOO0O0OOOOO0O0O0 = O00O00O00OO00000O  # line:274
        O0O000O0O00OO0O0O = O0O0OOOOO000OO000 * OOOO0O0OOOOO0O0O0  # line:275
        OOOOOO00O0000O0O0 = format(O0O000O0O00OO0O0O, "x")  # line:276
        OOOOOO00O0000O0O0 = OOOOOO00O0000O0O0[
            0 : len(OOOOOO00O0000O0O0) - 8
        ]  # line:277
        return int(OOOOOO00O0000O0O0, 16)  # line:278

    def hex2string(OOO000O0O00O000O0, O000OO0O0OOO00OO0: int):  # line:280
        OO00OO00OOO0OOO00 = format(O000OO0O0OOO00OO0, "x")  # line:281
        if len(OO00OO00OOO0OOO00) < 2:  # line:282
            return "0" + OO00OO00OOO0OOO00  # line:283
        return OO00OO00OOO0OOO00  # line:284

    def fch(O000OOO0O00O0OOOO, O000OOOOOOOOOO00O):  # line:286
        O000OOOOOOOOOO00O = O000OOOOOOOOOO00O[
            0 : len(O000OOOOOOOOOO00O) - 21
        ]  # line:287
        OO0O00O00OO00OOO0 = binascii.crc32(
            O000OOOOOOOOOO00O.encode("utf-8")
        )  # line:288
        OO0O00O00OO00OOO0 = str(OO0O00O00OO00OOO0)  # line:289
        for OO0000O0OOO0O0O00 in range(len(OO0O00O00OO00OOO0), 10):  # line:291
            OO0O00O00OO00OOO0 = "0" + OO0O00O00OO00OOO0  # line:292
        return OO0O00O00OO00OOO0